# http://dojopuzzles.com/problemas/exibe/contando-as-letras-dos-numeros/

unidades = {
    0: 0,
    1: 2,
    2: 4,
    3: 4,
    4: 6,
    5: 5,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 3,
    11: 4,
    12: 4,
    13: 5,
    14: 8,
    15: 6,
    16: 9,
    17: 9,
    18: 7,
    19: 8
    
}
dezena = {
   20: 5, 
   30: 6,
   40: 8,
   50: 9,
   60: 8,
   70: 7,
   80: 7,
   90: 7
}

conjuncao_e = 1

def conta_caracteres(n):    
    soma = 0
    valor = 0
    for i in range(1,n+1):
        if i < 20:
            valor = unidades[i]
        
        if i >= 20:
            uni = n % 10
            dez = n // 10

            if uni == 0:
                valor = unidades[uni] + dezena[dez*10]
            else:
                valor = unidades[uni] + dezena[dez*10] + conjuncao_e
                
        soma = soma + valor    
    return soma


def test_inicial():
    esperado = 2
    resultado = conta_caracteres(1)
    assert esperado == resultado

def test_ate_dois():
    esperado = 6
    resultado = conta_caracteres(2)
    assert esperado == resultado

def test_ate_tres():
    esperado = 10
    resultado = conta_caracteres(3)
    assert esperado == resultado

def test_ate_cinco():
    esperado = 21
    resultado = conta_caracteres(5)
    assert esperado == resultado

def test_ate_dezenove():
    esperado = 100
    resultado = conta_caracteres(19)
    assert esperado == resultado

def test_ate_vinte():
    esperado = 105
    resultado = conta_caracteres(20)
    assert esperado == resultado

def test_ate_vinte_um():
    esperado = 113
    resultado = conta_caracteres(21)
    assert esperado == resultado


test_inicial()
test_ate_dois()
test_ate_tres()
test_ate_cinco()
test_ate_dezenove()
test_ate_vinte()
test_ate_vinte_um()