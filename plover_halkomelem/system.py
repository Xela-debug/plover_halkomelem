# vim: set fileencoding=utf-8 :

# #TKNRGSHUOA*IEYFJZCNMPTH
KEYS = (
    '#',
    'S-', 'X-', 'T-', 'C-', 'Y-', 'N-', 'ʔ-', 'W-',
    'I-', 'E-',
    '*',
    '-Ə', '-W',
    '-T', '-X', '-S', '-L', '-N', '-Y', '-Θ', '-ʔ', '-@', '-!',
)

IMPLICIT_HYPHEN_KEYS = ('I-', 'E-', '5-', '0-', '-Ə', '-W', '*')

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'T-': '2-',
    'Y-': '3-',
    'ʔ-': '4-',
    'I-': '5-',
    'E-': '0-',
    '-T': '-6',
    '-S': '-7',
    '-N': '-8',
    '-Θ': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : 'S1-',
        'X-'        : 'S2-',
        'T-'        : 'T-',
        'C-'        : 'K-',
        'Y-'        : 'P-',
        'N-'        : 'W-',
        'ʔ-'        : 'H-',
        'W-'        : 'R-',
        'I-'        : 'A-',
        'E-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-Ə'        : '-E',
        '-W'        : '-U',
        '-T'        : '-F',
        '-X'        : '-R',
        '-S'        : '-P',
        '-L'        : '-B',
        '-N'        : '-L',
        '-Y'        : '-G',
        '-Θ'        : '-T',
        '-ʔ'        : '-S',
        '-@'        : '-D',
        '-!'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : 'q',
        'X-'        : 'a',
        'T-'        : 'w',
        'C-'        : 's',
        'Y-'        : 'e',
        'N-'        : 'd',
        'ʔ-'        : 'r',
        'W-'        : 'f',
        'I-'        : 'c',
        'E-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-Ə'        : 'n',
        '-W'        : 'm',
        '-T'        : 'u',
        '-X'        : 'j',
        '-S'        : 'i',
        '-L'        : 'k',
        '-N'        : 'o',
        '-Y'        : 'l',
        '-Θ'        : 'p',
        '-ʔ'        : ';',
        '-@'        : '[',
        '-!'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
}

DICTIONARIES_ROOT = 'asset:plover_halkomelem:dictionaries'
#DEFAULT_DICTIONARIES = ('halkomelem_user.json', 'halkomelem_main.json', 'halkomelem_commands.json')