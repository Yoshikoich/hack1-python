"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    contador = 0
    inicio = 6
    while contador < 6:
        inicio = inicio - 1
        result.append(inicio)
        contador = contador + 1
    return result  

fn_hack_7()

