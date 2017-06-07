const express = require('express');
const app = express();

app.get('/', function (req, res) {
  res.send({
    'hello':'world',
    ilove: 'slinky'
  });
});

app.listen(3000, () => {
  console.log('we listening on 3000!');
});
