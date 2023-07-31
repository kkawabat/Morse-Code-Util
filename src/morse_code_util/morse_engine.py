import numpy as np

MORSE_TRANSLATION_MAP = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                         'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                         'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                         'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
                         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                         '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}


class MorseEngine:
    self.morse_unit = .08
    self.duration_map = {'dot': morse_unit, 'dash': morse_unit * 3, 'short_pause': morse_unit * 3, 'long_pause': morse_unit * 7}

    def __init__(self, morse_unit=None, duration_map=None):
        if morse_unit is not None:
            self.morse_unit = morse_unit
        if duration_map is not None:
            self.duration_map = duration_map

    @classmethod
    def signal_to_text(cls, signal):
        morse = cls.signal_to_morse(signal)
        text = cls.morse_to_text(morse)
        return text

    @classmethod
    def signal_to_morse(cls, signal):
        morse = ''
        return morse

    @classmethod
    def morse_to_text(cls, morse):
        text = ''
        return text

    @classmethod
    def text_to_morse(cls, text):
        morse = ''
        return morse


if __name__ == '__main__':
    me = MorseEngine()
    me.text_to_morse_sound('hello')
    me.text_to_morse_sound('      ')
    # me.text_to_morse_sound('soasdfasdfs')
    # me.text_to_morse_sound('soasdfasdfs')
