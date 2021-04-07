# To run the server
#   flask run -p 8085

import json
from flask import Flask, request

app = Flask(__name__)

RESPONSE_PING               = {"message":"I'm alive!!"}
RESPONSE_GET                = {"message":"Get Message Received"}
RESPONSE_BAD_REQUEST        = "Bad Request"
RESPONSE_METHOD_NOT_ALLOWED = "Method Not Allowed"

STATUS_OK          = 200
STATUS_BAD_REQUEST = 400
STATUS_NOT_ALLOWED = 405

GET  = "GET"
POST = "POST"

# curl --request GET --header "Content-Type: application/json" --write-out "\n%{http_code}\n" http://localhost:8085/ping
# curl --request POST --write-out "\n%{http_code}\n" http://localhost:8085/ping
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    json_msg = ""
    if request.method == POST:
        json_msg = json.dumps(RESPONSE_METHOD_NOT_ALLOWED), STATUS_NOT_ALLOWED
    elif request.method == GET:
        json_msg = json.dumps(RESPONSE_PING), STATUS_OK
    return json_msg


# curl --request POST --write-out "\n%{http_code}\n" http://localhost:8085/ping/slug
# curl --request GET --write-out "\n%{http_code}\n" http://localhost:8085/ping/slug
@app.route('/ping/<name>', methods=['GET', 'POST'])
def pingname(name):
    json_msg = ""
    if request.method == GET:
        json_msg = json.dumps(RESPONSE_METHOD_NOT_ALLOWED), STATUS_NOT_ALLOWED
    elif request.method == POST:
        json_msg = json.dumps({"message": f"I'm alive, {name}!!"}), STATUS_OK
    return json_msg



# curl --request GET --header "Content-Type: application/json" --write-out "\n%{http_code}\n "http://localhost:8085/echo
# curl --request POST --header "Content-Type: application/json" --write-out "\n%{http_code}\n "http://localhost:8085/echo?msg=foo
# curl --request POST --write-out "\n%{http_code}\n"  http://localhost:8085/echo
@app.route('/echo', methods=['GET', 'POST'])
def echo():
    json_msg = ""
    msg = request.args.get('msg')

    if msg == "" or msg == None:
        if request.method == GET:
            json_msg = json.dumps(RESPONSE_GET), STATUS_OK
        elif request.method == POST:
            json_msg = json.dumps(RESPONSE_BAD_REQUEST), STATUS_BAD_REQUEST
    else:
        if request.method == GET:
            json_msg = json.dumps(RESPONSE_GET), STATUS_OK
        elif request.method == POST:
            json_msg = json.dumps({"message":msg}), STATUS_OK        
    return json_msg
