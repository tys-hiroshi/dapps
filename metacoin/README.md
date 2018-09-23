```
$ mkdir metacoin
$ cd metacoin/
$ truffle unbox metacoin
Downloading...
Unpacking...
Setting up...
Unbox successful. Sweet!

Commands:

  Compile contracts: truffle compile
  Migrate contracts: truffle migrate
  Test contracts:    truffle test
$ truffle develop
> compile
truffle(develop)> migrate
Using network 'develop'.

Running migration: 1_initial_migration.js
  Deploying Migrations...
  ... 0x560efaa7b8bd704637c868bee2747b4f3105f529ac81815085d8628dfb48bed6
  Migrations: 0x8cdaf0cd259887258bc13a92c0a6da92698644c0
Saving successful migration to network...
  ... 0xd7bc86d31bee32fa3988f1c1eabce403a1b5d570340a3a9cdba53a472ee8c956
Saving artifacts...
Running migration: 2_deploy_contracts.js
  Deploying ConvertLib...
  ... 0x1ea7ae41a73e00e2f3687839d2e2746ff71f095c05ca6750eb9a2bf744aa2404
  ConvertLib: 0x345ca3e014aaf5dca488057592ee47305d9b3e10
  Linking ConvertLib to MetaCoin
  Deploying MetaCoin...
  ... 0xf5a57fcf963dd9d59affd99924b98fa14449f321805de332dc508788380e325b
  MetaCoin: 0xf25186b5081ff5ce73482ad761db0eb0d25abfbf
Saving successful migration to network...
  ... 0x059cf1bbc372b9348ce487de910358801bbbd1c89182853439bec0afaee6c7db
Saving artifacts...
```

Call Contract of MetaCoin

```
> m = MetaCoin.at("0xf25186b5081ff5ce73482ad761db0eb0d25abfbf")
truffle(develop)> m.getBalance(web3.eth.accounts[0])
BigNumber { s: 1, e: 4, c: [ 10000 ] }
truffle(develop)> m.getBalance(web3.eth.accounts[1])
BigNumber { s: 1, e: 0, c: [ 0 ] }
truffle(develop)> m.sendCoin(web3.eth.accounts[1], 1000)
{ tx: '0x6b650d826e20aba52c82636f3f2947a263a66714f0684975253527e6f810d1ea',
  receipt: 
   { transactionHash: '0x6b650d826e20aba52c82636f3f2947a263a66714f0684975253527e6f810d1ea',
     transactionIndex: 0,
     blockHash: '0xa0ad6b7ad4bf877c85424f3ea3e7ce61698c104eda92703d28ea9e0b061d4b76',
     blockNumber: 6,
     gasUsed: 51057,
     cumulativeGasUsed: 51057,
     contractAddress: null,
     logs: [ [Object] ],
     status: '0x01',
     logsBloom: '0x00000000000000000000000000000000010000000000000000000010000000000000000000000020000000000000000000000000000000000000000000000000000000000000000010000008000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000010000000000000000000010000000000000000000000000000000000000000010000000002000000000000000000000000000000000000002000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' },
  logs: 
   [ { logIndex: 0,
       transactionIndex: 0,
       transactionHash: '0x6b650d826e20aba52c82636f3f2947a263a66714f0684975253527e6f810d1ea',
       blockHash: '0xa0ad6b7ad4bf877c85424f3ea3e7ce61698c104eda92703d28ea9e0b061d4b76',
       blockNumber: 6,
       address: '0xf25186b5081ff5ce73482ad761db0eb0d25abfbf',
       type: 'mined',
       event: 'Transfer',
       args: [Object] } ] }
truffle(develop)> m.getBalance(web3.eth.accounts[0])
BigNumber { s: 1, e: 3, c: [ 9000 ] }
truffle(develop)> m.getBalance(web3.eth.accounts[1])
BigNumber { s: 1, e: 3, c: [ 1000 ] }

```

If you send over coin(ex: 9500), it's failed.
