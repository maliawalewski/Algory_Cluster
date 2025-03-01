import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv("stock_data.csv")
features = [
    "priceEarningsRatio", "priceToSalesRatio", "enterpriseValueMultiple", 
    "priceToFreeCashFlowsRatio", "priceToOperatingCashFlowsRatio"
]
df = df.dropna(subset=features)
# print(df[features].head())

#standardize 
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

# KMeans clustering



