import os
from io import BytesIO
import bitsv
from bitsv import op_return
from bitsv import crypto
from bitsv import utils

network = "test"
woc = bitsv.network.services.WhatsonchainNormalised(api_key=None, network=network)
print(woc)

unspents = woc.get_unspents("mnoTQaiqDBjUG6WWAUwhFycirbrKYUMgmU")
for item in unspents :
    print(item)