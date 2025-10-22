# Resumo sobre Recursividade em Python

# A recursividade é um conceito onde uma função chama a si mesma para resolver um problema.
# Ela é dividida em duas partes:
# 1. Caso Base: Quando a função não chama mais a si mesma, geralmente para evitar loops infinitos.
# 2. Chamada Recursiva: A função se chama para resolver uma versão menor do problema.

# Exemplo: Cálculo do Fatorial de um número

def fatorial(n):
    # Caso Base: quando n é 0, o fatorial é 1
    if n == 0:
        return 1
    # Chamada Recursiva: n * fatorial de (n-1)
    else:
        return n * fatorial(n - 1)

# Testando a função fatorial
print(fatorial(5))  # Saída: 120

# Explicação:
# fatorial(5) = 5 * fatorial(4)
# fatorial(4) = 4 * fatorial(3)
# fatorial(3) = 3 * fatorial(2)
# fatorial(2) = 2 * fatorial(1)
# fatorial(1) = 1 * fatorial(0)
# fatorial(0) = 1 (Caso Base)
# Resultado final: 120

# Vantagens da Recursividade:
# 1. Clareza e Intuitividade:
#    - A recursividade traduz diretamente definições matemáticas, tornando o código mais fácil de entender para quem conhece a base teórica.
# 2. Redução de Linhas de Código:
#    - Soluções recursivas frequentemente resultam em códigos mais concisos do que suas versões iterativas.
# 3. Soluções Elegantes:
#    - Alguns problemas têm soluções mais elegantes e simples quando abordados recursivamente.

# Desvantagens da Recursividade:
# 1. Consumo de Memória:
#    - Soluções recursivas podem consumir mais memória devido ao armazenamento de variáveis intermediárias.
# 2. Performance:
#    - Devido à alocação de memória, soluções recursivas podem ser mais lentas em comparação com soluções iterativas.
# 3. Estouro de Pilha:
#    - Chamadas recursivas ocupam espaço na pilha de memória, e chamadas em excesso podem resultar em estouro de pilha (stack overflow).
# 4. Dificuldade de Debug:
#    - O rastreamento de problemas em funções recursivas pode ser desafiador devido ao número de chamadas de função que podem se acumular.
