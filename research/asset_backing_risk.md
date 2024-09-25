# Asset Backing Risk 
This risk arises when the market value of assets backing a stablecoin drops below the pegged value (for stablecoins referenced to an asset/index) or becomes too volatile for the stablecoin to maintain its stability (for those not referenced to any asset/index). Such situations increase the likelihood of the stablecoin depegging or becoming overly volatile, potentially leading to the complete failure of the protocol.

These assets, also referred to as collateral, are categorised as **exogenous assets**, **endogenous assets**, and **implicit assets** based on how their value is derived.

- **Exogenous assets**. These are assets that exist independently of the stablecoin and have broader use cases beyond backing the stablecoin’s value. The amount of these assets used to back a stablecoin is typically small relative to their use in other markets. Examples include the US dollar for USDC and USDT, USDC for DAI, and ETH for LUSD.

- **Endogenous asset**. These assets are created specifically to back the stablecoin and have limited use outside of the project. Their value is directly tied to the demand for the stablecoin they support—when demand for the stablecoin rises, so does the value of the endogenous asset. However, during a crisis of confidence, selling pressure on the stablecoin can cause both the stablecoin and its endogenous asset to enter a "death spiral," with both values plummeting. Notable examples include LUNA/UST and TITAN/IRON.

- **Implicit asset**. Some stablecoins do not have explicit assets as collateral, instead relying on market mechanisms—such as speculators and incentive systems—to dynamically adjust supply and stabilise prices. While similar to endogenous assets, implicit assets are not tokenized and thus do not have an observable market price. An example of this model is Basis, a project that shut down in 2018.

It’s common for stablecoin projects to use a mix of exogenous and endogenous assets as collateral.

The table below provides examples of the asset types chosen by various stablecoins to back their value, including projects like Terra’s UST, Iron, Basis, and NuBit, all of which have since failed.

![alt text](https://github.com/tamamatammy/sraf/blob/main/research/images/asset_type_example.jpg)

