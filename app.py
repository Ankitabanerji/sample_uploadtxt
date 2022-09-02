from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homepage():
    return render_template("index.html")


@app.route('/print', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchstring = request.form['content'].replace(" ", "")

            filename = "resources/sample.txt"
            fw = open(filename, "w")
            fw.write(searchstring)
            return render_template("results.html", st= searchstring)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)