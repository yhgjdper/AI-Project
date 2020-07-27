'use strict';

const rl = require("readline");
const fs = require('fs');
var bodyParser = require('body-parser')

const request = require('request');

const util = require('util');

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

/*
app.get('/getJson', function (req, res) {
    
    // If it's not showing up, just use req.body to see what is actually being passed.
    //console.log(req.body.selectpicker);
    console.log(util.inspect(req.body, false, null));
    
});
*/
let inputType = 'speech'
let outputType = 'speech'
let browserType = 'chrome'

app.post('/getResults', function(req, res) {
    if (req.body['input'] != undefined) {
        inputType = req.body['input'];
        console.log(req.body['input'])
    }
    else if (req.body['output'] != undefined) {
        outputType = req.body['output'];
        console.log(req.body['output'])
    }
    else if (req.body['browser'] != undefined) {
        browserType = req.body['browser'];
        console.log(req.body['browser'])
    }
    let setting = {
        input: inputType,
        output: outputType,
        browser: browserType
    };
    let data = JSON.stringify(setting);

    fs.writeFile('settings.json', data, (err) => {
        if (err) throw err;
        console.log('Data written to file');
    });
    res.redirect('/')
})

app.post('/startTalking', function(req, res) {
    console.log(req.body)
    res.redirect('/')
    if (req.body['talkButton'] == "toggle"){
        let talkData = {
            toggleTalking: 'on'
        };
        let talkJSON = JSON.stringify(talkData);
        fs.writeFile('startTalking.json', talkJSON, (err) => {
            if (err) throw err;
            console.log('Data written to file')
        })
    }
})




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