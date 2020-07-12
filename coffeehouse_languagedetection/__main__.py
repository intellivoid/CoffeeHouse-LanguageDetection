# noinspection DuplicatedCode
import sys

from coffeehouse_languagedetection import Server


def _real_main(argv=None):
    """
    The main command-line processor

    :param argv:
    :return:
    """
    if len(argv) < 2:
        _help_menu(argv)
    if argv[1] == '--help':
        _help_menu(argv)
    if argv[1] == '--test':
        _test_model_full()
    if argv[1] == '--test-dltc':
        _test_model_dltc()
    if argv[1] == '--test-cld':
        _test_model_cld()
    if argv[1] == '--test-ld':
        _test_model_ld()
    if argv[1] == '--start-server':
        _start_server(argv)


def _start_server(argv=None):
    """
    Starts the server

    :param argv:
    :return:
    """
    server = Server()
    server.start()


def _help_menu(argv=None):
    """
    Displays the help menu and commandline usage

    :param argv:
    :return:
    """
    print(
        "CoffeeHouse LanguageDetection CLI\n\n"
        "   --help\n"
        "   --test\n"
        "   --test-dltc\n"
        "   --test-cld\n"
        "   --test-ld\n"
        "   --start-server\n"
    )
    sys.exit()


def _test_model_ld():
    """
    Test the language prediction using the LD method
    :return:
    """
    print("Loading")
    import coffeehouse_languagedetection
    print("Ready\n")

    while True:
        input_text = input("> ")
        results = coffeehouse_languagedetection.predict(input_text, dltc=False, cld=False, ld=True)
        print(results['ld'])
        print(results['ld'][0])


def _test_model_cld():
    """
    Test the language prediction using the CLD method
    :return:
    """
    print("Loading")
    import coffeehouse_languagedetection
    print("Ready\n")

    while True:
        input_text = input("> ")
        results = coffeehouse_languagedetection.predict(input_text, dltc=False, cld=True, ld=False)
        print(results['cld'])
        print(results['cld'][0])


def _test_model_dltc():
    """
    Test the language prediction using the DLTC method

    :return:
    """
    print("Loading")
    import coffeehouse_languagedetection
    print("Ready\n")

    while True:
        input_text = input("> ")
        results = coffeehouse_languagedetection.predict(input_text, dltc=True, cld=False, ld=False)
        print(results['dltc'])
        print(results['dltc'][0])


def _test_model_full():
    """
    Tests the language prediction on all method

    :return:
    """
    print("Loading")
    import coffeehouse_languagedetection
    print("Ready\n")

    while True:
        input_text = input("> ")
        results = coffeehouse_languagedetection.predict(input_text)
        print("DLCT: {0}".format(results['dltc'][0]))
        print("CLD: {0}".format(results['cld'][0]))
        print("LD: {0}".format(results['ld'][0]))


if __name__ == '__main__':
    try:
        _real_main(sys.argv)
    except KeyboardInterrupt:
        print('\nInterrupted by user')
