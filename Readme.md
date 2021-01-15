


  CREATE A TOKEN using this url
 ```
 curl http://localhost:5000/login
```
Store Access key which is generated from above query..
```
  export ACCESS="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTA2OTkzMTYsIm5iZiI6MTYxMDY5OTMxNiwianRpIjoiNTJjZGI2ODgtZTMzNi00NzBhLWJmN2MtYzQ1NWQyNTNmZjhlIiwiZXhwIjoxNjEwNzAwMjE2LCJpZGVudGl0eSI6MTYxMDY5OTMxNi41NzI4NjA3LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.yWY0-HBb8hLs2zif2L4Ldz08PFGeJECYFpN7J51pQdY"
```
 Make a Request to get client_id with pannumber as data argument it will verify and returns client id (save it for future use)
```
   curl -X POST -H "Content-Type: Application/json" -H "Authorization: Bearer $ACCESS" -d '{"pannumber":"DOCPD3640N"}' http://localhost:5000/getclientid
```
Now Send client_id generated from above query and it will return json data of given pannumber.
```
    curl -X POST -H "Content-Type: Application/json" -H "Authorization: Bearer $ACCESS" -d '{"client_id":"K5LEEFV"}' http://localhost:5000/getinfo
   ```
