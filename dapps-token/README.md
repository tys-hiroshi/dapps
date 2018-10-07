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

## initialize geth

```
geth --datadir ~/geth/private_net/ init ~/geth/private_net/genesis.json
```

## execute geth

```
geth --networkid "10" --nodiscover --datadir ~/geth/private_net/ --rpc --rpcaddr "localhost" --rpcport "8545" --rpccorsdomain "*" --rpcapi "eth,net,web3,personal" --targetgaslimit "20000000" console 2>> ~/geth/private_net/error.log
```

## Deploy private network

```
eth.mining
```

```
miner.start(1)
eth.mining
```

```
truffle migrate --network development
truffle console --network development
d = DappsToken.at('')

d.name()

d.symbol()
```

## Deploy ropsten network

https://infura.io/

https://docs.npmjs.com/getting-started/fixing-npm-permissions

~/projects/tys-hiroshi/dapps$ npm install truffle-hdwallet-provider
~/projects/tys-hiroshi/dapps/dapps-token$ truffle migrate --network ropsten

```
~/projects/tys-hiroshi/dapps/dapps-token$ truffle migrate --network ropsten
Compiling ./contracts/DappsToken.sol...
Compiling ./contracts/Migrations.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/math/SafeMath.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/BasicToken.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Basic.sol...
Compiling ./node_modules/openzeppelin-solidity/contracts/token/ERC20/StandardToken.sol...
Writing artifacts to ./build/contracts

Using network 'ropsten'.

Running migration: 1_initial_migration.js
  Deploying Migrations...
  ... 0x00abd4776c7ae37c2114a1f30d24f43db586aa1c26dfa08e84a2912606f10640
  Migrations: 0xdda768633b8616a2f705857394dac563981e884e
Saving successful migration to network...
  ... 0xcb2f879d82a93fd54c7b210696b0208d3780ae9df21cfc1821c2b4296344fd9a
Saving artifacts...
Running migration: 2_deploy_dapps_token.js
  Deploying DappsToken...
  ... 0xcb53c37110cbdbaedd428b366ccfb2fa5224ed7528f8b8595becf463f293e07e
  DappsToken: 0x1b916f28c73d10b6befd159add051be0e86e3c20
Saving successful migration to network...
  ... 0x77760ddfb9c65add58187110f9cfb28259a59a242bbfb2fa148f404316a51534
Saving artifacts...
```

### Add DappsToken to MetaMask.

DappsToken: 0x1b916f28c73d10b6befd159add051be0e86e3c20

You can see below.

https://github.com/tys-hiroshi/dapps/blob/master/dapps-token_img/Screenshot%20from%202018-10-07%2016-24-53.jpg
https://github.com/tys-hiroshi/dapps/blob/master/dapps-token_img/Screenshot%20from%202018-10-07%2016-25-22.jpg
