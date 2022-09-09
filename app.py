from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json
import requests
from pytube import YouTube
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from uploaddata_snowflake import upload_on_snowflake
from connect_tomongodb import upload_data_mongo

app = Flask(__name__)
#
# service_account_info = json.loads(os.getenv('CREDENTIALS'))
# creds = service_account.Credentials.from_service_account_info(
#     service_account_info)
#
#
# def upload_basic():
#     try:
#
#         service = build('drive', 'v3', credentials=creds)
#
#         file_metadata = {'name': 'video.mp4',
#                          "parents": ["1_gwj96gYxHsmvkr9u0MR_4iQrp1PHzLg"]}
#         media = MediaFileUpload('./resources/video', resumable=True)
#         # pylint: disable=maybe-no-member
#         file = service.files().create(body=file_metadata, media_body=media,
#                                       fields='id').execute()
#         print(F'File ID: {file.get("id")}')
#
#     except HttpError as error:
#         print(F'An error occurred: {error}')
#         file = None
#
#     return file.get('id')


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
            upload_on_snowflake(searchstring)
            return render_template("results.html", st=searchstring+"uploaded on snowflake")

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)
