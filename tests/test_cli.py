from pathlib import Path
from shlex import split

import pytest

import copier
from copier.cli import CopierApp

SIMPLE_DEMO_PATH = Path(__file__).parent / "demo_simple"


def test_good_cli_run(dst):
    run_result = CopierApp.run(["--quiet", str(SIMPLE_DEMO_PATH), str(dst)], exit=False)
    a_txt = dst / "a.txt"
    assert run_result[1] == 0
    assert a_txt.exists()
    assert a_txt.is_file()
    assert a_txt.read_text().strip() == "EXAMPLE_CONTENT"