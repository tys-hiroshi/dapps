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


const tx = {
    safe: true,
    data: ["0x6d02", "hello universe in testnet"],
    pay: {
        key: key,
        rpc: "https://api.bitindex.network"
    },
};

//Can not use

// datapay.send(tx, function(err, res){
//     console.log(err)
//     console.log(res)
// })


//npm install mattercloudjs --save
// NodeJS
var options = {
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
    const res = await mattercloud.getBalance(addr);
    return res
}


// getUtxos("12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX").then(result => {
//     console.log(result); //
// });

console.log("getBalance")
getBalance("12XXBHkRNrBEb7GCvAP4G8oUs5SoDREkVX").then(result => {
    console.log(result); //
});