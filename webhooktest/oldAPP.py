from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhookevent():
    if request.method =='GET':  
        req = request.get_json()

        iD = req.get("id")
        name = req.get("name")
        resource = req.get("resource")
    else request.method == 'POST':
        print(iD)
        print(name)
        print(resource)

        return "Okay"

    if __name__ == '__main__':
        app.run(debug=True) 

# This script bascially handles incoming JSON and returns a simple, "Okay"
# message. This was meant to experiment with an incoming Webhook. Essentially,
# determining if I could create my own webhook by simply programing a Flask
# server to respond to simple JSON POST requests from Webex. It seems to be working
# okay when I send a post request from POSTMAN, but I can't get it uploaded to a 
# proper server to test. I uploaded it to pythoneverywhere.com, but I kept getting 
# errors (even though it worked the first time).I thought about uploading to Heroku, 
# but I still can't determine whether it's working becuase Heroku doesn't show me a 
# CLI for me to see the output.  (AFAIK)