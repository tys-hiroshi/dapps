npm i -g ganache-cli
ganache-cli

truffle compile
truffle migrate

truffle console

let instance = await HelloWorld.deployed()


instance.getWord()

instance.changeWord("Hello Tarou")

instance.getWord()
