


 # CREATE A TOKEN
 curl http://localhost:5000/login





  export ACCESS="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTA3MDg1NzYsIm5iZiI6MTYxMDcwODU3NiwianRpIjoiMWZmM2JkODQtZWZjMi00NjUwLWE2Y2UtNmI1NDNkMDlhN2M2IiwiZXhwIjoxNjEwNzA5NDc2LCJpZGVudGl0eSI6MTYxMDcwODU3Ni4wNDgyNjE2LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.Kmvq4I1UBIRMKGmg3Ip-FBIdiNw_HLBbghaSVDLaus0"


   curl -X POST -H "Content-Type: Application/json" -H "Authorization: Bearer $ACCESS" -d '{"pannumber":"DOCPD3640N"}' http://localhost:5000/getclientid

    curl -X POST -H "Content-Type: Application/json" -H "Authorization: Bearer $ACCESS" -d '{"client_id":"7ZY44BX"}' http://localhost:5000/getinfo