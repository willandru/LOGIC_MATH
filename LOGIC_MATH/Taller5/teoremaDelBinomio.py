def coeficiente_binomial(n, k):
    """Calcula el coeficiente binomial C(n, k)"""
    if k == 0 or k == n:
        return 1
    else:
        return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)

def expansion_binomio(a, b, n):
    """Calcula la expansión del binomio (a + b)^n"""
    expansion = ""
    for k in range(n + 1):
        coeficiente = coeficiente_binomial(n, k)
        termino = ""
        if coeficiente != 1:
            termino += str(coeficiente)
        if n - k > 0:
            termino += f"{a}^{n - k}"
        if k > 0:
            termino += f"{b}^{k}"
        expansion += termino + " + "
    # Elimina el último "+"
    expansion = expansion[:-3]
    return expansion

# Ejemplo de uso
a = "a"
b = "b"
n = 4
expansion = expansion_binomio(a, b, n)
print(f"La expansión de ({a} + {b})^{n} es: {expansion}")
