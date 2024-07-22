# libraries
import requests
import calendar
import pandas as pd
from datetime import date
from matplotlib import pyplot as plt



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


def check_date():
	return date.today().year, date.today().day

def is_first_of_the_month(function):
	def inner():
		if (check_date()[1] != 1): return
		print('getting csv')
		function()

	return inner

def year_to_date(dataframe):
	# removing dates not in time range
	for x in dataframe.index:
		if int(dataframe.loc[x, 'Date'][0:4]) < check_date()[0]:
			dataframe.drop(x,inplace=True)
	dataframe.reset_index(drop=True,inplace=True)
	

	# changing date to month
	for x in dataframe.index:
		dataframe.loc[x,'Date'] = calendar.month_abbr[int(dataframe.loc[x, 'Date'][5:7])]




@is_first_of_the_month
def get_CPI_csv():
	content = requests.get(f'https://www.econdb.com/widgets/cpi-annual-growth/data/?country=US&format=csv', headers=headers)
	with open('cpi-annual-growth.csv', 'w') as f:
		f.write(content.text)
@is_first_of_the_month
def get_unemployment_csv():
	content = requests.get(f'https://www.econdb.com/widgets/unemployment-rate/data/?country=US&format=csv', headers=headers)
	with open('unemployment-rate.csv', 'w') as f:
		f.write(content.text)
@is_first_of_the_month
def get_gov_bond_rates_csv():
	content = requests.get(f'https://www.econdb.com/widgets/yields/data/?country=US&format=csv', headers=headers)
	with open('government-bond-rates.csv', 'w') as f:
		f.write(content.text)
	



def get_CPI_df():
	get_CPI_csv()
	df = pd.read_csv('cpi-annual-growth.csv')[['Date','ALL']]

	year_to_date(df)

	return df

def get_unemployment_df():
	get_unemployment_csv()
	df = pd.read_csv('unemployment-rate.csv')[['Date', 'URATE']]
	
	year_to_date(df)

	return df

def get_gov_bond_rates_df():
	get_gov_bond_rates_csv()
	df = pd.read_csv('government-bond-rates.csv')[['Date','M3YD','Y10YD']]
	
	year_to_date(df)

	return df






def get_cpi_graph():
	cpi_data = get_CPI_df()

	#plt.rcParams['figure.figsize'] = [19.2, 10.8]
	#plt.rcParams['figure.labelsize'] = 20
	#plt.rcParams['axes.titlesize'] = 22


	#plt.set_title("CPI Data")
	plt.plot(cpi_data['Date'], cpi_data['ALL'])
	plt.fill_between(cpi_data['Date'], 0, cpi_data['ALL'], alpha=0.5)

	plt.savefig('.\\webpage\\graphs\\cpi-graph.png', format='png')
	plt.clf()

def get_unemployment_graph():
	data = get_unemployment_df()

	#plt.rcParams['figure.figsize'] = [19.2, 10.8]
	#plt.rcParams['figure.labelsize'] = 20
	#plt.rcParams['axes.titlesize'] = 22


	#plt.set_title("CPI Data")
	plt.plot(data['Date'], data['URATE'])
	plt.fill_between(data['Date'], 0, data['URATE'], alpha=0.5)

	plt.savefig('.\\webpage\\graphs\\unemployment-graph.png', format='png')
	plt.clf()
	
def get_government_bond_rate_graph():
	data = get_gov_bond_rates_df()

	#plt.rcParams['figure.figsize'] = [19.2, 10.8]
	#plt.rcParams['figure.labelsize'] = 20
	#plt.rcParams['axes.titlesize'] = 22


	#plt.set_title("CPI Data")
	plt.plot(data['Date'],data['M3YD'])
	plt.plot(data['Date'],data['Y10YD'])
	plt.fill_between(data['Date'], 0, data['M3YD'], alpha=0.5)
	plt.fill_between(data['Date'], 0, data['Y10YD'], alpha=0.5)

	plt.savefig('.\\webpage\\graphs\\gov-bond-rate-graph.png', format='png')
	plt.clf()


def get_graphs():
	get_cpi_graph()
	get_unemployment_graph()
	get_government_bond_rate_graph()



if __name__ == '__main__':
	get_graphs()


	
