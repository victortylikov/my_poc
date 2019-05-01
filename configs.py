import sys


def make_command_argument_dict() -> dict:
    url = get_argument_url()
    return {"url": url}


def get_argument_url() -> str:
    url = _get_value_for_cmd_arg("--url")
    return url


def _get_value_for_cmd_arg(flag_value):
    if flag_value not in sys.argv:
        return None

    index_of_flag = sys.argv.index(flag_value)
    index_of_value = index_of_flag + 1
    return sys.argv[index_of_value]
