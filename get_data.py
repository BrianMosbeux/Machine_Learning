import datetime as dt
import os
import pandas as pd 
import yfinance as yf
from yfinance.utils import auto_adjust


def download_stock_as_csv(ticker, output_folder, start=dt.datetime(2000, 1, 1), end=dt.datetime.today()):
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	df = yf.download(ticker, start, end)
	df.columns = [c[0] for c in df.columns]
	print(df)
	df.to_csv('{}/{}.csv'.format(output_folder, ticker))

download_stock_as_csv('GOOGL', 'stock_data')