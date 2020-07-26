'use strict';

const fs = require('fs');

let setting = {
    input: "speech",
    output: "speech",
    browser: "chrome"
};

let data = JSON.stringify(setting);

fs.writeFile('settings.json', data, (err) => {
    if (err) throw err;
    console.log('Data written to file');
});

var http = require('http');

const PORT=8080; 

fs.readFile('./website/index.html', function (err, html) {

    if (err) throw err;    

    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(PORT);
});
console.log('YEP');