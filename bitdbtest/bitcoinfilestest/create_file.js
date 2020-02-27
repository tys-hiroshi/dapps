var bitcoinfiles = require('bitcoinfiles-sdk');

/*
    Use with promises
*/
const result = await bitcoinfiles.createFile({
    file: {
        content: 'hello world',
        contentType: 'text/plain',
    },
    pay: {
        key: "your wif key"
    }
});

console.log(result);

/*
Use with callback
*/
require('bitcoinfiles-sdk').createFile({
    file: {
        content: 'hello world',
        contentType: 'text/plain',
    },
    pay: {
        key: "your wif key"
    }
}, function(result) {
    console.log(result)
});
/*
{
    success: true
    txid: "8657f139afbce31c038b852c8d6fb602b71f265d44421e357e02d602f0e4b8a3"
}
*/