import pandas as pd
import requests

API_KEY = 'replace'
sp_list = ['APO', 'LII', 'WDAY', 'TPL', 'DELL', 'ERIE', 'PLTR', 'SW', 'CRWD', 'GDDY', 'KKR', 'VST', 'GEV', 'SOLV', 'DECK', 'SMCI', 'BLDR', 'JBL', 'UBER', 'HUBB', 'LULU', 'VLTO', 'ABNB', 'BX', 'KVUE', 'PANW', 'AXON', 'FICO', 'BG', 'PODD', 'GEHC', 'STLD', 'FSLR', 'ACGL', 'TRGP', 'EQT', 'PCG', 'CSGP', 'INVH', 'KDP', 'ON', 'VICI', 'WBD', 'CPT', 'MOH', 'NDSN', 'CEG', 'FDS', 'EPAM', 'BRO', 'DAY', 'MTCH', 'TECH', 'MRNA', 'CRL', 'PTC', 'CZR', 'GNRC', 'NXPI', 'MPWR', 'TRMB', 'ENPH', 'TSLA', 'POOL', 'TER', 'TDY', 'TYL', 'WST', 'DPZ', 'DXCM', 'CARR', 'OTIS', 'IR', 'PAYC', 'LYV', 'STE', 'ZBRA', 'ODFL', 'WRB', 'NOW', 'LVS', 'NVR', 'CDW', 'IEX', 'LDOS', 'TROW', 'TMUS', 'MKTX', 'AMCR', 'CTVA', 'DD', 'DOW', 'FOX', 'FOXA', 'WAB', 'ATO', 'TFX', 'CE', 'FANG', 'LW', 'JKHY', 'KEYS', 'FTNT', 'ROL', 'ANET', 'CPRT', 'CPAY', 'BR', 'EVRG', 'MSCI', 'TTWO', 'HII', 'NCLH', 'CDNS', 'SBAC', 'IQV', 'AOS', 'MGM', 'PKG', 'RMD', 'BKR', 'ALGN', 'ANSS', 'EG', 'HLT', 'IT', 'AMD', 'ARE', 'RJF', 'SRE', 'SNPS', 'REG', 'CBOE', 'INCY', 'IDXX', 'MAA', 'D', 'HWM', 'COO', 'CHTR', 'MTD', 'ALB', 'FTV', 'LNT', 'TDG', 'AJG', 'LKQ', 'DLR', 'GPN', 'ULTA', 'CNC', 'HOLX', 'UDR', 'AWK', 'FRT', 'CFG', 'EXR', 'WTW', 'CHD', 'SYF', 'HPE', 'VRSK', 'NWS', 'UAL', 'PYPL', 'KHC', 'JBHT', 'O', 'EQIX', 'HSIC', 'SWKS', 'HCA', 'RCL', 'UHS', 'URI', 'MLM', 'AVGO', 'GOOGL', 'ESS', 'TSCO', 'META', 'MHK', 'ALLE', 'AME', 'VRTX', 'DAL', 'NWSA', 'ZTS', 'GM', 'REGN', 'ABBV', 'APTV', 'GRMN', 'HUM', 'DG', 'MDLZ', 'PNR', 'LYB', 'STX', 'LRCX', 'MNST', 'KMI', 'PSX', 'CCI', 'BWA', 'DLTR', 'XYL', 'TEL', 'MOS', 'ACN', 'FCX', 'MPC', 'CMG', 'BLK', 'EW', 'FFIV', 'NFLX', 'TT', 'JCI', 'CB', 'KMX', 'OKE', 'BRK-B', 'NRG', 'ROP', 'ROST', 'V', 'BKNG', 'FMC', 'ES', 'PWR', 'WDC', 'ORLY', 'HRL', 'VTR', 'WELL', 'IRM', 'RSG', 'WYNN', 'SJM', 'WEC', 'NDAQ', 'APH', 'LHX', 'CRM', 'FAST', 'CF', 'IVZ', 'DVA', 'MA', 'CTRA', 'ISRG', 'DOC', 'PM', 'AMT', 'J', 'EXPD', 'EXPE', 'ICE', 'MCHP', 'AKAM', 'DFS', 'AIZ', 'HST', 'CHRW', 'RL', 'AVB', 'CTSH', 'CBRE', 'FIS', 'CME', 'JNPR', 'KIM', 'BXP', 'GOOG', 'VRSN', 'EL', 'AMZN', 'LEN', 'AMP', 'PSA', 'TSN', 'STZ', 'DHI', 'LH', 'TPR', 'TMO', 'GILD', 'VTRS', 'MTB', 'BIIB', 'PLD', 'GEN', 'MKC', 'STT', 'VLO', 'DGX', 'CMCSA', 'TRV', 'ELV', 'EA', 'EBAY', 'GS', 'PFG', 'PRU', 'UPS', 'SPG', 'WAT', 'EQR', 'NVDA', 'PPL', 'COR', 'ZBH', 'FI', 'TXN', 'CTAS', 'SYK', 'MET', 'INTU', 'EOG', 'NI', 'DVN', 'SBUX', 'A', 'ROK', 'USB', 'ADI', 'PNW', 'QCOM', 'VMC', 'BBY', 'NTAP', 'AFL', 'MCK', 'CCL', 'DHR', 'AES', 'PAYX', 'WM', 'RF', 'COF', 'MCO', 'MAR', 'BEN', 'NTRS', 'OMC', 'CINF', 'TFC', 'FE', 'YUM', 'KLAC', 'HBAN', 'PGR', 'APA', 'EFX', 'SCHW', 'CAH', 'ADBE', 'AZO', 'AON', 'FITB', 'ALL', 'DRI', 'L', 'BK', 'AMAT', 'GLW', 'BSX', 'PARA', 'MU', 'LUV', 'UNH', 'MSFT', 'KEY', 'EMN', 'CSCO', 'COST', 'MS', 'IPG', 'LIN', 'AMGN', 'AEE', 'ADSK', 'K', 'ORCL', 'GL', 'ECL', 'NKE', 'C', 'PNC', 'HD', 'AVY', 'MMC', 'SYY', 'MDT', 'ITW', 'PH', 'DOV', 'TJX', 'CNP', 'RVTY', 'APD', 'NUE', 'BALL', 'HAS', 'HES', 'PHM', 'LOW', 'T', 'VZ', 'CAG', 'AAPL', 'BF-B', 'SNA', 'SWK', 'WMT', 'GWW', 'MAS', 'ADP', 'FDX', 'PCAR', 'AIG', 'WBA', 'WY', 'TXT', 'INTC', 'TGT', 'AXP', 'BAC', 'CI', 'DIS', 'DUK', 'NEE', 'TAP', 'WFC', 'IFF', 'JPM', 'WMB', 'HPQ', 'GPC', 'JNJ', 'BAX', 'BDX', 'LLY', 'MCD', 'NEM', 'CLX', 'CMI', 'EMR', 'SHW', 'ABT', 'ADM', 'AEP', 'BA', 'BMY', 'CAT', 'CL', 'CMS', 'COP', 'CPB', 'CSX', 'CVS', 'CVX', 'DE', 'DTE', 'ED', 'EIX', 'ETN', 'ETR', 'EXC', 'F', 'GD', 'GE', 'GIS', 'HAL', 'HIG', 'HON', 'HSY', 'IBM', 'IP', 'KMB', 'KO', 'KR', 'LMT', 'MMM', 'MO', 'MRK', 'MSI', 'NOC', 'NSC', 'OXY', 'PEG', 'PEP', 'PFE', 'PG', 'PPG', 'RTX', 'SLB', 'SO', 'SPGI', 'UNP', 'XEL', 'XOM']

