# Issuance and Redemption process

Issuance and redemption process determine the stablecoin supply. The framework assesses the risk by comparing who the issuer is and how the issuance/redemption is performed. The design of the issuance and redemption process is also closely linked to the stablecoin’s stabilisation mechanism. 

For almost all of the custodial stablecoin, issuance and redemption are controlled by centralised parties. For non-custodial stablecoin, issuance and redemption can be done via the leverage mechanism or the reserve mechanism. For example, DAI can be borrowed (i.e. minted) from the MakerDAO’s MCD vaults, and LUSD can be borrowed from Liquity’s Trove. The leverage component incentivises borrower and lender through interest rate which are set by the protocol governance. Stablecoins can be also minted directly from the reserve component at 1:1ish exchange rate against other assets (other stablecoins for most of the cases). 

In a nutshell, there are three types of issuers that controls the the issuance and redemption process:
- **Trusted entities**. Issuance and redemption are dictated by the centralised party.
- **DAO**. A dynamic set of parties, determined by their asset weight in the form of the protocol’s governance token. Any updates to the issuance and redemption process have to be approved by majority vote
- **Protocol algorithm**. A set of predefined rules that were written in the protocol’s smart contract code. It cannot be changed after the stablecoin is launch

## Issuance and redemption risk metrics 

To evaluate and compare stablecoin issuance and redemption risk, the following risk metrics should be considered:

- **Issuer**: name of the issuer - e.g. Coinbase, Tether, Sky, etc
- **Issuer type**: Type of the issuer
  - Trusted entities
  - DAO
  - Protocol Algorithm
- **Issuer type**: Whether Know-Your-Client process is mandatory for stablecoin issuance and redemption
  - Yes
  - No
- **Issuance mechanism**: How stablecoin is issued
- **Issuance mechanism**: How can user redeem stablecoins

## Issuance and Redemption process comparison example
![alt text](https://github.com/tamamatammy/sraf/blob/main/research/images/issuance_risk_example.jpg)

