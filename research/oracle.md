# Oracle

Stablecoins rely on oracles to import off-chain information such as price data in fiat currency to the blockchain network. These data are not native to blockchain, therefore the correctness of the imported data is not verifiable on-chain.

The use of oracles involves risks that the data feed sends incorrect data and negatively impacts the stablecoins. This can happen due to:

- Exploit by external attackers who are incentivised to manipulate the data 
- Exploit by parties who have the power to manipulate oracle data - e.g. oracle providers, protocols
- Accidents in the data process involved in importing prices on-chain
- Poor oracle design

## Oracle risk metrics

To evaluate and compare stablecoin oracle risk, the following risk metrics should be considered:

### **Oracle Risk Assessment Framework**  

| **Factor**              | **Description** | **Sample Values** |  
|-------------------------|---------------|------------------|  
| **Oracle Type**        | The design and trust model of the oracle system. | - **Trusted Party** (single entity-controlled oracle) <br> - **Trusted Multisig** (multi-signature-controlled oracle) <br> - **TWAP from DEXs** (time-weighted average price from decentralized exchanges) |  
| **Oracle Provider**    | The external oracle service providers used for price feeds. | - **Chainlink** <br> - **Chronicle** <br> - Other custom oracles |  
| **Oracle Design & Security** | How the oracle operates and the security measures in place to ensure integrity, both on-chain and off-chain. | - **Off-chain reporting (OCR) framework** (e.g., Chainlink’s OCR model) <br> - **Oracle fallback mechanisms** (alternative oracles used in case of failure) <br> - **Security guardrails** on price feeds (e.g., deviation thresholds, update frequency, multi-source validation) |  
