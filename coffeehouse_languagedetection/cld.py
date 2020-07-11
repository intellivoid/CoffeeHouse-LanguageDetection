import operator
import pathlib

import joblib

from . import utils

DEFAULT_DATA_DIR: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "data"


class ContentLanguageIdentifier:
    """
    Args:
        data_dir (str|path)
        max_text_len (int)

    Attributes:
        pipeline (:class:`sklearn.pipeline.Pipeline`)
    """

    def __init__(self, data_dir=DEFAULT_DATA_DIR, max_text_len=1000):
        self._version = 1.1
        self._model_id = self._get_model_id()
        self.data_dir = utils.to_path(data_dir).resolve()
        self.filename = self._model_id + ".pkl.gz"
        self.max_text_len = max_text_len
        self._pipeline = None

    @property
    def pipeline(self):
        if not self._pipeline:
            self._pipeline = self._load_pipeline()
        return self._pipeline

    def _load_pipeline(self):
        filepath = self.data_dir.joinpath(self.filename)
        with filepath.open(mode="rb") as f:
            pipeline = joblib.load(f)
        return pipeline

    def _get_model_id(self):
        fstub = "lang-identifier-v{}-sklearn"
        try:
            import pkg_resources
            filename = fstub.format(self._version)
        except ImportError:
            import sklearn
            filename = fstub.format(self._version)
        return filename

    def identify_lang(self, text):
        """
        Identify the most probable language identified in ``text``.

        Args:
            text (str)

        Returns:
            str: 2-letter language code of the most probable language.
        """
        text_ = utils.to_collection(text[:self.max_text_len], str, list)
        if self._is_valid(text_[0]):
            lang = self.pipeline.predict(text_).item()
            return lang
        else:
            return "un"

    def identify_topn_langs(self, text):
        """
        Identify the ``topn`` most probable languages identified in ``text``.

        Args:
            text (str)

        Returns:
            List[Tuple[str, float]]: 2-letter language code and its probability
            for the ``topn`` most probable languages.
        """
        text_ = utils.to_collection(text[:self.max_text_len], str, list)
        if self._is_valid(text_[0]):
            lang_probs = sorted(
                zip(self.pipeline.classes_, self.pipeline.predict_proba(text_).flat),
                key=operator.itemgetter(1),
                reverse=True,
            )
            items = [(lang.item(), prob.item()) for lang, prob in lang_probs]
            return_results = []

            for probability in items:
                return_results.append({
                    "language": list(probability)[0],
                    "probability": list(probability)[1]
                })

            return return_results
        else:
            return [("un", 1.0)]

    def _is_valid(self, text):
        return any(char.isalpha() for char in text)

    def init_pipeline(self):
        """
        Initialize a *new* language identification pipeline, overwriting any
        pre-trained pipeline loaded from disk under :attr:`LangIdentifier.data_dir`.
        Must be trained on (text, lang) examples before use.
        """
        import sklearn.feature_extraction
        import sklearn.pipeline

        self._pipeline = sklearn.pipeline.Pipeline(
            [
                (
                    "vectorizer",
                    sklearn.feature_extraction.text.HashingVectorizer(
                        analyzer="char_wb", ngram_range=(1, 3), lowercase=True,
                        n_features=4096, norm="l2",
                    )
                ),
                (
                    "classifier",
                    sklearn.neural_network.MLPClassifier(
                        activation="relu", solver="adam",
                        hidden_layer_sizes=(512,), alpha=0.0001, batch_size=512,
                        learning_rate_init=0.001, learning_rate="constant",
                        max_iter=15, early_stopping=True, tol=0.001,
                        shuffle=True, random_state=42,
                        verbose=True,
                    )
                ),
            ]
        )


_cld = ContentLanguageIdentifier()
detect = _cld.identify_lang
predict = _cld.identify_topn_langs