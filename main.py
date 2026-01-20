from sem_flores import Musgo, Samambaia
from com_flores import Gimnosperma, Angiosperma


def exibir_menu():
    print("\n==============================")
    print(" SISTEMA DE CLASSIFICAÇÃO DE PLANTAS ")
    print(" ONG Ambiental - Brasil ")
    print("==============================")
    print("1 - Identificar uma planta")
    print("0 - Sair")


def identificar_planta():
    print("\n--- Identificação da Planta ---")
    nome = input("Digite o nome da planta: ")

    flores = input("A planta possui flores? (sim/nao): ").lower()

    if flores == "nao":
        vasos = input("Possui vasos condutores (raiz, caule e folhas)? (sim/nao): ").lower()

        if vasos == "nao":
            planta = Musgo(nome)
        else:
            planta = Samambaia(nome)

    elif flores == "sim":
        frutos = input("A planta possui frutos? (sim/nao): ").lower()

        if frutos == "sim":
            tipo = input("É Monocotiledônea ou Dicotiledônea? ")
            planta = Angiosperma(nome, tipo)
        else:
            planta = Gimnosperma(nome)
    else:
        print("Resposta inválida. Tente novamente.")
        return

    print("\n>>> Resultado da Classificação <<<")
    planta.exibir_info()


# PROGRAMA PRINCIPAL
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        identificar_planta()
    elif opcao == "0":
        print("\nEncerrando o sistema. Obrigado!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
