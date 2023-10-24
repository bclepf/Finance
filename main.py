import requests
import datetime
import os


class Cor:
    VERDE = '\033[92m'
    RESET = '\033[0m'


SIGLAS_MOEDAS = {
    'DKK': 'Coroa Dinamarquesa',
    'NOK': 'Coroa Norueguesa',
    'SEK': 'Coroa Sueca',
    'USD': 'Dólar Americano',
    'AUD': 'Dólar Australiano',
    'CAD': 'Dólar Canadense',
    'EUR': 'Euro',
    'CHF': 'Franco Suíço',
    'JPY': 'Iene',
    'GBP': 'Libra Esterlina'
}


def obter_cotacao(moeda):
    current_time = datetime.datetime.now()
    current_date_str = current_time.strftime("%m-%d-%Y")

    api_url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='{moeda}'&@dataInicial='10-05-2023'&@dataFinalCotacao='{current_date_str}'&$top=100&$format=json&$select=cotacaoCompra"

    response = requests.get(api_url)
    response.raise_for_status()

    json_data = response.json()

    first_cotacao_compra = json_data['value'][0]['cotacaoCompra']

    return first_cotacao_compra


def converter_reais_para_moeda(valor_reais, cotacao, moeda_escolhida):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n{'=' * 80}")
        print(f"{'Calculadora de Conversão de Moeda':^80}")
        print(f"{'=' * 80}\n")

        valor_em_reais = float(input(
            f"Digite a quantia em reais que você deseja converter para {moeda_escolhida} ({SIGLAS_MOEDAS[moeda_escolhida]}): "))
        valor_convertido = valor_em_reais / cotacao

        print(f"\n{'=' * 80}")
        print("Resultado da Conversão:")
        print(f"Valor em Reais: {valor_em_reais:.2f} BRL")
        print(f"Valor Convertido: {valor_convertido:.2f} {moeda_escolhida}")
        print(f"{'=' * 80}\n")

    except ValueError:
        print(f"{Cor.VERDE}Erro:{Cor.RESET} Por favor, insira um valor válido em reais.")
    except Exception as e:
        print(f"{Cor.VERDE}Erro:{Cor.RESET} {e}")


def escolher_moeda():
    moedas_disponiveis = {
        '0': 'Retornar ao menu principal',
        '1': 'DKK',
        '2': 'NOK',
        '3': 'SEK',
        '4': 'USD',
        '5': 'AUD',
        '6': 'CAD',
        '7': 'EUR',
        '8': 'CHF',
        '9': 'JPY',
        '10': 'GBP',
    }

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\n{'=' * 80}")
    print(f"{'Escolha a Moeda para Conversão':^80}")
    print(f"{'=' * 80}\n")

    for opcao, descricao in moedas_disponiveis.items():
        if opcao == '0':
            print(f"{' ' * 1}[{opcao}]: {descricao}")
        else:
            print(f"{' ' * 1}[{opcao}]: {descricao} ({SIGLAS_MOEDAS.get(descricao, 'Desconhecido')})")

    escolha = input("\nDigite o número da opção desejada: ")

    if escolha in moedas_disponiveis:
        return moedas_disponiveis[escolha]
    else:
        print(f"{Cor.VERDE}Opção inválida. Escolha uma opção válida.{Cor.RESET}")
        return escolher_moeda()


def calcular_juros():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n{'=' * 80}")
        print(f"{'Calculadora de Juros':^80}")
        print(f"{'=' * 80}\n")

        montante = float(input("Digite o montante do empréstimo: "))
        tempo_meses = int(input("Digite o tempo em meses: "))
        taxa_mensal = float(input("Digite a taxa de juros ao mês (em porcentagem): ")) / 100

        montante_final = montante * (1 + taxa_mensal) ** tempo_meses

        print(f"\nMontante final a ser pago: {montante_final:.2f}")
        print(f"{'=' * 80}\n")

    except ValueError:
        print(f"{Cor.VERDE}Erro:{Cor.RESET} Por favor, insira valores válidos.")
    except Exception as e:
        print(f"{Cor.VERDE}Erro:{Cor.RESET} {e}")


