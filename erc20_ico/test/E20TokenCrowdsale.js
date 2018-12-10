var E20Token = artifacts.require("E20Token.sol");
var E20TokenCrowdsale = artifacts.require("E20TokenCrowdsale.sol");

contract('E20TokenCrowdsale', function(accounts) {
    var purchaser = accounts[2];
    it("sendTransaction", function() {
        return E20TokenCrowdsale.deployed().then(function(instance) {
            return instance.token().then(function(tokenAddress) {
                return E20Token.at(tokenAddress);
            });
        }).then(function(e20TokenInstance) {
            e20TokenInstance.addMinter(crowdsale.address);
            return e20TokenInstance.balanceOf(purchaser).then(function(balance) {
                console.log(balance);
                return E20TokenCrowdsale.deployed().then(function(instance) {
                    instance.sendTransaction({ from: purchaser, value: web3.toWei(5, "ether")});
                });
                e20TokenInstance.balanceOf(purchaser).then(balance => purchaserGusTokenBalance = balance.toString(10));
                console.log(web3.fromWei(purchaserGusTokenBalance, "ether"));
            });
        });
    });
});
