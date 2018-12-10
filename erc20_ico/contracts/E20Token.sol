pragma solidity ^0.4.24;

import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Mintable.sol";

contract E20Token is ERC20Mintable {
    string public name = "E20Token";
    string public symbol = "E20T";
    uint8 public decimals = 18;
}