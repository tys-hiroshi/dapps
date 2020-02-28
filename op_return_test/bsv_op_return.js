var bsv = require('bsv')
var Mnemonic = require('bsv-mnemonic')
//var datapay = require('datapay')

//let privKey = bsv.PrivateKey.fromRandom()
let privateKey = bsv.PrivateKey.fromRandom('testnet')

console.log(privateKey.toWIF())  //Import to much long privatekey charactor

key = "cUjmouxLg7StNaoZD9aX3pj3v1deQUiVsNB4ZqJ16mtv6tgRcrsq"  //testnet
let privateKey2 = bsv.PrivateKey.fromWIF(key)
console.log("privateKey2.toWIF()")
console.log(privateKey2.toWIF())

let publicKey = bsv.PublicKey.fromPrivateKey(privateKey2)
console.log("publicKey.toHex()")
console.log(publicKey.toHex())

let address = bsv.Address.fromPublicKey(publicKey)
console.log("address.toString()")
console.log(address.toString())


// const tx = {
//     safe: true,
//     data: ["0x6d02", "hello universe in testnet"],
//     pay: {
//         key: key,
//         rpc: "https://api.bitindex.network"
//     },
// };

//Can not use

// datapay.send(tx, function(err, res){
//     console.log(err)
//     console.log(res)
// })


//npm install mattercloudjs --save
// NodeJS
var options = {
    network: 'main',  // 'main', test', or 'stn'. 'main' and 'test' supported
    api_key: "2bUeAGavrUkHLAT8ScNHd3o8fYHj96SQTjukDrq72sfHHaZvCSZXWokVds76UPfGKf",
}
var mattercloud = require('mattercloudjs').instance(options);
// async function getBalanceAsync() {
//     var result = await mattercloud.getBalance('12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX');
//     console.log(result)
// }

// // getBalanceAsync().then((v) => {
// //     console.log(v);
// // })
// getBalanceAsync()

// function r(){}
// r(async () => {
// // When content loaded in page on ready, then run this code....
// mattercloud.setApiKey("2bUeAGavrUkHLAT8ScNHd3o8fYHj96SQTjukDrq72sfHHaZvCSZXWokVds76UPfGKf");
// var result = await mattercloud.getUtxos('12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX');
// console.log('result', result);
// //document.getElementById('results').innerHTML = JSON.stringify(result);
// });

// resolve1!!をreturnしているため、この値がresolveされる
// async function resolveSample() {
//     return await mattercloud.getBalance('12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX');
    
// }

// resolveSampleがPromiseを返し、resolve!!がresolveされるため
// then()が実行されコンソールにresolve!!が表示される
// resolveSample().then(value => {
//     console.log(value);
// });

// try {
//     (async () =>{
//             await Promise.reject()
//     })()
// }catch (e){
//     console.log('ERROR!', e) // これは出力されない。代わりに...
// }
// console.log('END');



// let mattercloud = require('mattercloudjs').instance({
//     api_key: '4ZiBSwCzjgkCzDbX9vVV2TGqe951CBrwZytbbWiGqDuzkDETEkLJ9DDXuNMLsr8Bpj'
//   })
  
  
async function broadcast(tx)
{
    const res = await mattercloud.sendRawTx(tx);
    return res.txid
}

async function getUtxos(addr)
{
    const res = await mattercloud.getUtxos([addr])
    return res
}

async function getBalance(addr)
{
    const res = await mattercloud.getBalance([addr]).catch((err) => 
    {
        console.log(err);
    });
    return res
}


// getUtxos("12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX").then(result => {
//     console.log(result); //
// });

console.log("getBalance")
getBalance("n2FLpfpAYXogeKMwxQFJuuX5s7dphU77G4").then(result => {
    console.log(result); //
});


// mattercloud.getBalance('14QrFf7TR7uiDpwBwrYhHaUEd83jNj23pL', function(result) {
//     console.log(result)
// });


// mattercloud.getBalance('12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX').then(result => {
//     console.log(result);
// });


// (node:8769) UnhandledPromiseRejectionWarning: #<Object>
// (node:8769) UnhandledPromiseRejectionWarning: Unhandled promise rejection. This error originated either by throwing inside of an async function without a catch block, or by rejecting a promise which was not handled with .catch(). (rejection id: 2)
// (node:8769) [DEP0018] DeprecationWarning: Unhandled promise rejections are deprecated. In the future, promise rejections that are not handled will terminate the Node.js process with a non-zero exit code.
// (node:8769) UnhandledPromiseRejectionWarning: #<Object>
// (node:8769) UnhandledPromiseRejectionWarning: Unhandled promise rejection. This error originated either by throwing inside of an async function without a catch block, or by rejecting a promise which was not handled with .catch(). (rejection id: 4)

//mattercloud is not free.
//use whatsonchain
//https://test.whatsonchain.com/
//https://bitcoinscaling.io/
//https://developers.whatsonchain.com/#get-balance
//GET https://api.whatsonchain.com/v1/bsv/<network>/address/<address>/balance
//GET curl https://api.whatsonchain.com/v1/bsv/test/address/n2FLpfpAYXogeKMwxQFJuuX5s7dphU77G4/balance
//https://test.whatsonchain.com/address/n2FLpfpAYXogeKMwxQFJuuX5s7dphU77G4#tab-json

