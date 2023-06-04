import pytest
from calculator import Calculator
from icalc import InteractiveCalculator
import io
from contextlib import redirect_stdout


def pytest_configure(config):
    # register new markers
    config.addinivalue_line(
        "markers",
        "key: specify a test key"
    )
    config.addinivalue_line(
        "markers",
        "calc_method: method name in Calculator"
    )
    config.addinivalue_line(
        "markers",
        "i_calc_method: method name in Interactive Calculator"
    )


def pytest_addoption(parser):
    # new options
    parser.addoption('--key', action='store', help='can be used to mark and run specific tests')
    parser.addoption('--calculator', action='store', default='calc',
                     help='which calculator would you like to test: Calculator or InteractiveCalculator')


def pytest_collection_modifyitems(config, items):
    # check if you got an option like --key=rob -> only robustness tests will be executed
    filter = config.getoption("--key")
    if filter:
        new_items = []
        for item in items:
            mark = item.get_closest_marker("key")
            if mark and mark.args and mark.args[0] == filter:
                # collect all items that have a key marker with that value
                new_items.append(item)
        items[:] = new_items


@pytest.fixture
def method(request):
    """

    :return: tested method of normal or interactive calculator
    """

    mode = request.config.getoption('--calculator')

    if mode == 'calc':
        mark = request.node.get_closest_marker('calc_method')
        calc = Calculator()
        return calc.__getattribute__(mark.args[0])
    else:
        mark = request.node.get_closest_marker('i_calc_method')

        calc_method = mark.args[0]
        if calc_method is None:
            return pytest.skip('method is not implemented')

        def _cmd(*args):
            calc = InteractiveCalculator()
            stdout_ = io.StringIO()
            with redirect_stdout(stdout_):
                cmd = ' '.join([calc_method] + [f'{a_}' for a_ in args])
                calc.onecmd(cmd)

            retval = stdout_.getvalue()
            if retval:
                if calc_method.startswith('b'):  # bitwise operator
                    return int(retval)
                else:
                    return float(retval)

        return _cmd
