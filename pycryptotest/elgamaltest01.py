from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA

## [python2]https://pythonhosted.org/pycrypto/Crypto.PublicKey.ElGamal-module.html

message = b"Hello"
key = ElGamal.generate(1024, Random.new().read)
# h = SHA.new()
# h.update(message)
# print(h.hexdigest())
h = SHA.new(message).digest()
print(h)
while 1:
    k = random.StrongRandom().randint(1,key.p-1)
    if GCD(k,key.p-1)==1: break
sig = key.sign(h,k)
if key.verify(h,sig):
    print("OK")
else:
    print("Incorrect signature")