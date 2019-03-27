var express = require('express');
var Fuse = require('fuse.js');
var bodyParser = require('body-parser');
var cors = require('cors')
var app = express();

app.use(cors())
var actsObject = require('../acts.json')
var titlesObject = require('../title.json')
var keywordsObject = require('../keyword.json')

var options = {
  keys: ['data'],
   shouldSort: true,
  threshold: 0.0,
  location: 0,
  distance: 30,
  maxPatternLength: 32,
  minMatchCharLength: 1

};
var acts = new Fuse(actsObject,options);
var titles = new Fuse(titlesObject,options);
var keywords = new Fuse(keywordsObject,options);

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());


app.get('/', function (req,res) {
   console.log("Hello")
   res.send("Hello")
})


app.post('/acts',function(req,res){
	suggestions = acts.search(req.body.query)
	// console.log("wad")
	console.log(req.body.query)
	// res.send("Hello")
	res.send(suggestions)
})

app.post('/titles',function(req,res){
	suggestions = titles.search(req.body.query)
	// console.log(keywords)
	console.log(req.body.query)
	// res.send("Hello")
	res.send(suggestions)
})

app.post('/keywords',function(req,res){
	suggestions = keywords.search(req.body.query)
	// console.log(keywords)
	console.log(req.body.query)
	// res.send("Hello")
	res.send(suggestions)
})


var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})