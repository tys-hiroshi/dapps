pragma solidity ^0.4.23;

import "./E20Z2Token.sol";
// import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/ERC20Mintable.sol";
// import "../node_modules/openzeppelin-solidity/contracts/token/ERC20/IERC20.sol";
// import "../node_modules/openzeppelin-solidity/contracts/crowdsale/Crowdsale.sol";
import "../node_modules/openzeppelin-solidity/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "../node_modules/openzeppelin-solidity/contracts/crowdsale/validation/TimedCrowdsale.sol";

//https://blog.zeppelin.solutions/how-to-create-token-and-initial-coin-offering-contracts-using-truffle-openzeppelin-1b7a5dae99b6

contract E20Z2TokenCrowdsale is TimedCrowdsale, MintedCrowdsale {

    constructor
        (
            uint256 _openingTime,
            uint256 _closingTime,
            uint256 _rate,
            address _wallet,
            ERC20Mintable _token
        )
        public
        Crowdsale(_rate, _wallet, _token)
        TimedCrowdsale(_openingTime, _closingTime) 
        {
    }
}