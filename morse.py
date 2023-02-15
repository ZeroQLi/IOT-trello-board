from gpiozero import LED
from time import sleep

# morse code dict
morse = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    ' ': ' '
}

''' from Wikipedia: https://en.wikipedia.org/wiki/Morse_code
International Morse code is composed of five elements:
- short mark, dot or "dit": "dot duration" is one time unit long
- longer mark, dash or "dah": three time units long
- inter-element gap between the dots and dashes within a character: one dot duration or one unit long
- short gap (between letters): three time units long
- medium gap (between words): seven time units long
'''

# timing: change unit (in secs) to make slower or faster

unit = 0.25
short = unit
longer = 3 * unit
inter_element_gap = unit
short_gap = 3 * unit - inter_element_gap
medium_gap = 7 * unit - short_gap

# the led
led = LED(27)

def blink(duration):
    led.on()
    sleep(duration)
    led.off()

def dot():
    blink(short)

def dash():
    blink(longer)

def space():
    sleep(medium_gap)

# mapping between symbol and function to be called
signal = {
    '.': dot,
    '_': dash,
    ' ': space
    }

message = input("What's the message? ")

for character in message.lower():
    for symbol in morse[character]:
        print(symbol, end='', flush=True)
        signal[symbol]()
        sleep(inter_element_gap)
    print(' / ', end='', flush=True)
    sleep(short_gap)
print()
