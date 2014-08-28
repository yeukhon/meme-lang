import lexer
import tokens

program = """\
yo x iz 1

one does not simply get out until x iz 2
wow "x is not 2 yet"
let x be 2
end
wow "x is now 2"
"""

for token in lexer.tokens(program, tokens.MEME_DEFINITIONS):
    print(token)
