//https://github.com/BitcoinFiles/bitcoinfiles-sdk
var createRequest = {
    file: {
        name: 'Hello world',
        content: 'hello',
        contentType: 'text/markdown',
    },
    pay: {
        key: ""
    }
}

var bitcoinfiles = require('bitcoinfiles-sdk');
async function createFile(createRequest)
{
    const res = await bitcoinfiles.createFile(createRequest).catch((err) => 
    {
        console.log(err);
    });
    return res;
}

createFile(createRequest).then(res => {
    console.log('result', res);
});