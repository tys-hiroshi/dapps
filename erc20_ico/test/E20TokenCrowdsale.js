var E20Token = artifacts.require("E20Token.sol");
var E20TokenCrowdsale = artifacts.require("E20TokenCrowdsale.sol");

contract('E20TokenCrowdsale', function(accounts) {
    var purchaser = accounts[2];
    var purchaserGusTokenBalanceEther = 0;
    var e20TokenInst;
    var inst;
    var purchaserBalance;
    var amount = 5000;
    it("sendTransaction", function() {
        E20TokenCrowdsale.deployed().then(inst => { crowdsale = inst });
        return E20TokenCrowdsale.deployed().then(function(instance) {
            return instance.token().then(function(tokenAddress) {
                inst = instance;
                return E20Token.at(tokenAddress);
            });
        }).then(function(e20TokenInstance) {
            e20TokenInst = e20TokenInstance;
            e20TokenInstance.addMinter(crowdsale.address);
            return e20TokenInstance.balanceOf(purchaser).then(function(balance) {
                purchaserBalance = balance;
                console.log("balance");
                console.log(balance);
                console.log("purchaserGusTokenBalanceEther");
                console.log(purchaserGusTokenBalanceEther);
                //e20TokenInstance.transfer(purchaser, web3.toWei(5, "ether"));
                return e20TokenInstance.transfer(purchaser, amount);
                //return balance;
            });
        }).then(function(istransfer) {
            console.log("istransfer");
            console.log(istransfer);
            return e20TokenInst.balanceOf(purchaser).then(function(balance) {
                assert.equal(balance.valueOf(), amount, "purchaser is " + amount);
            });
        });
    });
});
