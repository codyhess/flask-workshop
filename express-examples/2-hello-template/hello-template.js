const express = require('express')
const app = express()

app.set('view engine', 'pug')

app.get('/', function(req, res) {
  if (!req.query.name) req.query.name = 'Nameless Person'
  res.render('index', {name: 'Hello ' + req.query.name + '!'})
})

app.listen('3000', () => {
  console.log('listening 3000')
})
