const express = require('express');
const app = express();

app.get('/', function (req, res) {
  res.setHeader('Content-type', 'application/json');
  res.send(JSON.stringify({'hello':'world'}));
});

app.listen(3000, () => {
  console.log('we listening on 3000!');
});
