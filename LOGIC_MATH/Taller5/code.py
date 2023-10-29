def coeficiente_binomial(n, k):
    """Calcula el coeficiente binomial C(n, k)"""
    if k == 0 or k == n:
        return 1
    else:
        return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)

def expansion_binomio(n):
    """Calcula la expansión del binomio (a + b)^n"""
    terms = []
    for k in range(n + 1):
        coeficiente = coeficiente_binomial(n, k)
        term = ""
        if coeficiente != 1:
            term += str(coeficiente)
        if n - k > 0:
            term += f"({a}^{n - k})"
        if k > 0:
            term += f"({b}^{k})"
        terms.append(term)
    return " + ".join(terms)

# Ejemplo de uso
a = "a"
b = "b"
n = 4
expansion = expansion_binomio(n)
print(f"La expansión de ({a} + {b})^{n} es: {expansion}")
