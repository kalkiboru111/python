from byotest import *

''' doc-string
eur_coins = [100, 50, 20, 10, 5, 2, 1]
usd_coins = [100, 50, 25, 10, 5, 1]
'''

#storing coin values in dictionary

''' Working with dictionary of EU coins
usd_coins = {
    1: 20, 
    5: 20, 
    10: 20, 
    25: 20, 
    50 :20, 
    100:20
}

'''

eur_coins = { 
    1: 20, 
    2: 20, 
    5: 20, 
    10: 20, 
    20: 20, 
    50: 20, 
    100: 20
}

def get_change(amount, coins=eur_coins):
    change = []
    for coin in coins:
        while coin <= amount:
            if coins[coin] == 0:

            else:
                amount -=coin
                change.append(coin)
            else:
                return False
            
           
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(9), [5,2,2])
test_are_equal(get_change(35, usd_coins), [25,10])

print("All tests pass!")

def test_exception_was_raised(func, args, message):
    """
    Test that an error gets thrown inside of a given function. Raises
    AssertionError if the error message was different from the expected
    message
    `func` is a reference to the function that is to be called
    `args` is a tuple containing the arguments that are to be provided to
        `func`
    `message` is the string that is expected to be output by the error once
        it's thrown
    """
    try:
        # Call the function and unpack the `args` tuple by using `*`. This
        # will unpack each of the items from the `args` tuple to pass 
        # them into the function as arguments
        func(*args)

        # Execution will cease at this point if the error was successfully
        # thrown, and will move onto the `except` block. If the
        # function was successfully executed without throwing an error, we'll
        # raise an AssertionError here to inform the developer that the
        # function didn't throw an error as expected
        assert False, "Exception was not raised"
    except Exception as e:
        # The message that was thrown will be stored in the exception
        # instance as the first item in the list of `args`. This will allow us
        # to check to see if the message that was thrown is the same as the
        # message that the developer was expecting 
        assert e.args[0] == message, "The message that was provided did not match the message thrown"