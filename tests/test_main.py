def convert_tuples_to_lists(tuples):
    return [list(t) for t in tuples]

def test_convert_tuples_to_lists():
    tuples = [(1,2), (3,4), (5,6)]
    expected = [[1,2], [3,4], [5,6]]
    assert convert_tuples_to_lists(tuples) == expected
