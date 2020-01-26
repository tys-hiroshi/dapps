pragma solidity ^0.5.0;

contract Adoption {

    address[16] public adopters;  //This is an array of Ethereum addresses.   16個のアドレスを用意する(初期値: 0x0000000000000000000000000000000000000000)

    // Adopting a pet
    function adopt(uint petId) public returns (uint) {
        require(petId >= 0 && petId <= 15);

        adopters[petId] = msg.sender;  //「msg.sender」を使うと、関数を呼び出したスマートコントラクトのアドレスを参照できる

        return petId;
    }
    
    // Retrieving the adopters
    function getAdopters() public view returns (address[16] memory) {
        return adopters;
    }
}