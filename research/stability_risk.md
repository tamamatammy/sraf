# Stability Mechanism
This risk category analyses how stablecoin can fail to achieve stability through analysing its stability mechanism and price stability in the past.

## Stability mechanism analysis
At a very high level, there are two main types of stability mechanisms used in practice today:

- **Reserve-backed mechanism**, where there is an issuance and redemption process against a communal reserve of assets that allow 1 unit pegged asset value (e.g. $1 for USD pegged) worth of assets to be exchanged for one stablecoin and vice versa. This includes custodial stablecoins, where centralised issuers and custodians handle these tasks off-chain (e.g.USDC, USDT) as well as on-chain exchange mechanisms like the Peg Stability Mechanism (i.e. PSM) for DAI.

- **Leverage mechanisms** (also known as Collateralised Debt Position CDP) that allows stablecoin units to be minted by borrowing against overcollateralized positions (e.g. LUSD, RAI, and non-PSM issuance in DAII) or possibly other sorts of leverage instruments (such as perpetual swaps).

It can be extremely challenging to fully understand each stablecoin’s stability mechanism. However, users can understand the risks involved by knowing the high-level design:

- **Asset backing risk associated with the reserved-backed component**
Stablecoin that has the reserve component exposes to the same risk - the risk that value of reserve drops and stablecoins become udnercollateralised. Depending on the types of asset in reserves (e.g. fiat, crypto, or stablecoin) and the way that the stablecoin holds the reserve (e.g. custodial vs non-custodial, on-chain vs off-chain), stablecoin users exposed to different asset backing risks which is covered in the ‘Asset Backing’ section.

- **Short squeeze risk associated with the leverage component**
For stablecoins that only have the leverage component and have not setup negative rate (e.g. LUSD and the original DAI), it may suffer from short squeeze where stablecoin value goes up as collateral value goes down and borrowers want to buy back the stablecoin to deleverage their leverage position, eventually becoming costly to deleverage or to liquidate. Having the reserved-backed component can help to reduce the shortsqueeze risk

- **Liquidation risk associated with the leverage component**
The risk that the value of the collateral declines faster than the liquidation happens, making liquidation harder and more costly to be executed. Advanced liquidation design can be deployed to reduce the liquidation risk - for example, crvUSD uses a new technique called LLAMMA (Lending Liquidating AMM Algorithm) for continuous liquidations.

### Stability Mechanism Assessment Example
The follwing table shows a high-level stability mechanism analysis of USDC, USDT, DAI and LUSD 
![alt text](https://github.com/tamamatammy/sraf/blob/main/research/images/stability_mechanism_example.jpg)

## Historical stability performance
Statistical measures can be used to assess stablecoin’s historical stability performance over time. Many existing empirical studies only focus on stablecoin’s price deviation from its peg value. As stablecoin design continues to evolve, some new designs (e.g. RAI) try to achieve stability without tracking a specific asset (e.g. fiat currency, gold, etc).

The SRAF framework has chosen five risk measures, and each provides a unique way to assess how resilient the stablecoin is under normal and extreme market conditions in the past. The selected risk metrics are:

- Volatility metrics: Price Volatility, Standard Deviation from peg difference
- Expected loss metrics: Value-at-Risk, Tail Value-at-Risk, Maximum Drawdown

The chosen metrics can be used individually or together based on users’ needs. They do not only focus on price fluctuations but also expected losses that may be incurred when holding

### Metrics
**Volatility metric: Price Volatility** 

Price volatility estimates how much the value of stablecoin fluctuates around its mean price over a certain period of time. High volatility may indicate that the price of stablecoin can change dramatically in either direction. 

In this framework, volatility is measured as the standard deviation of stablecoin’s logarithmic returns.


\
$$ Vol_T = \sqrt{(\sum_{i=1}^n (r_i - \bar{r})^2 \over (n+1)} $$

\
where
\
$~~~~$ Vol: $~~~$  Voliatility
\
$~~~~$ T: $~~~~$  Number of periods in the vol
\
$~~~~$ n: $~~~~$  Number of periods in the same period
\
$~~~~$ r: $~~~~$  Logarithmic return $\log{price_{current} \over price_{previous}}$
\
$~~~~$ i: $~~~~$  the $i_th$ period in the sample period

**Volatility metric: standard deviation of peg difference** 

This metric measures how much past stablecoin prices deviated from its pegged value over a certain period of time (e.g. over an hour, over one day or over one week). The calculation is:

\
$$ s.d_{peg diff} = \sqrt{(\sum_{i=1}^n (p_i - peg)^2 \over (n-1)} $$

\
where
\
$~~~~$ $s.d_{peg diff}$: $~~$ Standard deviation of stablecoin price to its pegged value over n periods
\
$~~~~$ peg: $~~~~~~~~~~~~~~~$ Stablecoin peg value - e.g. $1 for stablecoins that are pegged to USD
\
$~~~~$ n: $~~~~~~~~~~~~~~~~~$ Number of periods in the same period
\
$~~~~$ p_i: $~~~~~~~~~~~~~~~$ Stablecoin price at period i 
\
$~~~~$ i: $~~~~~~~~~~~~~~~~~$ the $i_th$ period in the sample period


**Expected loss metric: Value-at-Risk**
Value-at-Risk (VaR) estimates the possible losses incurred by holding a stablecoin for a certain period of time (e.g. one hour, one day or one week), with a given probability. For example, a 95% hourly VaR of 0.2 indicates there is a 95% chance that the underlying stablecoin will not lose more than 20% of its value over the next hour.

There are three different methods of calculating VaR - Variance-Covariance, Historical Simulation, and Monte Carlo simulation. Each modelling method comes with certain data assumptions and gives different VaR calculations. For example, the Variance-Covariance method is a parametric method that assumes the price returns follow a normal distribution and the Historical Simulation method is a non-parametric method that relies solely on the historical data. It is up to the framework users to select one or a hybrid approach to model VaR for stablecoins.

[var modelling in detail]

**Expected loss metric: Tail Value-at-Risk**
Tail VaR is another metric that can be used to measure the potential losses of holding a stablecoin over a certain period of time. It is very similar to VaR, but unlike VaR which only determines risk at a given confidence level,  TVaR considers all losses that are worse than the given VaR level. It is calculated as the mean of all losses that are worse than or equal to VaR 

[TVaR modelling in detail].

**Expected loss metric: Maximum drawdown**
Maximum drawdown (MDD) is an indicator of downside risk that measures the stablecoin’s largest price drop from peak to trough. It indicates the maximum loss that can be insured by holding the given stablecoin over a certain period of time (e.g. can be over one-month, one-quarter, or even one-year).

\
$$ MDD_{T} = p_{max} - p_{min} $$

\
where
\
$~~~~$ $MDD_{T}$: $~~~$ Maximum drawdown over period T
\
$~~~~$ $p_{max}$: $~~~~$ Highest stablecoin price in period T
\
$~~~~$ $p_{min}$: $~~~~$ Lowest stablecoin price in period T
