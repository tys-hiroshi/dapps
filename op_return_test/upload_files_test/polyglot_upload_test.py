#pip3 install polyglot-bitcoin
# pip3 install bitsv

import polyglot
import bitsv
import yaml

with open('config.yml', 'r') as yml:
    config = yaml.load(yml)

privatekey_wif = config["testnet"]["privatekey_wif"]
print(privatekey_wif)
uploader = polyglot.Upload(privatekey_wif, 'test')
print(uploader.network)
# Optional parameters shown for completeness are populated from the file path by default
# filepath = "img/bitcoinsv.png"
# res = uploader.upload_b(filepath)

#filepath = "contents/bsvuploadtest.txt"
#res = uploader.upload_b(filepath)
#print(res)
#https://testnet.bitcoincloud.net/tx/47f0706cdef805761a975d4af2a418c45580d21d4d653e8410537a3de1b1aa4b
# https://testnet.bitcoincloud.net/tx/1c7df64da80389b1f5697975dac5cd1fc800ff25387210743746bee5393b1a5a
# のScriptsの	0 OP_RETURN 31394878696756345179427633744870515663554551797131707a5a56646f417574 232320426974636f696e207376206f6e20746573746e65740a0a49276d204869726f0a の
# 232320426974636f696e207376206f6e20746573746e65740a0a49276d204869726f0a がHexなので変換すると表示される。
#curl --location --request GET  "https://api.whatsonchain.com/v1/bsv/test/tx/hash/1c7df64da80389b1f5697975dac5cd1fc800ff25387210743746bee5393b1a5a"
#curl --location --request GET  "https://api.whatsonchain.com/v1/bsv/test/tx/hash/47f0706cdef805761a975d4af2a418c45580d21d4d653e8410537a3de1b1aa4b"
#curl --location --request GET  "https://api.whatsonchain.com/v1/bsv/test/tx/hash/7a8293c6d779222280766d4fb52c097085fca847111051e6540701ff76c9b897"

# address = "mnoTQaiqDBjUG6WWAUwhFycirbrKYUMgmU"

# privateKey = bitsv.PrivateKey(privatekey_wif, network="test")
# print(privateKey)
# print(privateKey.get_unspents())
# print(uploader.get_unspents())

# print(uploader.network)
# #uploader.get_largest_utxo()

#https://add.bico.media/beta/?testnet
