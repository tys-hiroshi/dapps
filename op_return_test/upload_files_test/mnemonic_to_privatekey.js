var bsv = require('bsv')
var fs = require("fs");

var use_require_json = require('./config.json');
console.log(use_require_json)
var bsv_mnemonic = use_require_json.testnet.bsv_mnemonic
console.log(bsv_mnemonic)

// Get testnet wallet on https://tools.fullcyclemining.com/
// Success: you have a new testnet wallet
// Wallet Passphrase: -----------------
// Receiving Address: mxPSrbZEKRf2soJ5cfrHnAsNj2BH9jdHEv
var Mnemonic = require('bsv-mnemonic');
var code = new Mnemonic(bsv_mnemonic);

var xpriv1 = code.toHDPrivateKey("", network='testnet'); // no passphrase
//var xpriv2 = code.toHDPrivateKey('my passphrase'); // using a passphrase

console.log(xpriv1)
console.log(xpriv1.privateKey)
privatekey_wif = xpriv1.privateKey.toWIF()
console.log(privatekey_wif)

let privateKey2_ = bsv.PrivateKey.fromWIF(privatekey_wif)
console.log("privateKey2_.toWIF()")
console.log(privateKey2_.toWIF())

let publicKey_ = bsv.PublicKey.fromPrivateKey(privateKey2_)
console.log("publicKey_.toHex()")
console.log(publicKey_.toHex())

let address_ = bsv.Address.fromPrivateKey(privateKey2_)
console.log("address_.toString()")
console.log(address_.toString())

// // let address_ = bsv.Address.fromPublicKey(publicKey_)
// // console.log("address_.toString()")
// // console.log(address_.toString())

