# Stablecoin liquidity

Stablecoin liquidity risk refers to that a stablecoin protocol cannot maintain enough available liquidity, causing wild price swings in the secondary market. Stablecoin liquidity exists both onchain and offchain. For majority of the cases, user buy and sell stablecoins at:

- **centralised exchanges (CEX)**. CEX  like Coinbase and Binance relies on market makers to provide stablecoin liquidity, based on the order book model. 

- **decentralised exchanges (DEX)**. DEX, or AMM (Automatic Market Makers), uses liquidity pools to facilitate crypto asset trading. They rely on liquidity providers to supply tokens to the pool for trading purposes and the price of the token is determined by the AMM’s own pricing strategy. 

- **stablecoin reserve component** which allow users to swap stablecoin at a 1:1ish exchange rate to other assets depending on the reserve composition. 


In the crypto market, liquidity is fragmented betweent different platforms, exits both onchain and offchain. It is a real challenge, especially to non-expert crypto users, to fully understand the liquidity risk associated with the stablecoin. The framework proposes some general guidelines over how stablecoin liquidity can be measured based on where the liquidity takes place, but framework users should also be aware that the actual calculations are different depending on individual stablecoin design.

## **Comparing liquidity on CEX**

Crypto trading on centralized exchanges (CEX) follows the order book model, much like securities trading in traditional finance (TradFi). This allows us to apply standard market liquidity metrics to compare stablecoin liquidity on CEXs.

- **Bid-Ask Spread**
The difference between the highest price a buyer is willing to pay (bid) and the lowest price a seller is willing to accept (ask). This spread represents the implicit cost of executing an immediate trade. A narrower spread indicates higher liquidity, while a wider spread suggests lower liquidity and higher transaction costs.

- **Market Depth**
While the bid-ask spread provides a quick snapshot of trading costs, market depth offers a broader view of liquidity. It measures the volume of buy and sell orders across different price levels, reflecting how well the market can absorb large trades without significant price impact. A deep market has a high volume of orders on both sides, ensuring smoother execution for larger trades.

![alt_text](https://github.com/tamamatammy/sraf/blob/main/research/images/market_depth.jpg)
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ Figure: A order book view of market depth for the BTC-USD pair

As all data are offchain, users have to rely on the exchange’s data under the assumptions that it covers all the data required for liquidity calculation and its data quality can be trusted. Traditional market liquidity risk metrics like market depth can be used to measure stablecoin liquidity at CEX.


## **Comparing liquidity on DEX**

Most DEXs use AMMs for trading, where liquidity depends on liquidity pools rather than traditional order books. Measuring liquidity on a DEX requires different approaches than on CEXs. It is very complex and can take years for a team of experts to develop a comprehensive onchain liquidity risk model. However, for non-expert crypto users, the following key quantitative metrics can provide a high-level comparison of stablecoin liquidity on DEXs.


- **Total Value Locked (TVL)**. The total amount of assets locked in a DEX’s liquidity pools. A higher TVL generally suggests deeper liquidity, but it alone does not differentiate liquidity risk across different pools with similar TVL.

- **Slippage**. The difference between the quoted price and the actual execution price due to broader market movements. Lower slippage indicates better liquidity for stablecoin trades.

- **Price Impact**. the difference between the current market price and the final execution price,  directly caused by your own trade. Lower price impact for a given trade size means deeper liquidity.



Different AMM models impact price efficiency and liquidity in distinct ways. Here are the most commonly used AMM pool designs today:

- **Constant Product Pool:** Uses the x * y = k formula, maintaining equal value weighting between assets. Commonly used in Uniswap V2-style pools.
  
- **Weighted Pool:** Allows for non-equal asset weightings (e.g., 80/20, 60/20/20), offering more flexibility than constant product pools.
  
- **Stable Pool:** Designed for assets that trade near parity (e.g., stablecoins), reducing slippage and price impact.
  
- **Concentrated Liquidity Pool:** Allows liquidity providers (LPs) to allocate liquidity within specific price ranges, improving efficiency but requiring active management.



## **Comparing liquidity in stablecoin reserve component**
For stablecoins with a reserve component that allows direct redemption, liquidity can be assessed by measuring the Total Value Locked (TVL) within the reserve. A higher reserve TVL generally indicates stronger redemption capability and peg stability, but additional factors such as withdrawal mechanisms and reserve composition should also be considered.

- **Non-Custodial Stablecoins (e.g. DAI, GYD):** Liquidity can be measured in real time by tracking the TVL within the reserve’s smart contract (e.g., Maker’s Peg Stability Module (PSM)).

- **Custodial Stablecoins (e.g., USDC, USDT):** Reserve size is assessed through audit or attestation reports. However, the reliability of these figures depends on the stablecoin issuer’s transparency and reporting practices. To evaluate data reliability, we can use the "Information Quality" metric from ‘the Asset Backing Risks’ section, which helps assess the credibility of reserve disclosures.






