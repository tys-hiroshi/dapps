# ERC20 ICO

Example of creating a crowdsale with Zeppelin Solidity v2.0

Companion code to the Blogpost [https://blog.zeppelin.solutions/how-to-create-token-and-initial-coin-offering-contracts-using-truffle-openzeppelin-1b7a5dae99b6](https://blog.zeppelin.solutions/how-to-create-token-and-initial-coin-offering-contracts-using-truffle-openzeppelin-1b7a5dae99b6)

```
$ npm i -g ganache-cli
$ npm i -E openzeppelin-solidity@2.0.0
$ truffle compile
$ truffle migrate

$ truffle console

purchaser = web3.eth.accounts[2]

E20TokenCrowdsale.deployed().then(inst => { crowdsale = inst })

crowdsale.token().then(addr => { tokenAddress = addr } )

tokenAddress

e20TokenInstance = E20Token.at(tokenAddress)

e20TokenInstance.addMinter(crowdsale.address)

e20TokenInstance.balanceOf(purchaser).then(balance => balance.toString(10))

E20TokenCrowdsale.deployed().then(inst => inst.sendTransaction({ from: purchaser, value: web3.toWei(5, "ether")}))

e20TokenInstance.balanceOf(purchaser).then(balance => purchaserGusTokenBalance = balance.toString(10))

web3.fromWei(purchaserGusTokenBalance, "ether")
```

