from .cld import *


def cld_predict(text_input):
    return cld.identify_language(text_input)
