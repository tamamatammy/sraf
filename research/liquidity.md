# Stablecoin liquidity

Stablecoin liquidity risk refers to that a stablecoin protocol cannot maintain enough available liquidity, causing wild price swings in the secondary market. Stablecoin liquidity exists both onchain and offchain. For majority of the cases, user buy and sell stablecoins at:

- **centralised exchanges (CEX)**. CEX  like Coinbase and Binance relies on market makers to provide stablecoin liquidity, based on the order book model. 

- **decentralised exchanges (DEX)**. DEX, or AMM (Automatic Market Makers), uses liquidity pools to facilitate crypto asset trading. They rely on liquidity providers to supply tokens to the pool for trading purposes and the price of the token is determined by the AMM’s own pricing strategy. 

- **stablecoin reserve component** which allow users to swap stablecoin at a 1:1ish exchange rate to other assets depending on the reserve composition. 


In the crypto market, liquidity is fragmented betweent different platforms, exits both onchain and offchain. It is a real challenge, especially to non-expert crypto users, to fully understand the liquidity risk associated with the stablecoin. The framework proposes some general guidelines over how stablecoin liquidity can be measured based on where the liquidity takes place, but framework users should also be aware that the actual calculations are different depending on individual stablecoin design.

**To compare liquidity at CEX:**

Crypto trading on centralized exchanges (CEX) follows the order book model, much like securities trading in traditional finance (TradFi). This allows us to apply standard market liquidity metrics to compare stablecoin liquidity on CEXs.

- **Bid-Ask Spread**
The difference between the highest price a buyer is willing to pay (bid) and the lowest price a seller is willing to accept (ask). This spread represents the implicit cost of executing an immediate trade. A narrower spread indicates higher liquidity, while a wider spread suggests lower liquidity and higher transaction costs.

- **Market Depth**
While the bid-ask spread provides a quick snapshot of trading costs, market depth offers a broader view of liquidity. It measures the volume of buy and sell orders across different price levels, reflecting how well the market can absorb large trades without significant price impact. A deep market has a high volume of orders on both sides, ensuring smoother execution for larger trades.

![alt_text](https://github.com/tamamatammy/sraf/blob/main/research/images/market_depth.jpg)
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ Figure: A order book view of market depth for the BTC-USD pair

As all data are offchain, users have to rely on the exchange’s data under the assumptions that it covers all the data required for liquidity calculation and its data quality can be trusted. Traditional market liquidity risk metrics like market depth can be used to measure stablecoin liquidity at CEX.



**To compare liquidity at DEX:**
