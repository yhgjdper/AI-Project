const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('<h1> HEHEHEHE</h1>'))

app.post('/settings', (req, res) => {
    //Sends back setting variables


    
    res.send(200);
});

app.listen(port, () => console.log(`listening at http://localhost:${port}`));
