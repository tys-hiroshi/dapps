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

https://infura.io/
