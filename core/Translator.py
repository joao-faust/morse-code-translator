from core.Dictionary import *
from unidecode import unidecode


class Translator:

    @staticmethod
    def encode(content: str) -> tuple:
        dic = Dictionary.encode()
        message_to_list = list(unidecode(content.lower()))
        encoded_message = ''

        isValid = True
        i = 0
        while isValid and i < len(message_to_list):
            if message_to_list[i] not in dic:
                isValid = False
            else:
                letter = message_to_list[i]
                encoded_message += f'{dic[letter]} '
            i += 1

        if isValid is False:
            return False, message_to_list[i-1]
        return True, encoded_message


    @staticmethod
    def decode(content: str) -> tuple:
        dic = Dictionary.decode()
        message_to_list = content.lower().split()
        decoded_message = ''

        isValid = True
        i = 0
        while isValid and i < len(message_to_list):
            if message_to_list[i] not in dic:
                isValid = False
            else:
                code = message_to_list[i]
                decoded_message += dic[code]
            i += 1

        if isValid is False:
            return False, message_to_list[i-1]
        return True, decoded_message
