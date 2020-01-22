truffle unbox pet-shop

The default Truffle directory structure contains the following:

contracts/: Contains the Solidity source files for our smart contracts. There is an important contract in here called Migrations.sol, which we'll talk about later.

migrations/: Truffle uses a migration system to handle smart contract deployments. A migration is an additional special smart contract that keeps track of changes.

test/: Contains both JavaScript and Solidity tests for our smart contracts
truffle-config.js: Truffle configuration file

The pet-shop Truffle Box has extra files and folders in it, but we won't worry about those just yet.


The minimum version of Solidity required is noted at the top of the contract: pragma solidity ^0.5.0;. The pragma command means "additional information that only the compiler cares about", while the caret symbol (^) means "the version indicated or higher".


The view keyword in the function declaration means that the function will not modify the state of the contract. Further information about the exact limits imposed by view is available here.



In a terminal, make sure you are in the root of the directory that contains the dapp and type:

```
truffle compile
```


```
truffle migrate
```