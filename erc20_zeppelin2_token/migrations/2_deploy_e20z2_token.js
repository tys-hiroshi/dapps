var E20Z2Token = artifacts.require("./E20Z2Token.sol")

module.exports = function(deployer) {
    var initialSupply = 100000;
    deployer.deploy(E20Z2Token, initialSupply);
}