from pathlib import Path

import pytest

_TEST_FOLDER = Path(__file__).parent.absolute()
_DATA_FOLDER = (_TEST_FOLDER / "data").resolve(strict=True)


@pytest.fixture
def data_directory() -> Path:
    return _DATA_FOLDER
