var E20Z2Token = artifacts.require("E20Z2Token.sol");

contract('E20Z2Token', function(accounts) {
    it("account[0] own 100000 E20Z2Token.", function() {
        return E20Z2Token.deployed().then(function(instance) {
            return instance.balanceOf.call(accounts[0]);
        }).then(function(balance) {
            assert.equal(balance.valueOf(), 100000, "account[0] don't own 100000");
        });
    });
});