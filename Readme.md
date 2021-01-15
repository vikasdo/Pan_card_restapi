


  CREATE A TOKEN using this url
 ```
 curl http://localhost:5000/login


I have mongodb running on cloud 
```
Store Access key which is generated from above query..
```
  export ACCESS="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTA3MjA5NjUsIm5iZiI6MTYxMDcyMDk2NSwianRpIjoiZTMwNDAzZTUtNDYzYy00YTE1LTkyYWEtYTcxNDMxZTI0MDIxIiwiZXhwIjoxNjEwNzIxODY1LCJpZGVudGl0eSI6MTYxMDcyMDk2NS41NzMxODEyLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.DcH7VykH-lE2cJUnfLgFM3XPYekIu-9ctJePZTb_05g"



```
 Make a Request to get client_id with pannumber as data argument it will verify and returns client id (save it for future use)
```
   curl -X POST -H "Content-Type: Application/json" -H "Authorization: Bearer $ACCESS" -d '{"pannumber":"DOCPD3640N"}' http://localhost:5000/getclientid
```
Now Send client_id generated from above query and it will return json data of given pannumber.
```
    curl -X POST -H "Content-Type: Application/json" -H "Authorization: Bearer $ACCESS" -d '{"client_id":"T8E704Y"}' http://localhost:5000/getinfo
   ```
