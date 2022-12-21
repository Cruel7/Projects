import numpy as np
import pandas as pd
import random
import xlsxwriter
import math
import requests
import warnings

from secretz import IEX_CLOUD_API_TOKEN
warnings.simplefilter(action='ignore', category=FutureWarning)
stocks=pd.read_csv("sp_500_stocks.csv")

my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']

final_dataframe = pd.DataFrame(columns = my_columns)
for symbol in stocks['Ticker'][:5]:
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
                                        pd.Series([symbol,
                                                   data['latestPrice'],
                                                   data['marketCap'],
                                                   'N/A']
                                                  index = my_columns),
                                        ignore_index = True)

print(final_dataframe)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []
for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))
    print(symbol_strings[i])

final_dataframe = pd.DataFrame(columns=my_columns)

for symbol_string in symbol_strings[:1]:
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    for symbol in symbol_string.split(','):
        final_dataframe = final_dataframe.append(
            pd.Series([symbol,
                       data[symbol]['quote']['latestPrice'],
                       data[symbol]['quote']['marketCap'],
                       'N/A'],
                      index=my_columns),
            ignore_index=True)

print(final_dataframe)

portfolio_size=1255541.15

position_size=portfolio_size/len(final_dataframe.index)
for i in range(0,len(final_dataframe.index)):
    final_dataframe.loc[i, 'Number Of Shares to Buy'] = math.floor(position_size / final_dataframe['Price'][i])
    print(final_dataframe)


writer = pd.ExcelWriter('recommended_trades.xlsx', engine='xlsxwriter')
final_dataframe.to_excel(writer, sheet_name='Recommended Trades', index = False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = writer.book.add_format(
        {
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

dollar_format = writer.book.add_format(
        {
            'num_format':'$0.00',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

integer_format = writer.book.add_format(
        {
            'num_format':'0',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

column_formats = {
                    'A': ['Ticker', string_format],
                    'B': ['Price', dollar_format],
                    'C': ['Market Capitalization', dollar_format],
                    'D': ['Number of Shares to Buy', integer_format]
                    }

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 20, column_formats[column][1])
    writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], string_format)

writer.save()

mkap=pd.read_csv("recommended_trades.xlsx")
mkaplist=[]
for x in mkap["marketCap"]:
    mkaplist.append(x)