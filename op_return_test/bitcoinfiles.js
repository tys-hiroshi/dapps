//https://github.com/BitcoinFiles/bitcoinfiles-sdk
// npm i bitcoinfiles-sdk --save

var bsv = require('bsv')
var Mnemonic = require('bsv-mnemonic')
//let privKey = bsv.PrivateKey.fromRandom()
//let privateKey = bsv.PrivateKey.fromRandom('livenet')  //livenet or testnet

//console.log(privateKey.toWIF())  //Import to much long privatekey charactor

key = "L5jMsatWLXW2ei5v6oMfrxW1JJ9nZKiRSHBMnF9dSFepTHGfyu3F"  //livenet
//key = "cUjmouxLg7StNaoZD9aX3pj3v1deQUiVsNB4ZqJ16mtv6tgRcrsq"  //testnet
//https://developers.whatsonchain.com/#get-api-status

var createRequest = {
    file: {
        name: 'Hello world',
        content: 'hello',
        contentType: 'text/markdown',
    },
    pay: {
        key: key,
        rpc: "https://whatsonchain.com/",
    }
}

var bitcoinfiles = require('bitcoinfiles-sdk');
async function createFile(createRequest)
{
    const res = await bitcoinfiles.createFile(createRequest).catch((err) => 
    {
        console.log(err);
    });
    return res;
}

createFile(createRequest).then(res => {
    console.log('result', res);
});