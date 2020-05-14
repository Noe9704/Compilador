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
            "=" : "int",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "&" : None,
            "|" : "bool"            
        },
        "float" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            "=" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "&" : None,
            "|" : "bool"            
        },
        "char" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None
        }
    },
    "float" : {
        "int" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            "=" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "&" : "bool",
            "|" : "bool"            
        },
        "float" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            "=" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "&" : "bool",
            "|" : "bool"           
        },
        "char" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None
        }
    },
    "char" : {
        "int" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None            
        },
        "float" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None            
        },
        "char" : {
            "+" : "char",
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : "char",
            ">" : None,
            "<" : None,
            "==" : "bool",
            "&" : None,
            "|" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None
        }
    },
    "bool" : {
        "int" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None            
        },
        "float" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None            
        },
        "char" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            ">" : None,
            "<" : None,
            "==" : None,
            "&" : None,
            "|" : None
        },
        "bool" : {
            "+" : None,
            "-" : None,
            "*" : None,
            "/" : None,
            "=" : "bool",
            ">" : "bool",
            "<" : None,
            "==" : "bool",
            "&" : "bool",
            "|" : "bool"
        }
    }
}

def ReturnType(opA,opB,operator):
    return typeOperator[opA][opB][operator]

    
    








