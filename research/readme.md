# Stablecoin Risk Assessment Framework

Historically, stablecoin popularity was driven by market metrics like market share and market cap. However, the collapse of Terra in October 2022 served as a wake-up call for the crypto industry—could this disaster have been avoided? The answer is yes, but only by acknowledging and managing the inherent risks associated with stablecoins.

In the first part, we analyse the key challenges for stablecoin risk assessment, including a review of existing approaches and case studies of two major depeg events: the collapse of Terra and the temporary depeg of USDC.

- [Defining Stablecoin Risk](https://github.com/tamamatammy/sraf/blob/main/research/defining_stablecoin_risk.md)
- [Issue with Existing Risk Assessment Approach](https://github.com/tamamatammy/sraf/blob/main/research/issues.md)

The second section introduces the Stablecoin Risk Assessment Framework (SRAF) and explains how it can effectively analyse and evaluate stablecoin. Stablecoins can generally be classified into two types: **custodial stablecoins** and **non-custodial stablecoins**.

- **Custodial Stablecoins**. These stablecoins have their reserves, issuance, redemption, and governance managed by one or more centralised entities. Users must rely on these parties to verify the reserve balances that back the stablecoin.

- **Non-Custodial Stablecoins**. Stablecoins’ issuance and redemption are managed by smart contracts, with reserve or proof of reserve (e.g. tokentised RWA) held on-chain. Governance decisions - such as changes to reserve assets, collateral ratios, or token minting and burning mechanism - are made by DAOs or algorithms, or both. Non custodial stablecoins depend heavily on smart contracts, which tend to be far more complex than those used by custodial stablecoins

At a high level, stablecoins within the same type group tend to share similar risk profiles. For instance, custodial stablecoins are more exposed to counterparty risk, as their reserves are managed by trusted entities. On the other hand, non-custodial stablecoins, which rely on complex smart contracts, expose users to higher smart contract risk.

The framework breaks down the stablecoin risk assessment into several categories, where stablecoins that have been assigned with the same value are exposed to similar types of risks. Given the complexity of stablecoin design and the current limitations of a fully data-driven approach, SRAF employs a hybrid method, combining both quantitative and qualitative assessments. Rather than providing a single overall risk score, the framework enables users to gain a deeper understanding of the various risks involved and the potential negative impacts associated with each type of risk.

The following are the risk categories and the recommended metrics for assessing each category:
  - [Asset Backing](https://github.com/tamamatammy/sraf/blob/main/research/asset_backing_risk.md)
  - [Stability Mechanism and Historical Stability Performance](https://github.com/tamamatammy/sraf/blob/main/research/stability_risk.md)
  - [Issuance and Redemption process](https://github.com/tamamatammy/sraf/blob/main/research/issuance_redemption.md)
  - [Liquidity](https://github.com/tamamatammy/sraf/blob/main/research/liquidity.md)
  - [Governance](https://github.com/tamamatammy/sraf/blob/main/research/governance.md)
  - [Smartcontract](https://github.com/tamamatammy/sraf/blob/main/research/smart_contract.md)
  - [Oracle](https://github.com/tamamatammy/sraf/blob/main/research/oracle.md)
  - [Regulatory Risk](https://github.com/tamamatammy/sraf/blob/main/research/regulatory_risk.md)

In the third section, we introduce a new stablecoin risk assessment framework that evaluates risk across multiple dimensions and highlights the need for an overall stablecoin rating.

- [Current challenge of having a single rating](https://github.com/tamamatammy/sraf/blob/main/research/single_rating_challenge.md)


---------------
Open items
- get reviewers to finish review
- Promotion
  - X tweet 
  - blogpost for medium, mirror.xyz or linkedin
