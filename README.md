# Simple HRP
 ## A basic implementation of Hierarchical Risk Parity (HRP) portfolio optimization.  

Hierarchical Risk Parity (HRP) is a risk-based portfolio optimization algorithm that generates stable and diversified portfolios that helps investors achieve optimal allocation by reducing risk and maximizing returns and is generally more robust to estimation errors in the covariance matrix.

This approach was developed by Marcos López de Prado and is based on the idea of clustering assets by their similarity and then optimizing the weights of the resulting clusters. The algorithm applies graph theory and machine learning to construct portfolios based on the information contained in the covariance matrix. Unlike traditional optimizers, HRP does not require the invertibility of the covariance matrix (i.e., Markowitz. see notes). 

HRP is also quite adaptable. It works well with both large and small portfolios and can be easily adjusted to reflect changing market conditions. And because it is based on quantitative analysis rather than subjective judgments, the method is less prone to human biases and emotions. 

This simplified version of HRP downloads stock data from Yahoo Finance for the 12 stocks listed and ingests them into a Pandas data frame. It then calculates the weights of each asset.

## Additional Considerations and Constraints
- Minimum and maximum weights for each asset or sector constraint.
- Asset correlation clustering before optimization.
- Use a rolling window to update the covariance matrix and weights over time.
- Variations using Ward’s minimum variance method and complete linkage.
- Market capitalization constraints.
- Cardinality constraints (total portfolio assets.)
- Turnover constraints.
- Transaction cost constraints.

## Gotchas
In this unconstrained version of HRP, suggested weights can exceed 100% of your intended allocation. Consider constraining weights by normalizing them.   

    if weights.sum() > 1:  
        weights = weights/weights.sum()
 
## Notes
### Issues with the Markowitz Model
The Markowitz model can result in stability and sensitivity issues as it assumes the underlying covariance matrix is invertible. However, this is often not the case in practice due to estimation errors and other issues, leading to unstable and unreliable portfolio weights.

## Literature Review
[Building Diversified Portfolios that Outperform Out-of-Sample](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678)  
[The Hierarchical Risk Parity Algorithm: An Introduction](https://hudsonthames.org/an-introduction-to-the-hierarchical-risk-parity-algorithm/)  
[A Constrained Hierarchical Risk Parity Algorithm with Cluster-based Capital Allocation](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)  
[Hierarchical Risk Parity - Implementation & Experiments (Part I)](https://gmarti.gitlab.io/qfin/2018/10/02/hierarchical-risk-parity-part-1.html)  
[What is seration?](http://www.atgc-montpellier.fr/permutmatrix/manual/SeriationCorps.htm)  
[Hierarchical Risk Parity Implementation in Rcpp and OpenMP](https://gallery.rcpp.org/articles/hierarchical-risk-parity/)  
[Hierarchical Clustering Portfolio Optimization](https://riskfolio-lib.readthedocs.io/en/latest/hcportfolio.html)  
[Hierarchical Risk Parity with allocation constraints?](https://quant.stackexchange.com/questions/37065/hierarchical-risk-parity-with-allocation-constraints)  
[Python - Hierarchical Risk Parity (PyPortfolioOpt) - rolling windows](https://stackoverflow.com/questions/64668684/python-hierarchical-risk-parity-pyportfolioopt-rolling-windows) 
[Hierarchical Risk Parity on RAPIDS: An ML Approach to Portfolio Allocation](https://developer.nvidia.com/blog/hierarchical-risk-parity-on-rapids-an-ml-approach-to-portfolio-allocation/)  
[Improving the volatility of the optimal weights of the Markowitz model](https://www.tandfonline.com/doi/full/10.1080/1331677X.2021.1981963)  
[Markowitz and inverse covariance matrix](https://stats.stackexchange.com/questions/534035/markowitz-and-inverse-covariance-matrix)  
[Hierarchical Risk Parity (HRP)](https://breakingdownfinance.com/finance-topics/modern-portfolio-theory/hierarchical-risk-parity/)

John E. Putman II 2023





