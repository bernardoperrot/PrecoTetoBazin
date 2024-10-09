import yfinance as yf
from datetime import datetime, timedelta

acao = str(input("Digite o Ticker da Stock: "))
div_min = float(input("Dividendos minimos %: "))
acao = acao.upper()

ativo = yf.Ticker(acao)


dividend_info = ativo.dividends

data_atual = datetime.now()

data_um_ano_atras = data_atual - timedelta(days=365)

data_um_ano_atras_formatada = data_um_ano_atras.strftime("%Y-%m-%d")

filtered_dividends = dividend_info[dividend_info.index >= data_um_ano_atras_formatada]
total = 0
count = -1
index = 0

preco = round(ativo.history(period='1d')['Close'].iloc[0], 2)
print('------------------')
print(f'| Ticker: {acao} |')
print('------------------')
for i in filtered_dividends:
    dividend = dividend_info.iloc[count]
    cash_yield = round((dividend/preco)*100, 3)
    data = dividend_info.index[count]
    index = index + 1
    
    data_organizada = data.strftime("%d/%m/%Y")
    print(f'{index} - Dividendo: R$ {dividend}, Data: {data_organizada}, Yield no Preco atual: {cash_yield} %')
    print('--------')
    total = round(total + dividend, 4)
    count = count -1

preco_teto = round(total*(100/div_min), 3)
yield_total = round((total/preco)*100, 3)
margem = round(((preco_teto-preco)/preco)*100, 2)
print('------------------------------------------------------------------------')
print(f'| Dividendos totais nos ultimos 12 meses: $ {total}, Yield: {yield_total} % |')
print('------------------------------------------------------------------------')
print('------------------------')
print(f'| Preco teto: $ {preco_teto} |')
print('------------------------')
print('------------------------')
print(f'| Preco atual: $ {preco} |')
print('------------------------')
print('-----------------------------------')
print(f'| Margem de segurança: {margem} % |')
print('-----------------------------------')
