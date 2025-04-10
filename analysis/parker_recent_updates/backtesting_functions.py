import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def download_sp500_data(start_date, end_date):
    """Return S&P 500 CLOSE Over Specificed Interval"""

    df = pd.read_csv('../../data/processed/quarterly/cluster_labels/2022_Q4_clusters.csv')
    tickers = df['symbol'].unique().tolist()

    start_date = '2021-04-01'
    end_date = '2024-12-31'

    prices = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    return prices

# corresponding date = 2 weeks after quarter end. quarter metrics will have become available 
quarters_dict = {
    "2021_Q1": "2021-04-21",
    "2021_Q2": "2021-07-21",
    "2021_Q3": "2021-10-21",
    "2021_Q4": "2022-01-21",
    "2022_Q1": "2022-04-21",
    "2022_Q2": "2022-07-21",
    "2022_Q3": "2022-10-21",
    "2022_Q4": "2023-01-21",
    "2023_Q1": "2023-04-21",
    "2023_Q2": "2023-07-21",
    "2023_Q3": "2023-10-21"
}


def returns(price_df):
    """Calculate ratio between start of period 2-week MA and end of period 2-week MA"""
    
    # 1day to 1day returns could be sensitive to market noise, calculate average instead
    start_period = price_df.iloc[0:14]
    end_period = price_df.iloc[-14:-1]

    start_period_avg = start_period.mean()
    end_period_avg = end_period.mean()
    
    returns_df = ((end_period_avg - start_period_avg) / start_period_avg).reset_index()
    returns_df.columns = ['symbol', 'returns']

    return returns_df


def get_validation(price_df, training_quarter):
    """Get returns DataFrame"""
    start_date = quarters_dict[training_quarter]
    end_date = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=365)
    filtered_prices = price_df.loc[(price_df.index > start_date) & (price_df.index <= end_date)]

    returns_df = returns(filtered_prices)

    return returns_df

def get_eval(train_quarter):
    df_train = pd.read_csv(f'../../data/processed/quarterly/cluster_labels/{train_quarter}_clusters.csv')
    df_clustered = df_train[['symbol', 'cluster']].drop_duplicates()
    
    validation_df = get_validation(train_quarter)
    df_eval = df_clustered.merge(validation_df, on='symbol', how='inner')

    return df_eval

def performance(df_eval):
    """Get dataframe of performance"""
    performance_summary = df_eval.groupby('cluster')['returns'].agg(['mean', 'median', 'std', 'count'])
    performance_summary = performance_summary.sort_values(by='mean', ascending=False)

    return performance_summary
