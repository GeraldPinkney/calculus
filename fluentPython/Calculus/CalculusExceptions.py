# CalculusExceptions


# class Error is derived from super class Exception
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class StateError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, state, action, msg):
        self.state = state
        self.action = action

        # Error message thrown is saved in msg
        self.msg = msg


class RoundError(Error):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, state, action, msg):
        self.state = state
        self.action = action

        # Error message thrown is saved in msg
        self.msg = msg


"""
try:
    raise (StateError(2, 3 * 2, "Not Allowed"))

# Value of Exception is stored in error
except StateError as error:
    print('Exception occured: ', error.msg)
"""
