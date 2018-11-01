/*
 * NB: since truffle-hdwallet-provider 0.0.5 you must wrap HDWallet providers in a 
 * function when declaring them. Failure to do so will cause commands to hang. ex:
 * ```
 * mainnet: {
 *     provider: function() { 
 *       return new HDWalletProvider(mnemonic, 'https://mainnet.infura.io/<infura-key>') 
 *     },
 *     network_id: '1',
 *     gas: 4500000,
 *     gasPrice: 10000000000,
 *   },
 */

// module.exports = {
//   // See <http://truffleframework.com/docs/advanced/configuration>
//   // to customize your Truffle configuration!
// };

var HDWalletProvider = require("truffle-hdwallet-provider");
var mnemonic = your.metamask.mnemonic;
var accessToken = your.Infra.accessToken;


module.exports = {
  networks:{
    development:{
      host: "localhost",
      port: 8545,
    network_id:"10"
    },
  ropsten:{
    provider: function(){
    return new HDWalletProvider(
      mnemonic,
      "https://ropsten.infura.io/" + accessToken
    );
  },
    network_id: 3,
    gas: 500000
    }
  }
};