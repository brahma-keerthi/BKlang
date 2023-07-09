from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input("BKlang >> ")

    if ( text == 'devinfo' ):
        print('Brahma Keerthi H S\nComputer Science Student\n')

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()

    if result is not None:
        print(result)
    else:
        print('Syntax Error\n1. To perform operations >> 3 * 2 .....\n2. To create variables >> get a = 2\n3. Comparition operators >> ?= equals to, != not equals to...\n4. If-else blocks >> if a < b do get a = a + 1 elif a ?= b do get a = a + 2 else do b = b + 1\n5. While loop >> while a < b do get a = a + 2\n6. To get devloper details >> devinfo\n')