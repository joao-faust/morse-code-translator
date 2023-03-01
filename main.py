import sys
import signal

from termcolor import colored
from core.Translator import *
from utils.custom_print import *


def signal_handler(sig, frame) -> None:
    sys.exit(0)


def options() -> None:
    print('0 - To exit')
    print('1 - To encode')
    print('2 - To decode')


def ask_op() -> str:
    options()
    op = input('> ')
    return op


def op1() -> None:
    decoded_message = input('Type here> ')

    if len(decoded_message) == 0:
        return

    message = Translator.encode(decoded_message)
    if message[0] is False:
        print(colored(f'[ERROR] - Character "{message[1]}" is invalid', 'red'))
        return
    print(message[1])


def op2() -> None:
    encoded_message = input('Type here> ')
    if len(encoded_message) == 0:
        return

    message = Translator.decode(encoded_message)
    if message[0] is False:
        print(colored(f'[ERROR] - Character "{message[1]}" is invalid', 'red'))
        return
    print(message[1])


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    custom_print('Welcome', 10)
    op = ask_op()
    while op != '0':
        if op == '1':
            op1()
        elif op == '2':
            op2()
        else:
            print('Option is invalid!')
        custom_print('', 13)
        op = ask_op()
