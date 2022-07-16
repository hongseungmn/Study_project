'use strict'
let express = require('express');
let app = express();

app.listen(3000,function() {
    console.log("Start! express server on port 3000!");
});

app.use(express.static("public"));

//url routing
app.get("/",function(req,res){
    //res.send("<h1>hi friend!</h1>");
    res.sendFile(__dirname + "/public/main.html");
});

app.get("/main",function(req,res){
    //res.send("<h1>hi friend!</h1>");
    res.sendFile(__dirname + "/public/main.html");
});

app.post("/email_post", function(req,res){
    //get : req.paran('email')
    res.send("post response");
})