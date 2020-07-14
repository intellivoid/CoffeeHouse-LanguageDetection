from .server import *

__all__ = ["Server"]


def predict(text_input, dltc=True, ld=True, cld=True, seed=None, as_string=False):
    """
    Predicts the language using the three different methods

    :param as_string:
    :param text_input:
    :param dltc:
    :param ld:
    :param cld:
    :param seed:
    :return:
    """
    results = {}
    if dltc:
        import coffeehouse_languagedetection.dltc
        results["dltc"] = coffeehouse_languagedetection.dltc.predict(text_input, as_string)
    if ld:
        import coffeehouse_languagedetection.ld
        if seed is None:
            results["ld"] = coffeehouse_languagedetection.ld.predict(text_input)
        else:
            results["ld"] = coffeehouse_languagedetection.ld.predict(text_input, seed)
    if cld:
        import coffeehouse_languagedetection.cld
        results["cld"] = coffeehouse_languagedetection.cld.predict(text_input)
    return results
