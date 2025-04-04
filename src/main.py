"""Sistema bancário simples"""

from datetime import datetime

#  v1.0
# ~ TODO: Operação de depósito
# ~ Deve ser possível depositar valores positivos para a conta bancária.
# ~ A v1 do projeto trabalha apenas com 1 usuário, dessa forma não é preciso se
# ~ preocupar em identificar qual o número da conta ou da agência.
# ~ Todos os depósitos devem ser armazenados em uma variável e exibidos na
# ~ operação de extrato.

# ~ TODO: Operação de saque
# ~ O sistema deve permitir realizar 3 saques diários com limite máximo de
# ~ R$ 500,00 por saque.
# ~ Caso o usuário não tenha saldo suficiente na conta, o sistema deve exibir
# ~ uma mensagem informando que não poderá sacar por saldo insuficiente.
# ~ Todos os saques devem ser armazenados em uma variável e exibidos na
# ~ operação de extrato.

# ~ TODO: Operação de extrato
# ~ Essa operação deve listar todos os depósitos e saques realizados na conta.
# ~ No fim da listagem deve ser exibido o saldo atual da conta.
# ~ Os valores devem ser exibidos usando o formato R$ XXX.XX, exemplo:
# ~ 1500.45 = R$ 1500.45


#  v2.0
# ~ TODO: Recursos com data e hora.
# ~ Estabelecer um limite de 10 transações diárias (manter o limite de saques).
# ~ Se o usuário tentar fazer uma transação após atingir o limite, deve ser
# ~ informado que ele excedeu o número de transações permitidas para aquele dia.
# ~ Mostrar no extrato a data e hora de todas as transações.

MENU = """
|''''''''''''''''''''''''''''''''''''|
| [1] DEPOSITAR                      |
| [2] SACAR                          |
| [3] EXTRATO                        |
| [0] SAIR                           |
|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,|
"""

LIMITE_SAQUE_DIARIO = 3
LIMITE_SAQUE = 500.00
LIMITE_TRANSACOES_DIARIAS = 10

saldo = 0.0
qtde_saque_ao_dia = 0
qtde_transacoes_diaria = 0
extrato = "Extrato:\n"

while True:
    data_atual = datetime.now()

    print(MENU)
    escolha = input("Digite uma das opções: ")
    print("-------------------------")
    if escolha not in ["0", "1", "2", "3"]:
        print("OPÇÃO NÃO ENCONTRADA. TENTE NOVAMENTE.")
        continue

    if escolha in ["1", "2"]:
        qtde_transacoes_diaria += 1
        if qtde_transacoes_diaria > LIMITE_TRANSACOES_DIARIAS:
            print("VOCÊ ATINGIU O LIMITE DE TRANSAÇÕES PERMITIDAS AO DIA.")
            continue

    if escolha == "1":
        try:
            deposito = float(input("Valor a ser depositado: "))
        except ValueError:
            print("VALOR INVÁLIDO.")
            continue

        if deposito <= 0:
            print("NÃO É POSSÍVEL DEPOSITAR VALORES NEGATIVOS.")
            continue

        saldo += deposito
        extrato += f"\n   Depositado   ->    R$ {deposito:+5,.2f}         [{
            data_atual.strftime('%d-%m-%y %H:%M')
        }]"
        continue

    if escolha == "2":
        if qtde_saque_ao_dia >= LIMITE_SAQUE_DIARIO:
            print("NÚMERO DE SAQUES DIÁRIOS0 EXCEDIDO.")
            continue

        try:
            saque = float(input("Digite quanto deseja sacar: "))
        except ValueError:
            print("VALOR INVÁLIDO.")
            continue

        if saque > LIMITE_SAQUE:
            print("LIMITE POR SAQUE EXCEDIDO. MAX: R$ 500.")
            continue

        if saque <= 0:
            print("NÃO É POSSÍVEL SACAR VALORES NEGATIVOS.")
            continue

        if saque > saldo:
            print("SALDO INSUFICIENTE.")
            continue

        saldo -= saque
        extrato += f"\n   Saque        ->    R$ {saque:+5,.2f}         [{
            data_atual.strftime('%d-%m-%y %H:%M')
        }]"
        qtde_saque_ao_dia += 1
        continue

    if escolha == "3":
        str_saldo_atual = f"\n   Saldo atual:       R$ {saldo:+5,.2f}         [{
            data_atual.strftime('%d-%m-%y %H:%M')
        }]"
        print(extrato)
        print(str_saldo_atual)
        continue

    if escolha == "0":
        print("FECHANDO APLICATIVO BANCÁRIO...")
        break

# info = {data_atual.strftime("%d-%m-%y"): qtde_transacoes_diaria}
