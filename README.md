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

## Structure
- `data/`: Raw and cleaned datasets
- `features/`: Feature generation and preprocessing scripts
- `clustering/`: Clustering models and evaluation
- `analysis/`: Cluster-level and stock-specific analysis notebooks, including position diagnostics and interpretation tools
- `data_collection/`: Tools for scraping and updating data

## Collaborators
- [@parkercarrus](https://github.com/parkercarrus)
- [@maliawalewski](https://github.com/maliawalewski)

