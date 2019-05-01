import options


CMD_ARGS = {}


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=options.URL,
                     help="start endpoint")
    parser.addoption("--browser", action="store", default=options.BROWSER,
                     help="browser")


def pytest_configure(config):
    global CMD_ARGS
    CMD_ARGS["--url"] = config.getoption("--url")
    CMD_ARGS["--browser"] = config.getoption("--browser")
    print("BBBB2 ", CMD_ARGS["--url"], CMD_ARGS["--browser"])
