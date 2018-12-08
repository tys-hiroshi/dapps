pragma solidity ^0.4.23;

//import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";
//import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Detailed.sol";
import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Mintable.sol";
import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Burnable.sol";
import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Detailed.sol";

contract E20Z2Token is ERC20Mintable, ERC20Burnable, ERC20Detailed {

    string private _name = "E20Z2Token";
    string private _symbol = "Z2T";
    uint8 private _decimals = 18;

    uint value = 1000000;

    constructor()
        ERC20Detailed(_name, _symbol, _decimals)
        ERC20Burnable()
        ERC20Mintable()
        public
    {
        _mint(msg.sender, value);
    }
}