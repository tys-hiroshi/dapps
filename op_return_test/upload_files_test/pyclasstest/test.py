class Wallet:
    def __init__(self, wif, network="main"):
        self.wif = wif
        self.network = network

class Upload(Wallet):
    def __init__(self, wif, network="main"):
        super().__init__(wif)
        self.network = network


u = Upload("key", "test")
print(u.network)