pragma solidity >=0.5.0 <0.6.0;
 
contract HelloWorld {
  string word;
 
  constructor(string memory _word) public {
      word = _word;
  }
 
  function getWord() public view returns(string memory) {
      return word;
  }
  
  function changeWord(string memory _word) public {
      word = _word;
  }
 
}