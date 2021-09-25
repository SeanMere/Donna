""" Donna
The Donna program is the rudimentary beginnings of a virtual assistant a la Alexa or Siri. It borrows its name from the assistant in the show Suits.
Currently the proof of concept only supports finding and playing Youtube videos. The over-modulization may be considered to be 'too much', but hopefully
lays a framework for easily extensible code.
Mostly the combination of api's of others.
"""
import interpreting
import nlp
import listening
import invoking
import speaker


nlp_parser = nlp.Parser()
interpreter = interpreting.Interpreter()
invoker = invoking.Invoker()

while True:
    speaker.speak("How can I help you?")
    request = listening.listen()
    sentence = nlp_parser.parse(request)
    commands = interpreter.interpret(sentence)
    invoker.invoke(commands)


