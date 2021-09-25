import abc
class Command():
    def __init__(self, func, params):
        self.func = func
        self.params = params

    # @abc.abstractmethod
    def execute(self):
        """Method to execute the command."""
        self.func(self.params)

    @abc.abstractmethod
    def undo(self):
        """A method to undo the command."""
        pass
