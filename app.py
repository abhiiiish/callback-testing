from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)


@app.route('/store', methods=['GET','POST'])
def request_get():

    url = 'http://127.0.0.1:5000/show'

    params = {
        "brand_id": "656890e90866e3d38a426d4f"
    }

    headers = {"Authorization": "k5esldhz7TkrK9rYqN69RbzifYTd9u2J"}

    data = requests.get(url, params==params, headers=headers)

    if data.status_code==200:
        result = data.json()

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)