def investimentos():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{'=' * 80}")
            print(f"{'Investimentos em Contas Digitais':^80}")
            print(f"{'=' * 80}\n")

            print("Escolha o banco:")
            print(f"{' ' * 1}[0]: Voltar ao menu principal")
            print(f"{' ' * 1}[1]: PagBank")
            print(f"{' ' * 1}[2]: Neon")
            print(f"{' ' * 1}[3]: Sofisa Direto")
            print(f"{' ' * 1}[4]: 99Pay")
            print(f"{' ' * 1}[5]: PicPay")
            print(f"{' ' * 1}[6]: Nubank")
            print(f"{' ' * 1}[7]: C6 Bank")

            numero_banco = int(input("\nDigite o número do banco: "))

            informacoes_bancos = {
                1: {"Nome": "PagBank", "Descricao": "106% do CDI em CDB. Pagamento a cada 30 dias.",
                    "Rendimento_Ano": 13.94, "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1139.40},
                2: {"Nome": "Neon",
                    "Descricao": "105% do CDI em CDB. A cada 180 dias, o rendimento aumenta em 1% do CDI, até o máximo de 113% do CDI.",
                    "Rendimento_Ano": 13.80, "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1165.63},
                3: {"Nome": "Sofisa Direto", "Descricao": "110% do CDI em CDB. Liquidez diária.",
                    "Rendimento_Ano": 14.46, "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1144.60},
                4: {"Nome": "99Pay",
                    "Descricao": "Rendimento Automático. Até R$500 rende 220% do CDI; o restante rende 100%.",
                    "Rendimento_Ano": 28.93, "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1210.40},
                5: {"Nome": "PicPay",
                    "Descricao": "Rendimento Automático 102% do CDI. Dinheiro deve estar na conta por 30 dias para receber os ganhos; nos cofrinhos, rende a partir do 1º dia útil.",
                    "Rendimento_Ano": 13.41, "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1134.10},
                6: {"Nome": "Nubank",
                    "Descricao": "Rendimento Automático. Nas caixinhas e conta, 100% do CDI; investido em CDB, chega até 110% do CDI.",
                    "Rendimento_Ano": 13.15, "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1131.50},
                7: {"Nome": "C6 Bank", "Descricao": "104% do CDI em CDB.", "Rendimento_Ano": 13.67,
                    "Investimento_Inicial": 1000, "Valor_Apos_1_Ano": 1136.70}
            }

            if numero_banco == 0:
                break
            elif numero_banco in informacoes_bancos:
                banco_selecionado = informacoes_bancos[numero_banco]
                print(f"\nInformações sobre {banco_selecionado['Nome']}:")
                print(f"{'Descrição:':<15} {banco_selecionado['Descricao']}")
                print(f"{'Rendimento ao ano:':<15} {banco_selecionado['Rendimento_Ano']:.2f}%")
                print(f"{'Investimento inicial:':<15} R${banco_selecionado['Investimento_Inicial']:.2f}")
                print(f"{'Valor após 1 ano:':<15} R${banco_selecionado['Valor_Apos_1_Ano']:.2f}\n")
            else:
                print("Número de banco inválido. Por favor, escolha um número válido.")

            numero_banco = int(input("Pressione 1 para saber sobre outra conta digital ou 0 para voltar ao menu: "))
            if numero_banco == 0:
                break

    except ValueError:
        print(f"{Cor.VERDE}Erro:{Cor.RESET} Por favor, insira um número válido.")
    except Exception as e:
        print(f"{Cor.VERDE}Erro:{Cor.RESET} {e}")


def sair():
    print("Obrigado por usar o Finance")


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"\n{'=' * 80}")
        print(f"{'Bem-vindo ao Finance!':^80}")
        print(f"{'=' * 80}\n")

        print("Escolha uma opção:")
        print(f"{' ' * 1}[1]: Converter reais para moeda estrangeira{' ' * 15}")
        print(f"{' ' * 1}[2]: Calculadora de Juros{' ' * 38}")
        print(f"{' ' * 1}[3]: Investimentos{' ' * 41}")
        print(f"{' ' * 1}[4]: Sair{' ' * 65}")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            moeda_escolhida = escolher_moeda()
            if moeda_escolhida is not None:
                cotacao_atual = obter_cotacao(moeda_escolhida)
                converter_reais_para_moeda(0, cotacao_atual, moeda_escolhida)

        elif opcao == '2':
            calcular_juros()

        elif opcao == '3':
            investimentos()

        elif opcao == '4':
            sair()
            break

        else:
            print(f"{Cor.VERDE}Opção inválida. Escolha uma opção válida.{Cor.RESET}")

        if opcao in ['1', '2']:
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
