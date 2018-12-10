pragma solidity ^0.4.23;

import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Mintable.sol";

contract E20Z2Token is ERC20Mintable {
    string public name = "E20Z2Token";
    string public symbol = "Z2T";
    uint8 public decimals = 18;
}