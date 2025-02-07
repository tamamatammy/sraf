# Governance

Governance is the process to manage system parameters and possibly code/methods updates. It aims to manage risk, earn protocol profit, and support protocol growth by managing parameters like interest rate, collateral factors, asset class to be accepted as collateral, maximum supply of stablecoins, the trigger of emergency shutdown, etc. Ideally, governance should be incentivized to manage the protocol well and disincentivized or disallowed from actions that are not aligned with the interests of protocol users (e.g. ranging from rug-pulls to seeking short term profits at the expense of longer term stability).

Stablecoin governance can be grouped into three different categories: 

- **trust-base governance**. All current custodial stablecoin using the trusted base governance where all governance decisions were made offchain and are controlled by centralised parties. Decision turnover solely depends on the centralised party - it can be very fast as it’s dictated by single or few parties, but it can also be slow if those parties are not efficient in decision-making. The governance process takes place offchain and it is not transparent. Stablecoin users are exposed to high centralised risk. 

- **majority vote governance (the DAO).** Decisions are normally made based on votings by the governance token holder. Governance process is transparent to the public as it takes place onchain. It normally takes at least 48 hours for a decision to be made and delivered. Level of decentralisation depends on the distribution of the governance power - in the case that only few parties hold majority of the gov tokens, the decentralisation level will also be low

- **Algorithmic based governance.** The parameters are already set and fixed in the smart contract and nobody can change them. It is fully transparent and the level of decentralisation is high. Although this approach does not have the governance risks like the other, it will be a problem if later bugs are identified in the code.
