const HelloWorld = artifacts.require("HelloWorld");
 
module.exports = (deployer) => {
  const word = "Hello";
  deployer.deploy(HelloWorld, word);
};