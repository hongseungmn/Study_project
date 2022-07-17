'use strict'
let express = require('express');
let app = express();
let bodyParser = require("body-parser");
let cors = require('cors');

app.listen(3000,function() {
    console.log("Start! express server on port 3000!");
});

app.use(express.static("public"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.use(cors);
app.set("view engine","ejs");

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
    //get : req.param('email')
    console.log(req.body.email);
    //res.send("<h1>welcome!! " + req.body.email + "</h1>");
    res.render("email.ejs",{'email' : req.body.email});
});

app.post("/ajax_send_email",function(req,res){
    console.log(req.body.email);
    //check validation about input values => DB
    let responseData = {'resule' : 'ok','email' : req.body.email};
    res.json(responseData);
});