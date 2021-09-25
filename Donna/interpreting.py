import media
import commands


class Interpreter:
    def __init__(self):
        pass
    def interpret(self, sentence):
        function = known_commands[sentence.verb.lower()]
        dir_obj = sentence.dir_obj
        return commands.Command(function, dir_obj)

#Very primitive proof of concept
known_commands = {"play": media.play}