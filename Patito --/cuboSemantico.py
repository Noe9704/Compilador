
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
            "and" : "error",
            "or" : "error"            
        },
        "float" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "and" : "error",
            "or" : "error"            
        },
        "char" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"
        },
        "bool" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"
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
            "and" : "error",
            "or" : "error"            
        },
        "float" : {
            "+" : "float",
            "-" : "float",
            "*" : "float",
            "/" : "float",
            ">" : "bool",
            "<" : "bool",
            "==" : "bool",
            "and" : "error",
            "or" : "error"            
        },
        "char" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"
        },
        "bool" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"
        }
    },
    "char" : {
        "int" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"            
        },
        "float" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"            
        },
        "char" : {
            "+" : "char",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "bool",
            "and" : "error",
            "or" : "error"
        },
        "bool" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"
        }
    },
    "bool" : {
        "int" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"            
        },
        "float" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"            
        },
        "char" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "error",
            "and" : "error",
            "or" : "error"
        },
        "bool" : {
            "+" : "error",
            "-" : "error",
            "*" : "error",
            "/" : "error",
            ">" : "error",
            "<" : "error",
            "==" : "bool",
            "and" : "bool",
            "or" : "bool"
        }
    }
}

def ReturnType(opA,opB,operator):
    return typeOperator[opA][opB][operator]

    
    








