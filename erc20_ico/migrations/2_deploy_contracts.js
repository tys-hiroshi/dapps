const E20TokenCrowdsale = artifacts.require('./E20TokenCrowdsale.sol');
const E20Token = artifacts.require('./E20Token.sol');

module.exports = function(deployer, network, accounts) {
    const openingTime = web3.eth.getBlock('latest').timestamp + 20; // twenty secs in the future
    const closingTime = openingTime + 86400 * 20; // 20 days
    const rate = new web3.BigNumber(1000);
    const wallet = accounts[1];

    return deployer
        .then(() => {
            return deployer.deploy(E20Token);
        })
        .then(() => {
            return deployer.deploy(
                E20TokenCrowdsale,
                openingTime,
                closingTime,
                rate,
                wallet,
                E20Token.address
            );
        });
};
