import requests
import datetime
import os

siglas_moedas = {
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

def converter_reais_para_moeda(valorReais, cotacao, moeda_escolhida):
    try:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar terminal
        valor_em_reais = float(input(f"Digite a quantia em reais que você deseja converter para {moeda_escolhida} ({siglas_moedas[moeda_escolhida]}): "))
        valor_convertido = valor_em_reais / cotacao
        print(f"{valor_em_reais:.2f} reais equivalem a {valor_convertido:.2f} {moeda_escolhida}.")
    except ValueError:
        print("Por favor, insira um valor válido em reais.")
    except Exception as e:
        print(f"Erro: {e}")

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

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar terminal

    print("Escolha a moeda para conversão:")
    for opcao, descricao in moedas_disponiveis.items():
        if opcao != '0':
            print(f"{opcao}: {descricao} ({siglas_moedas[descricao]})")
        else:
            print(f"{opcao}: {descricao}")

    escolha = input("Digite o número da opção desejada: ")

    if escolha in moedas_disponiveis:
        if escolha == '0':
            return None
        else:
            return moedas_disponiveis[escolha]
    else:
        print("Opção inválida. Escolha uma opção válida.")
        return escolher_moeda()

def calcular_juros():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar terminal
        montante = float(input("Digite o montante do empréstimo: "))
        tempo_meses = int(input("Digite o tempo em meses: "))
        taxa_mensal = float(input("Digite a taxa de juros ao mês (em porcentagem): ")) / 100

        montante_final = montante * (1 + taxa_mensal) ** tempo_meses

        print(f"\nMontante final a ser pago: {montante_final:.2f}")
    except ValueError:
        print("Por favor, insira valores válidos.")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar terminal
        print("\nBem-vindo ao Finance!")
        print("Escolha uma opção:")
        print("1. Converter reais para moeda estrangeira")
        print("2. Calculadora de Juros")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            moeda_escolhida = escolher_moeda()
            if moeda_escolhida is not None:
                cotacao_atual = obter_cotacao(moeda_escolhida)
                converter_reais_para_moeda(0, cotacao_atual, moeda_escolhida)

        elif opcao == '2':
            calcular_juros()

        elif opcao == '3':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")

        if opcao in ['1', '2']:
            input("Pressione Enter para continuar...")  # Espera por um input para continuar

if __name__ == "__main__":
    main()
