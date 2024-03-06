// Question 1 

const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Ecoute sur http://localhost:${port}`);
});


// Question 2 
const express = require('express');
const app = express();
const port = 3001;

app.get('/getServer', (req, res) => {
  res.json({ code: 200, server: `localhost:${port}` });
});

app.listen(port, () => {
  console.log(`Ecoute sur http://localhost:${port}`);
});
