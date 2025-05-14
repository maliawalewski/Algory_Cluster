# Stock Clustering for Return Forecasting

This project explores the use of unsupervised machine learning to cluster the s&p500 stocks based on financial fundamentals and return behavior. 
The goal is to identify meaningful groupings that can support investment decisions and return forecasting.

## Methods
- **Feature Engineering**: Cleaned and standardized financial ratios and return data
- **Clustering Models**: K-Means Clustering with various distance metrics
- **Dimensionality Reduction**: PCA and t-SNE for visualization
- **Analysis**: Examined return patterns across clusters to evaluate predictive value

## Key Findings
- Certain clusters consistently outperformed others in specific market conditions
- Fundamental signals (e.g. P/E ratio, debt/equity) aligned with cluster groupings
- Useful for building intuition about sector-agnostic return patterns
- Includes stock-specific notebooks (e.g. EL_analysis.ipynb) to explore individual positioning within clusters and support actionable interpretation

## Structure
- `data/`: Raw and cleaned datasets
- `features/`: Feature engineering notebooks for transforming financial metrics into model inputs
- `clustering/`: Core unsupervised ML model (stock_clustering_model.ipynb) used to group stocks by financial and return-based features
- `analysis/`: Stock-specific and quarterly return analysis notebooks (paypal_analysis.ipynb, quarterlyARS.ipynb, etc.)
- `data_collection/`: Scripts for pulling quarterly stock data

## Collaborators
- [@parkercarrus](https://github.com/parkercarrus)
- [@maliawalewski](https://github.com/maliawalewski)

