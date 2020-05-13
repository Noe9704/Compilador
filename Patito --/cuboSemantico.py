'''
tipo = typeOperator['int']['int']['+']
if tipo is None:
    ERROR
'''

typeOperator = {
    "int" : {
        "int" : {
            "+" : "int",
            "-" : "int",
            "*" : "int",
            "/" : "int",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "and" : None,
            "or" : None            
        },
        "float" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "and" : None,
            "or" : None            
        },
        "char" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None
        }
    },
    "float" : {
        "int" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "and" : None,
            "or" : None            
        },
        "float" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "and" : None,
            "or" : None            
        },
        "char" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None
        }
    },
    "char" : {
        "int" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None            
        },
        "float" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None            
        },
        "char" : {
            "+" : "char",
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : "bool",
            "and" : None,
            "or" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None
        }
    },
    "bool" : {
        "int" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None            
        },
        "float" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None            
        },
        "char" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "and" : None,
            "or" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : "bool",
            "and" : "bool",
            "or" : "bool"
        }
    }
}

def ReturnType(opA,opB,operator):
    return typeOperator[opA][opB][operator]

    
    








