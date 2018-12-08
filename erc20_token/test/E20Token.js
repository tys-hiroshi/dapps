var ERC20Token = artifacts.require("E20Token.sol");

contract('E20Token', function(accounts) {
    it("account[0] own 100000 E20Token.", function() {
        return ERC20Token.deployed().then(function(instance) {
            return instance.balanceOf.call(accounts[0]);
        }).then(function(balance) {
            assert.equal(balance.valueOf(), 100000, "account[0] don't own 100000");
        });
    });
});