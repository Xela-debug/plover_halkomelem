# vim: set fileencoding=utf-8 :

# #TKNRGSHUOA*IEYFJZCNMPTH
KEYS = (
    '#',
    'S-', 'T-', 'X-', 'C-', 'Y-', 'N-', 'ʔ-', 'W-',
    'I-', 'E-',
    '*',
    '-Ə', '-W',
    '-S', '-Y', '-N', '-L', '-T', '-X', '-Θ', '-ʔ', '-@', '-!',
)

IMPLICIT_HYPHEN_KEYS = ('I-', 'E-', '5-', '0-', '-Ə', '-W', '*')

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'X-': '2-',
    'Y-': '3-',
    'ʔ-': '4-',
    'I-': '5-',
    'E-': '0-',
    '-S': '-6',
    '-N': '-7',
    '-T': '-8',
    '-@': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : 'S1-',
        'T-'        : 'S2-',
        'X-'        : 'T-',
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
        '-S'        : '-F',
        '-Y'        : '-R',
        '-N'        : '-P',
        '-L'        : '-B',
        '-T'        : '-L',
        '-X'        : '-G',
        '-Θ'        : '-T',
        '-ʔ'        : '-S',
        '-@'        : '-D',
        '-!'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'T-'        : 'q',
        'K-'        : 'a',
        'N-'        : 'w',
        'R-'        : 's',
        'G-'        : 'e',
        'S-'        : 'd',
        'H-'        : 'r',
        'U-'        : 'f',
        'O-'        : 'c',
        'A-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-I'        : 'n',
        '-E'        : 'm',
        '-Y'        : 'u',
        '-F'        : 'j',
        '-J'        : 'i',
        '-Z'        : 'k',
        '-C'        : 'o',
        '-N'        : 'l',
        '-M'        : 'p',
        '-P'        : ';',
        '-T'        : '[',
        '-H'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
}

#DICTIONARIES_ROOT = 'asset:plover_viet:dictionaries'
#DEFAULT_DICTIONARIES = ('viet_user.json', 'viet_main.json', 'viet_commands.json')