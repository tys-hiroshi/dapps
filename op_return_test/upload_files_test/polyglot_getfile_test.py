import requests
import json

# https://api.whatsonchain.com/v1/bsv/test/tx/hash/1c7df64da80389b1f5697975dac5cd1fc800ff25387210743746bee5393b1a5a
url = "https://api.whatsonchain.com/v1/bsv/test/tx/hash/1c7df64da80389b1f5697975dac5cd1fc800ff25387210743746bee5393b1a5a"
#url = "https://api.whatsonchain.com/v1/bsv/test/tx/hash/47f0706cdef805761a975d4af2a418c45580d21d4d653e8410537a3de1b1aa4b"
headers = {"content-type": "application/json"}
r = requests.get(url, headers=headers)
data = r.json()
print(json.dumps(data, indent=4))
print(data['vout'][0]['scriptPubKey']['asm'])
binary = data['vout'][0]['scriptPubKey']['asm'].split()[3]

import binascii
path_w = 'download/bitcoinsv.txt'
with open(path_w, mode='wb') as f:
    f.write(binascii.unhexlify(binary))