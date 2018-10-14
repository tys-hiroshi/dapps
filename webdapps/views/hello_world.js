var abi = [
    {
      "constant": true,
      "inputs": [],
      "name": "get",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "pure",
      "type": "function"
    }
  ];
  var address = "0x35657c7484a5d3c782c02b65bb701f83e1ec1446"; // コントラクトアドレス
   
  window.onload = function() {
    var contract = web3.eth.contract(abi).at(address);
    contract.get((error, result) => {
      document.getElementById("contract_result").textContent = result;
    });
  };