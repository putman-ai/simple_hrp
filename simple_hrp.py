import yfinance as yf
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist

# Stocks to download
tickers = [ 'PKI', 'NWE', 'TT', 'AMSF', 'COLM', 'AEP', 'XOM', 'RNR', 'PEG', 'KO', 'LULU', 'ETR' ]
market_cap = np.array([ 3.4, 37.2, 0.97, 4.5, 42.7, 413, 9.6, 29.8, 258, 42, 20.7 ]) # in billions

# Normalize the market caps
market_cap = market_cap / sum(market_cap)

try:
    # Ingest data
    data = yf.download(tickers, start="2019-05-01", end="2023-05-31")['Adj Close']
    data = data.dropna(axis=1)

    # Calculate the distance matrix between assets
    corr_matrix = data.corr()
    dist_matrix = np.sqrt((1 - corr_matrix.copy()) / 2)

    # Cluster the assets based on their distance
    linkage_matrix = linkage(pdist(dist_matrix), method='single')
    clusters = fcluster(linkage_matrix, 3, criterion='maxclust')

    # Calculate the inverse variance of each cluster
    inv_variances = {i: 1 / np.var(data.iloc[:, clusters == i].mean(axis=1)) for i in np.unique(clusters)}

    # Calculate weight of each asset based on its inverse variance and cluster membership
    weights = pd.Series(index=data.columns)
    for i in np.unique(clusters):
        weights[clusters == i] = inv_variances[i] / np.sum(list(inv_variances.values()))

    # adjust weights for market capitalization
    weights = weights * market_cap

    # constrain weights to 1
    weights = weights/weights.sum()

    # Redistribute any leftover weight due to precision issues
    leftover = 1.0 - weights.sum()
    weights += leftover / len(weights)

    print("Final Portfolio Allocation:")
    print(weights)

except Exception as e:
    print(f"Error occurred: {e}")