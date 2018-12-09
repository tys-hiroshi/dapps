var E20Z2Token = artifacts.require("E20Z2Token.sol");

contract('E20Z2Token', function(accounts) {
    it("account[0] own 100000 E20Z2Token.", function() {
        return E20Z2Token.deployed().then(function(instance) {
            return instance.balanceOf.call(accounts[0]);
        }).then(function(balance) {
            assert.equal(balance.valueOf(), 100000, "account[0] don't own 100000");
        });
    });
    it("should send token correctly", function() {
        // Get initial balances of first and second account.
        var account_one = accounts[0];
        var account_two = accounts[1];
    
        var account_one_starting_balance;
        var account_two_starting_balance;
        var account_one_ending_balance;
        var account_two_ending_balance;
    
        var transfer_amount = 100;
    
        return E20Z2Token.deployed().then(function(instance) {
            return instance.balanceOf.call(account_one);
        }).then(function(balance){
            account_one_starting_balance = balance.toNumber();
            return E20Z2Token.deployed().then(function(instance) {
                return instance.balanceOf.call(account_two);
            });
        }).then(function(balance){
            account_two_starting_balance = balance.toNumber();
            return E20Z2Token.deployed().then(function(instance) {
                return instance.transfer(account_two, transfer_amount)
            });
        }).then(function(){
            return E20Z2Token.deployed().then(function(instance) {
                return instance.balanceOf.call(account_one);
            });
        }).then(function(balance){
            account_one_ending_balance = balance.toNumber();
            return E20Z2Token.deployed().then(function(instance) {
                return instance.balanceOf.call(account_two);
            });
        }).then(function(balance){
            account_two_ending_balance = balance.toNumber();
            console.log(account_one_starting_balance);
            console.log(account_two_starting_balance);
            console.log(account_one_ending_balance);
            console.log(account_two_ending_balance);
            
            assert.equal(account_one_ending_balance, account_one_starting_balance - transfer_amount, "Amount wasn't correctly taken from the sender");
            assert.equal(account_two_ending_balance, account_two_starting_balance + transfer_amount, "Amount wasn't correctly sent to the receiver");
        });
    });
});