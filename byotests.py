def number_of_evens(number):
    return False

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, but got {1}".format(expected, actual)
    
def test_is_in_collection(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in_collection(collection, item):
    assert item not in collection, "{0} does contain {1]".format(collection, item)
    
def test_between_numbers(range, number):
    assert number in range, "{0} does not contain {1}".format(range, number)
    
    