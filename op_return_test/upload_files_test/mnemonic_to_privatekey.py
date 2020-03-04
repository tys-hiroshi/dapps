# pip3 install bitsv

import polyglot
import bitsv
import yaml

with open('config.yaml', 'r') as yml:
    config = yaml.load(yml)

mnemonic = config["testnet"]["mnemonic"]

print(mnemonic)

bitsv.Key()