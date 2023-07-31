CHAR_TO_MORSE_MAP = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                     'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
                     'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
                     'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
                     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                     '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}
MORSE_TO_CHAR_MAP = {v: k for k, v in CHAR_TO_MORSE_MAP.items()}

SIGNAL_FRAME_PERIOD = 10  # 10 ms


class MorseEngine:
    def __init__(self, tapping_speed=.08):
        self.tapping_speed = tapping_speed
        self.short_duration_threshold = tapping_speed * SIGNAL_FRAME_PERIOD
        self.short_pause_duration_threshold = tapping_speed * SIGNAL_FRAME_PERIOD * 3
        self.long_pause_duration_threshold = tapping_speed * SIGNAL_FRAME_PERIOD * 7

    def signal_to_text(self, signal):
        morse = self.signal_to_morse(signal)
        text = self.morse_to_text(morse)
        return text

    def signal_to_morse(self, signal):
        morse = [dur for dur in signal.replace('U', 'D').split('D') if dur != '']
        up = []
        for duration in morse[::2]:
            duration = int(duration)
            if duration <= self.short_pause_duration_threshold:
                up.append('')
            elif int(duration) <= self.long_pause_duration_threshold:
                up.append(' ')
            else:
                up.append(' / ')

        down = ['.' if int(duration) <= self.short_duration_threshold else '-' for duration in morse[1::2]]
        morse = ''.join([x for y in zip(up, down) for x in y])
        return morse

    @classmethod
    def morse_to_text(cls, morse):
        morse_breakdown = [MORSE_TO_CHAR_MAP.get(morse_block, '�') for morse_block in morse.split(' ') if morse_block != '']
        text = ''.join(morse_breakdown).strip()
        return text

    @classmethod
    def text_to_morse(cls, text):
        morse = ' '.join([CHAR_TO_MORSE_MAP.get(c, '') for c in text])
        return morse


if __name__ == '__main__':
    me = MorseEngine()
    sample_signal = '23U1D1U1D1U1D1U1D12U1D7U1D2U7D2U1D11U2D7U1D2U7D2U1D1U1D11U6D1U6D1U6D20U'

    sample_morse = me.signal_to_morse(sample_signal)
    print(sample_morse)

    sample_text = me.morse_to_text(sample_morse)
    print(sample_text)

    sample_reversed_morse = me.text_to_morse(sample_text)
    print(sample_reversed_morse)

    print(me.text_to_morse('hello world'))
