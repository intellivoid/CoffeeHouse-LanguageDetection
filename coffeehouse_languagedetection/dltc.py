import os


class LanguagePrediction(object):

    def __init__(self):
        """
        Public Constructor
        """
        from coffeehouse_dltc.main import DLTC
        self.dltc = DLTC()
        self.model_directory = os.path.join(os.path.dirname(__file__), 'data')
        self.dltc.load_model_cluster(self.model_directory)

    def predict(self, text_input):
        """
        Takes the user input and predicts if the input is either
        spam or ham

        :param text_input:
        :return: Returns dictionary of predicted values.
        """
        return self.dltc.predict_from_text(text_input)


_dltc = LanguagePrediction()
predict = _dltc.predict
