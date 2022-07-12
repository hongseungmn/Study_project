module.exports = class DB {
    info = {
    host:'114.71.137.154',
    port:'52208',
    user:'diy',
    password:'server402!',
    database:'diy'
    };

    getName(conn, res, body) {
        console.log("body =>>>>>>>>>>>>>>>>>>",body);
        const id = body.keyWord;
        //const qry = 'select SN_NAME from TB_TEST where SN_ID = ?';
        const qry = "SELECT SN_NAME FROM TB_TEST WHERE SN_NAME LIKE '%"+id+"%'";
        conn.query(qry, [id], (err, row) => {
            console.log("row=>>>>>>>>>>>>>>>>>>>>>>",row);
            res.send(row);
            res.end();
        })
    };

    getAll(conn,res){
        const qry = 'select * from TB_TEST';
        conn.query(qry,(err,row) => {
            console.log("row=>>>>>>>>>>>>>>>>>>>>>>",row);
            res.send(row);
            res.end();
        })
    };
}