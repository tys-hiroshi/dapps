
const E20Z2TokenCrowdsale = artifacts.require('./E20Z2TokenCrowdsale.sol');
const E20Z2Token = artifacts.require('./E20Z2Token.sol');

module.exports = function(deployer, network, accounts) {
    const openingTime = web3.eth.getBlock('latest').timestamp + 2; // two secs in the future
    const closingTime = openingTime + 86400 * 20; // 20 days
    const rate = new web3.BigNumber(1000);
    const wallet = accounts[1];

    return deployer
        .then(() => {
            return deployer.deploy(E20Z2Token);
        })
        .then(() => {
            return deployer.deploy(
                E20Z2TokenCrowdsale,
                openingTime,
                closingTime,
                rate,
                wallet,
                E20Z2Token.address
            );
        });
};