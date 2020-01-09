import sh
import pytest
import os
import platform

def test_version():
    """
    Test that the CI runs with the expected python version
    """
    # expected version
    try:
        sh.python(['--version'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)


@pytest.mark.parametrize('mode', ['test', 'run', 'bench'])
@pytest.mark.parametrize('problem', ['acoustic', 'tti'])
def test_bench(mode, problem):
    """
    Test that the CI runs with the expected python version
    """
    # expected version
    try:
        sh.python(['benchmarks/user/benchmark.py', mode, '-P', problem, '-d','100', '100', '100'])
    except sh.ErrorReturnCode as e:
        pytest.fail(e)