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

## Stability Mechanism Assessment Example
The follwing table shows a high-level stability mechanism analysis of USDC, USDT, DAI and LUSD 
![alt text](https://github.com/tamamatammy/sraf/blob/main/research/images/stability_mechanism_example.jpg)