def get_stock_data(ticker, start_date, end_date):
    """Returns daily stock information"""
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date}&to={end_date}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["historical"] if "historical" in data else None

def get_balance_sheet(symbol, period='quarterly'):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period={period}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def get_ratios(symbol, period='quarterly'):
    url = f"https://financialmodelingprep.com/api/v3/ratios/{symbol}?period={period}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def get_next_available(index, price_df): # reports come out on Saturday, but there is no market info for Saturday. Align report with Monday price data.
    count = 0
    while True:
        count+=1
        index = index + pd.Timedelta(days=1)
        if index in price_df.index:
            return price_df.loc[[index]]
        elif count > 30: # raise error if function fails to find price data
            raise Exception('Failed to fetch price data')
        
def get_df(symbol, start_date, end_date):
    # Get data from APIs
    price = get_stock_data(symbol, start_date, end_date)
    balance = get_balance_sheet(symbol, period='quarterly')
    ratios = get_ratios(symbol)

    # Convert to dataframes
    price_df = pd.DataFrame(price)
    balance_df = pd.DataFrame(balance)
    ratios_df = pd.DataFrame(ratios)

    # Convert dates and set indices
    price_df['date'] = pd.to_datetime(price_df['date'])
    price_df.set_index('date', inplace=True)

    balance_df['date'] = pd.to_datetime(balance_df['date'])
    balance_df.set_index('date', inplace=True)

    ratios_df['date'] = pd.to_datetime(ratios_df['date'])
    ratios_df.set_index('date', inplace=True)

    # Filter by date range
    min_date = max(price_df.index.min(), balance_df.index.min(), ratios_df.index.min())
    max_date = min(price_df.index.max(), balance_df.index.max(), ratios_df.index.max())

    price_df = price_df[(price_df.index >= min_date) & (price_df.index <= max_date)]
    balance_df = balance_df[(balance_df.index >= min_date) & (balance_df.index <= max_date)]
    ratios_df = ratios_df[(ratios_df.index >= min_date) & (ratios_df.index <= max_date)]

    # Build corresponding price and ratio data
    corresponding_price = pd.DataFrame()
    corresponding_ratios = pd.DataFrame()

    for index, row in balance_df.iterrows():
        if index in price_df.index:
            new_row_price = price_df.loc[[index]]
        else:
            new_row_price = get_next_available(index, price_df)
        corresponding_price = pd.concat([corresponding_price, new_row_price])

        if index in ratios_df.index:
            new_row_ratios = ratios_df.loc[[index]]
        else:
            new_row_ratios = get_next_available(index, ratios_df)
        corresponding_ratios = pd.concat([corresponding_ratios, new_row_ratios])

    corresponding_ratios = corresponding_ratios.reset_index(drop=True)
    corresponding_price = corresponding_price.reset_index(drop=True)

    # Combine all data
    new_rows = []
    for (index1, row1), (index2, row2), (index3, row3) in zip(balance_df.iterrows(), corresponding_price.iterrows(), corresponding_ratios.iterrows()):
        newrow = pd.concat([row1, row2, row3])
        new_rows.append(newrow)

    # Create final dataframe
    df = pd.DataFrame([s.reset_index(drop=True) for s in new_rows])
    df.columns = list(balance_df.columns) + list(corresponding_price.columns) + list(corresponding_ratios.columns)
    
    return df
