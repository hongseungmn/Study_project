'use strict'
let express = require('express');
let app = express();

app.listen(3000,function() {
    console.log("Start! express server on port 3000!");
});

app.get("/",function(req,res){
    res.send("<h1>hi friend!</h1>");
    res.sendFile(__dirname + "public/main.html");
});