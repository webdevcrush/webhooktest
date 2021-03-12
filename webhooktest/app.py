from flask import Flask, render_template, request
from send_mail import send_mail

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhookevent():

    if request.method == 'POST':
        req = request.get_json()

        iD = req.get("id")
        name = req.get("name")
        resource = req.get("resource")
        event = req.get("event")
        filter = req.get("filter")
        orgId = req.get("orgId")
        createdBy = req.get("createdBy")
        appId = req.get("appId")
        ownedBy = req.get("ownedBy")
        status = req.get("status")
        actorId = req.get("actorId")
        data_id = req['data']['id']
        data_roomId = req['data']['roomId']
        data_personId = req['data']['personId']
        data_personEmail = req['data']['personEmail']
        data_created = req['data']['created']


        print(iD)
        print(name)
        print(resource)
      
        send_mail(iD, name, resource, event, filter, orgId, createdBy, appId, ownedBy, status, actorId, data_id, data_roomId, data_personId, data_personEmail, data_created)
        return "okay", 200
    elif request.method == 'GET':
        return "Yes, this works okay."

        
if __name__ == '__main__':
    app.run(debug=True)