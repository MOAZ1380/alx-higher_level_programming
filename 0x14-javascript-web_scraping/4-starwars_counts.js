#!/usr/bin/node
const request = require('request');
url = process.argv[2];
request(url, function (error, response, body){
        let body2 = JSON.parse(body).results;
        let x = 0;
        let count = 0;
        for(let i = 0; i < body2.length; i++){
                let character = JSON.parse(body).results[i].characters;
                for(let x =0; x < character.length;x++){
                        let character2 = character[x];
                        if (character2.endsWith('/18/')){
                                count +=1;
                        }
                        else{
                                count+=0;
                        }       
                }
        }
        console.log(count);
});

