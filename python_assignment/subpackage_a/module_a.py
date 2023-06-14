def _add(x: int, y: int) -> int:
    # for private function it's ok not to have a docstring.
    return x + y


def add(x: int, y: int = 42) -> int:
    """Add two variables.

    Adds two variables and gives the sum. Note, sum is commutative, the order of
    parameters does not matter.

    Parameters
    ----------
    x : int
        First variable to be added.
    y : int
        Second variable.

    Returns
    -------
    int
        Sum of x and y.

    Raises
    ------
    ValueError
        If `x` is equal to -1.
    """
    if x == -1:
        raise ValueError("Tabu value.")
    return _add(x, y)
