var bsv = require('bsv')
var Mnemonic = require('bsv-mnemonic')
var datapay = require('datapay')

// let privKey = bsv.PrivateKey.fromRandom()
// let privateKey = bsv.PrivateKey.fromRandom('mainnet')

// console.log(privateKey.toWIF())  //Import to much long privatekey charactor
//L3rhtPaLariMxQvRjNq7P5tp4ocuctEB81qcLyJmkBaSB2N3GoE6
key = "L3pexkbtTNNdaaK7HwypKKEyMToNK3q3bdsGgTVrrp1bcaGkzMFt"
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
    data: ["0x6d02", "hello universe"],
    pay: {key: key},
};

datapay.send(tx, function(err, res){
    console.log(err)
    console.log(res)
})