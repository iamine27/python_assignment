from python_assignment.subpackage_b.module_c import number_of_lines


def test_number_of_lines(data_directory, max_lines):
    filepath = data_directory.joinpath("arrivals.csv")
    assert number_of_lines(filepath) <= max_lines
