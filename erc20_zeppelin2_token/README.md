$ truffle develop
truffle(develop)> migrate
truffle(develop)> e20z2Token = E20Z2Token.at(E20Z2Token.address)
truffle(develop)> e20z2Token.name()
'E20Z2Token'
truffle(develop)> e20z2Token.symbol()
'Z2T'
truffle(develop)> e20z2Token.totalSupply()
BigNumber { s: 1, e: 5, c: [ 100000 ] }

truffle(develop)> e20z2Token.balanceOf(web3.eth.accounts[0])
BigNumber { s: 1, e: 5, c: [ 100000 ] }
truffle(develop)> e20z2Token.balanceOf(web3.eth.accounts[1])
BigNumber { s: 1, e: 0, c: [ 0 ] }
truffle(develop)> e20z2Token.transfer(web3.eth.accounts[1], 10)
{ tx: '0x016a269aab91313529d7f13b540ca9cf55dd767a7a223b86e938c72aada5f363',
  receipt: 
   { transactionHash: '0x016a269aab91313529d7f13b540ca9cf55dd767a7a223b86e938c72aada5f363',
     transactionIndex: 0,
     blockHash: '0x26d27224a937f09edcba068678f725b297f23ebcb9094e4930bb820e15070137',
     blockNumber: 61,
     gasUsed: 51739,
     cumulativeGasUsed: 51739,
     contractAddress: null,
     logs: [ [Object] ],
     status: '0x01',
     logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000100000000000000000000000000000000010000008000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000030000000000000000000010000000000000000000000000000000000000000010000000002000000000000000000000000002000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' },
  logs: 
   [ { logIndex: 0,
       transactionIndex: 0,
       transactionHash: '0x016a269aab91313529d7f13b540ca9cf55dd767a7a223b86e938c72aada5f363',
       blockHash: '0x26d27224a937f09edcba068678f725b297f23ebcb9094e4930bb820e15070137',
       blockNumber: 61,
       address: '0xd95b1dbec167c6cf547d018ddecf41a4cb2e2f73',
       type: 'mined',
       event: 'Transfer',
       args: [Object] } ] }
truffle(develop)> e20z2Token.balanceOf(web3.eth.accounts[0])
BigNumber { s: 1, e: 4, c: [ 99990 ] }
truffle(develop)> e20z2Token.balanceOf(web3.eth.accounts[1])
BigNumber { s: 1, e: 1, c: [ 10 ] }

$ geth --networkid "10" --nodiscover --datadir ~/geth/private_net/ --rpc --rpcaddr "localhost" --rpcport "8545" --rpccorsdomain "*" --rpcapi "eth,net,web3,personal" --targetgaslimit "20000000" console 2>> ~/geth/private_net/error.log


> eth.mining
false
> miner.start(1)
Error: Cannot start mining without etherbase address: etherbase address must be explicitly specified
    at web3.js:3119:20
    at web3.js:6023:15
    at web3.js:4995:36
    at <anonymous>:1:1

> personal.newAccount()
Passphrase: 
Repeat passphrase: 
"0xc7441a410ff40c6d0f7c1f0371e11d678871afbb"
> miner.start(1)
true
