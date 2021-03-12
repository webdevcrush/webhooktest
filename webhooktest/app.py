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
        
        # data 
        # {
        #     id
        #     roomId
        #     personId
        #     personEmail
        #     created
        # }
        # Probaby not required to handle all of these... so can grab only the ones you want.
        # For a workable example, however, you'd probably wnat to handle all of them.

        print(iD)
        print(name)
        print(resource)
      
        send_mail(iD, name, resource, event, filter, orgId, createdBy, appId, ownedBy, status, actorId)
        return "okay", 200
    elif request.method == 'GET':
        return "Yes, this works okay."

        
if __name__ == '__main__':
    app.run(debug=True)