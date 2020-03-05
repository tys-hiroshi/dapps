# pip3 install bitsv

import polyglot
import bitsv
import yaml
import mnemonic ##pip3 install mnemonic
# https://github.com/trezor/python-mnemonic

with open('./config.yaml', 'r') as yml:
    config = yaml.load(yml)

bsvmnemonic = config["testnet"]["mnemonic"]

print(bsvmnemonic)

import binascii
import sys

# if len(sys.argv) > 1:
#     data = sys.argv[1]
# else:
#     data = sys.stdin.readline().strip()
# data = binascii.unhexlify(bsvmnemonic)

m = mnemonic.Mnemonic("english")

#print(m.to_mnemonic(data))
seed = mnemonic.Mnemonic.to_seed(bsvmnemonic, passphrase="")
masterkey = mnemonic.Mnemonic.to_hd_master_key(seed)
print(masterkey)
# data = binascii.unhexlify(masterkeyhex)
# print(data)

# https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#Serialization_format
#4 byte: version bytes 
# (mainnet: 0x0488B21E public, 0x0488ADE4 private;
#  testnet: 0x043587CF public, 0x04358394 private)

#mainnet
xprv = b"\x04\x88\xad\xe4"  ## 0x0488ADE4
xprvhex = xprv.hex()
print(xprvhex)

print(binascii.unhexlify(xprvhex))

#testnet
tprvhex = "04358394" ## 0x04358394
tprvbyte = binascii.unhexlify(tprvhex)
print(tprvbyte)
# b'\x045\x83\x94' byte
tprvbytehex = binascii.hexlify(tprvbyte)
print(tprvbytehex)

# https://github.com/trezor/python-mnemonic/blob/master/mnemonic/mnemonic.py
# Note: I defined to_hd_master_key_testnet() method
# the method definition is below.

# @classmethod
#     def to_hd_master_key_testnet(cls, seed):
#         if len(seed) != 64:
#             raise ValueError("Provided seed should have length of 64")

#         # Compute HMAC-SHA512 of seed
#         seed = hmac.new(b"Bitcoin seed", seed, digestmod=hashlib.sha512).digest()

#         # Serialization format can be found at: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#Serialization_format
#         xprv = b'\x045\x83\x94'  # Version for private testnet
#         xprv += b"\x00" * 9  # Depth, parent fingerprint, and child number
#         xprv += seed[32:]  # Chain code
#         xprv += b"\x00" + seed[:32]  # Master key

#         # Double hash using SHA256
#         hashed_xprv = hashlib.sha256(xprv).digest()
#         hashed_xprv = hashlib.sha256(hashed_xprv).digest()

#         # Append 4 bytes of checksum
#         xprv += hashed_xprv[:4]

#         # Return base58
#         return b58encode(xprv)

masterkey_testnet = mnemonic.Mnemonic.to_hd_master_key_testnet(seed)
print(masterkey_testnet)  ##prefix is tprv. Base58エンコードした値

# Note: I cant find bsvbip32 package on pypi.
# then I install from source code ( https://github.com/AustEcon/bsvbip32 )
# 1.clone repository
# 2.python3 setup.py develop

# privatekey to wif
# https://qiita.com/QUANON/items/2e280a89f6bbca5dc4a6

from bsvbip32 import Bip32

tprv = Bip32(masterkey_testnet)

privatekey_wif = tprv.wif()

print("it is privatekey wif format.")
print(privatekey_wif) ## it is privatekey wif format.
