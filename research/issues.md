# Issue with existing risk assessment approach
## 1. Misuse  of market share metrics
Many stablecoin-related decisions are driven by yield and trends, making market share analysis one of the most common methods for assessing performance. Crypto users often rely on metrics such as market cap, circulating supply, user addresses, and total value locked (TVL) to gauge the success of stablecoins. However, this type of analysis falls short when it comes to identifying risks. The crypto industry has learned hard lessons from two significant stablecoin depeg events: [the collapse of Terra](https://github.com/tamamatammy/sraf/blob/main/research/terra_collapse.md) and the [temporary depeg of USDC](https://github.com/tamamatammy/sraf/blob/main/research/usdc_depeg.md)

In the case of UST, it was recognized as the third-largest stablecoin before its crash. Its market cap had reached nearly $18 billion USD by April 2022, and LUNA, the associated token, peaked at $119. However, the crash in May 2022 was caused by a fundamental flaw in UST's design: it was under-collateralized and primarily backed by LUNA, which had circular value and could collapse to zero.

Similarly, when USDC depegged on March 10, 2023, it was the second-largest stablecoin by market cap. Although USDC was fully backed by cash and cash equivalents, the depeg occurred due to the collapse of Silicon Valley Bank (SVB), exposing USDC users to custodian risk, as part of its reserves were held in SVB accounts.

These cases highlight that relying on market share metrics like market cap and circulating supply does little to assess the underlying risks of stablecoins.

## 2.  Overemphasis on downward risk
Most existing stablecoin risk frameworks focus solely on depeg scenarios where the market value of a stablecoin falls below its pegged value. However, stablecoin users can also suffer losses when the price of a stablecoin exceeds its peg. For example, users may face the risk of a short squeeze if they are forced to buy stablecoins at inflated prices to repay debt. Thus, upward price volatility should also be considered in risk assessments, but it often isn't.

## 3. Incomplete risk assessment for different stablecoin types
Many risk frameworks are tailored to specific types of stablecoins, which limits their applicability. Traditional rating agencies like Moody’s, and Fitch Ratings primarily assess fiat-backed stablecoins with off-chain reserve assets. Their frameworks focus heavily on counterparty risks, including reserve custodians, issuance and redemption mechanisms, and centralised governance. While these methods are useful for centralised stablecoins, they are inadequate for assessing risks associated with non-custodial stablecoins, which rely on decentralised or algorithmic mechanisms.

Another common assumption in these frameworks is that stablecoins are pegged to external reference assets like fiat currencies or commodities. However, newer stablecoin designs, such as RAI by Reflexer, are engineered to achieve stability without pegging their value to any external asset. As a result, risk assessments focused solely on price movements around a peg are ineffective for such designs.
