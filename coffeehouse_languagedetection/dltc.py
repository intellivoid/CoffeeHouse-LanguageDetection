import os
import operator


class LanguagePrediction(object):

    def __init__(self):
        """
        Public Constructor
        """
        from coffeehouse_dltc.main import DLTC
        self.dltc = DLTC()
        self.model_directory = os.path.join(os.path.dirname(__file__), 'data', 'langdetect_build')
        self.dltc.load_model_cluster(self.model_directory)
        # noinspection SpellCheckingInspection
        self.language_codes = codes = {"afrikaans": "af", "amharic": "am", "arabic": "ar", "azerbaijani": "az",
                                       "belarusian": "be", "bulgarian": "bg", "bengali": "bn", "bosnian": "bs",
                                       "catalan": "ca", "cebuano": "ceb", "corsican": "co", "czech": "cs",
                                       "welsh": "cy", "danish": "da", "german": "de", "greek": "el", "english": "en",
                                       "esperanto": "eo", "spanish": "es", "estonian": "et", "basque": "eu",
                                       "persian": "fa", "finnish": "fi", "french": "fr", "frisian": "fy", "irish": "ga",
                                       "scots_gaelic": "gd", "galician": "gl", "gujarati": "gu", "hausa": "ha",
                                       "hawaiian": "haw", "hebrew": "he", "hindi": "hi", "hmong": "hmn",
                                       "croatian": "hr", "haitian_creole": "ht", "hungarian": "hu", "armenian": "hy",
                                       "indonesian": "id", "igbo": "ig", "icelandic": "is", "italian": "it",
                                       "japanese": "ja", "georgian": "ka", "kazakh": "kk", "khmer": "km",
                                       "kannada": "kn", "korean": "ko", "kurdish": "ku", "kyrgyz": "ky", "latin": "la",
                                       "luxembourgish": "lb", "lao": "lo", "lithuanian": "lt", "latvian": "lv",
                                       "malagasy": "mg", "maori": "mi", "macedonian": "mk", "malayalam": "ml",
                                       "mongolian": "mn", "marathi": "mr", "malay": "ms", "maltese": "mt",
                                       "myanmar": "my", "nepali": "ne", "dutch": "nl", "norwegian": "no",
                                       "nyanja": "ny", "odia": "or", "punjabi": "pa", "polish": "pl", "pashto": "ps",
                                       "portuguese": "pt", "romanian": "ro", "russian": "ru", "sindhi": "sd",
                                       "sinhala": "si", "slovak": "sk", "slovenian": "sl", "samoan": "sm",
                                       "shona": "sn", "somali": "so", "albanian": "sq", "serbian": "sr",
                                       "sesotho": "st", "sundanese": "su", "swedish": "sv", "swahili": "sw",
                                       "tamil": "ta", "telugu": "te", "tajik": "tg", "thai": "th", "tagalog": "tl",
                                       "turkish": "tr", "uyghur": "ug", "ukrainian": "uk", "urdu": "ur", "uzbek": "uz",
                                       "vietnamese": "vi", "xhosa": "xh", "yiddish": "yi", "yoruba": "yo",
                                       "chinese_simplified": "zh", "chinese_traditional": "zh", "zulu": "zu"}

    def predict(self, text_input):
        """
        Takes the user input and predicts if the input is either
        spam or ham

        :param text_input:
        :return: Returns dictionary of predicted values.
        """
        results = self.dltc.predict_from_text(text_input)
        results = sorted(zip(list(results.keys()), list(results.values())), key=operator.itemgetter(1), reverse=True)
        return_results = []
        for language in results:
            language = list(language)
            return_results.append({"language": self.language_codes[language[0]], "probability": language[1]})
        return return_results


_dltc = LanguagePrediction()
predict = _dltc.predict
