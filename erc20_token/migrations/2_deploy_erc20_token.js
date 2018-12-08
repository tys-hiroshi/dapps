var E20Token = artifacts.require("./E20Token.sol")

module.exports = function(deployer) {
    var initialSupply = 100000;
    deployer.deploy(E20Token, initialSupply);
}