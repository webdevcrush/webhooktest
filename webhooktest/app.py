from flask import Flask, request
import logging

logging.basicConfig(filename='test.txt', level=logging.INFO)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhookevent():
    # if request.method == 'GET':
    #     return "Yo, this works"

    if request.method == 'POST':
        req = request.get_json()

        iD = req.get("id")
        name = req.get("name")
        resource = req.get("resource")
        
        logging.info(iD)
        logging.info(name)
        logging.info(resource)

        return "okay", 200
    elif request.method == 'GET':
        return "Yes, this works okay."

        
if __name__ == '__main__':
    app.run(debug=True)