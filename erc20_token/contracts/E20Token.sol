pragma solidity ^0.4.23;
//import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";
import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/StandardToken.sol";

contract E20Token is StandardToken {
    string public name = "E20Token";  //Token name
    string public symbol = "E20T";  //Token unit
    uint public decimals = 18;  //18 is the most common number of decimal places

    constructor(uint initialSupply) public {
        totalSupply_ = initialSupply;
        balances[msg.sender] = initialSupply;
    }
}