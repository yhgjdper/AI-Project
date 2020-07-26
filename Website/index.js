'use strict';

const fs = require('fs');
var bodyParser = require('body-parser')

var express = require('express'),
    app = express();
var http = require('http');

app.use(bodyParser.urlencoded({
    extended: true
}));

const PORT=8080; 

// as only one page can use res.sendfile to render the page which will contain the drop   downs


app.get('/', function(req, res){
    res.sendfile('./website/index.html');
});

app.get('/getJson', function (req, res) {
    
    // If it's not showing up, just use req.body to see what is actually being passed.
    console.log(req.body.selectpicker);
});

app.listen(3000); 
/*
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
*/
console.log('YEP');