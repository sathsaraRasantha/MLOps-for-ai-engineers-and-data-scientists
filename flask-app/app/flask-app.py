from flask import Flask, jsonify, request
from area import area_in_acres

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def get_input():
    packet = request.get_json(force=True)
    length = packet['length']
    width = packet['width']

    area = area_in_acres(length,width)

    return {"area in acres": area}


if __name__ == '__main__':
    app.run(debug=True)


