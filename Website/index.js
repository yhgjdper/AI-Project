let app = require('express');

app.get('/', (req, res) => {
    res.send('<h1> BEEEG GAMERS GAMING </h>');
});

app.listen(3000, console.log('Server listening in 3000'));