from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json
import requests

app = Flask(__name__)


def upload_on_gdrive():
    headers = {"Authorization": "Bearer "
                                "ya29.a0AVA9y1vVUMLTcq6nRnVZksDQLl5ScGdwBx315zuIDqqxURUKvHjL2h4qT952ZKvOCTagvTXxIgqDjWy"
                                "-7M_FvBfyEwY48Y"
                                "-T54QsVLHhAIunQ82JZkf4GfhwPzhUhbVDcsYicA__2Eq6T5YKRZ5l_chyFPgUaCgYKATASAQASFQE65dr8RBSENWYC-SLZkG7ZP2GVPg0163"}
    para = {
        "name": "sample.txt",
        "parents": ["1_gwj96gYxHsmvkr9u0MR_4iQrp1PHzLg"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./resources/sample.txt", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)


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
            fw.close()
            try:
                upload_on_gdrive()
            except:
                print("could not upload")

            fw = open(filename, "r")
            data = fw.read()
            return render_template("results.html", st=data)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)
