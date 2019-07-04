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
    
def test_between(upper_limit, lower_limit, actual):
    """
    Check to ensure that a number is between two other numbers. Raises
    AssertionError if the number is not between the other two numbers
    """
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)