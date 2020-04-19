# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('COLON', 'COMA', 'CTE_F', 'CTE_I', 'CTE_STRING', 'DIV', 'ELSE', 'EQUAL', 'FLOAT', 'GREATERTHAN', 'ID', 'IF', 'INT', 'LBRACKET', 'LESSTHAN', 'LPARENT', 'MINUS', 'MULT', 'NOEQUAL', 'PLUS', 'PRINT', 'PROGRAM', 'RBRACKET', 'RPARENT', 'SEMICOLON', 'VAR'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_ID>[a-zA-Z][a-zA-Z0-9]*)|(?P<t_INT>\\d+)|(?P<t_FLOAT>\\d+\\.\\d+)|(?P<t_CTE_STRING>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_CTE_F>[0-9]+\\.[0-9]+)|(?P<t_CTE_I>[0-9]+)|(?P<t_COLON>\\:)|(?P<t_SEMICOLON>\\;)|(?P<t_LBRACKET>\\{)|(?P<t_RBRACKET>\\})|(?P<t_LPARENT>\\()|(?P<t_RPARENT>\\))|(?P<t_NOEQUAL><>)|(?P<t_PLUS>\\+)|(?P<t_MINUS>\\-)|(?P<t_MULT>\\*)|(?P<t_COMA>,)|(?P<t_EQUAL>=)|(?P<t_LESSTHAN><)|(?P<t_GREATERTHAN>>)|(?P<t_DIV>/)', [None, ('t_ID', 'ID'), ('t_INT', 'INT'), ('t_FLOAT', 'FLOAT'), (None, 'CTE_STRING'), None, None, (None, 'CTE_F'), (None, 'CTE_I'), (None, 'COLON'), (None, 'SEMICOLON'), (None, 'LBRACKET'), (None, 'RBRACKET'), (None, 'LPARENT'), (None, 'RPARENT'), (None, 'NOEQUAL'), (None, 'PLUS'), (None, 'MINUS'), (None, 'MULT'), (None, 'COMA'), (None, 'EQUAL'), (None, 'LESSTHAN'), (None, 'GREATERTHAN'), (None, 'DIV')])]}
_lexstateignore = {'INITIAL': ' '}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
