# ERC20 token

https://github.com/tys-hiroshi/EIPs/blob/master/EIPS/eip-20.md

## 

```
mkdir dapps-token
cd dapps-token
truffle init
$ npm init -y
$ npm install -E openzeppelin-solidity
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN dapps-token@1.0.0 No repository field.

+ openzeppelin-solidity@1.12.0
added 1 package from 1 contributor in 0.351s
```

```
truffle(develop)> test
Using network 'develop'.

Compiling ./contracts/DappsToken.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/math/SafeMath.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/BasicToken.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Basic.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/StandardToken.sol...


  Contract: DappsToken
    ✓ should put 1000 DappsToken in the first account


  1 passing (45ms)

truffle(develop)> migrate

truffle(develop)> dappsToken = DappsToken.at(DappsToken.address)
truffle(develop)> dappsToken.name()
'DappsToken'
truffle(develop)> dappsToken.symbol()
'DTKN'
truffle(develop)> dappsToken.totalSupply()
BigNumber { s: 1, e: 3, c: [ 1000 ] }
truffle(develop)> dappsToken.balanceOf(web3.eth.accounts[0])
BigNumber { s: 1, e: 3, c: [ 1000 ] }
truffle(develop)> dappsToken.balanceOf(web3.eth.accounts[1])
BigNumber { s: 1, e: 0, c: [ 0 ] }
truffle(develop)> dappsToken.transfer(web3.eth.accounts[1], 100)
truffle(develop)> dappsToken.balanceOf(web3.eth.accounts[0])
BigNumber { s: 1, e: 2, c: [ 900 ] }
truffle(develop)> dappsToken.balanceOf(web3.eth.accounts[1])
BigNumber { s: 1, e: 2, c: [ 100 ] }

```