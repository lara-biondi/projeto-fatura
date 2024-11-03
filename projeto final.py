# Entrada do nome do usuário
nome = input('Digite seu nome: ')
print('Olá, senhora(o)', nome, 'seja bem-vindo(a)')

# Entrada do número do cartão
cartao = input('Digite o número do seu cartão,é o numero que fica perto do nome do senhor(a) no propio cartão: ')
print('Ok, anotado:', cartao)

# Entrada do valor da última compra e verificação de confirmação
valor_compra = float(input("agora por favor digite o valor da compra: R$ "))
ultima_compra = input("Essa é a última compra? Digite somente a letra (s/n) se sim ou não: ").strip().lower()

# Verificação se o usuário respondeu corretamente
while True:
    ultima_compra = input("Essa é a última compra? (s/n): ").strip().lower()
    if ultima_compra in ['s', 'n']:
        break
    print("Entrada inválida. Responda com 's' para sim ou 'n' para não.")
# Verifica se o valor digitado é "s" ou "n"
if ultima_compra != 's' and ultima_compra != 'n':
    alerta = "Por favor, insira apenas 's' ou 'n'."
    print(alerta)
    # Retorna ou finaliza aqui, dependendo do que deseja fazer

# Entrada do dia de pagamento
dia_pagamento = int(input("Informe o dia do pagamento da fatura (1-31): "))
print('Ok, anotado:', dia_pagamento)

# Função para calcular os juros do cartão
def calcular_juros_cartao(valor_fatura, dia_pagamento):
    if dia_pagamento <= 25:
        # Sem juros aplicados se pago até o dia 25
        return valor_fatura, 0
    else:
        # Calcula os dias de atraso e o juros sobre o valor da fatura
        dias_atraso = dia_pagamento - 25
        juros_fixo = valor_fatura * 0.03  # Juros fixo de 3%
        juros_dias_atraso = valor_fatura * (0.01 * dias_atraso)  # Juros de 1% ao dia de atraso
        juros_total = juros_fixo + juros_dias_atraso
        valor_com_juros = valor_fatura + juros_total
        return valor_com_juros, juros_total

# Parte do código que interage com o usuário
try:
    # Solicita o valor da fatura e o dia do pagamento
    valor_fatura = float(input("Digite o valor da fatura: R$ "))
    dia_pagamento = int(input("Digite o dia do pagamento da fatura (1-31): "))

    # Chama a função para calcular o valor com juros
    valor_com_juros, juros_total = calcular_juros_cartao(valor_fatura, dia_pagamento)

    # Exibe os resultados finais
    print(f"\nValor final da fatura com juros: R$ {valor_com_juros:.2f}")
    print(f"Quantidade total de juros aplicados: R$ {juros_total:.2f}")

except ValueError:
    print("Por favor, insira valores numéricos válidos para a fatura e o dia de pagamento.")