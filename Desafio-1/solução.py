def fatores_primos(n):
    fatores = []
    # Começamos pelo primeiro número primo
    divisor = 2
    
    # O loop vai até a raiz quadrada de n para eficiência
    while divisor * divisor <= n:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor # Divide n pelo divisor (divisão inteira)
        divisor += 1
    
    # Se n ainda for maior que 1, o que sobrou é um número primo
    if n > 1:
        fatores.append(n)
        
    return fatores

# --- Testando com os exemplos do desafio ---
if __name__ == "__main__":
    print(f"630: {fatores_primos(630)}") # Esperado: [2, 3, 3, 5, 7]
    print(f"13:  {fatores_primos(13)}")  # Esperado: [13]
    print(f"100: {fatores_primos(100)}") # Esperado: [2, 2, 5, 5]
