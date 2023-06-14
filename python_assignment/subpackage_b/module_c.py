from pathlib import Path


def number_of_lines(filepath: Path):
    """Compute number of lines in a file.

    Parameters
    ----------
    filepath : Path
        relative or absolute path to a file

    Returns
    -------
    number of lines
    """
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    return len(data)
