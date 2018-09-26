pragma solidity ^0.4.23;
import "openzeppelin-solidity/contracts/ownership/Ownable.sol";

contract DappsToken is StandardToken {
    string public name = "DappsToken";
    string public symbol = "DTKN";
    uint public decimals = 18;

    constructor(uint initialSupply) public {
        totalSupply_ initialSupply;
        balances[msg.sender] = initialSupply;
    }
}