TK_YO = "TK_YO"
TK_ID = "TK_ID"
TK_IZ = "TK_IZ"
TK_EQUAL = "TK_EQUAL"
TK_ONE_DOES_NOT = "TK_ONE DOES NOT"
TK_WHALE = "TK_WHALE"
TK_LET = "TK_LET"
TK_BE = "TK_BE"
TK_WOW = "TK_WOW"
TK_END = "TK_END"
TK_STRING = "TK_STRING"
TK_COMMENT = "TK_COMMENT"
TK_NUMBER = "TK_NUMBER"
TK_WHITESPACE = "TK_WHITESPACE"

MEME_DEFINITIONS = [
    (r'[\s\n\t]+', TK_WHITESPACE),
    (r'#[^\\n]*', TK_COMMENT),
    (r'\".+\"', TK_STRING),
    (r'yo', TK_YO),
    (r'iz', TK_IZ),
    (r'one does not simply get out until', TK_ONE_DOES_NOT),
    (r'whale', TK_WHALE),
    (r'let', TK_LET),
    (r'be', TK_BE),
    (r'wow', TK_WOW),
    (r'end', TK_END),
    (r'equal', TK_EQUAL),
    (r'[a-zA-Z][a-zA-Z_]*', TK_ID),
    (r'\d+(?:\.\d*)?', TK_NUMBER)
]
