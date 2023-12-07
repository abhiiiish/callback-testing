from flask import Flask, render_template, request, jsonify
import requests

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector


app = Flask(__name__)
app.secret_key = '9876543210'


db_config = {
    'host': 'localhost',
    'user': 'user_1',
    'password': 'pass.c0m',
    'database': 'abhishek'
}

@app.route('/store', methods=['GET','POST'])
def request_get():

    url = 'https://callback-test-oe2t.onrender.com/store'

    params = {
        "brand_id": "656890e90866e3d38a426d4f"
    }

    headers = {"Authorization": "k5esldhz7TkrK9rYqN69RbzifYTd9u2J"}

    # data = requests.get(url, params=params, headers=headers)

    # if data.status_code==200:
    #     result = data.json()
    # else:
    #     print("Error occurred - {}".format(data.text))


    if request.method == 'GET':
        data = requests.get(url, params=params, headers=headers)
        brand_id = data.get('brand_id')
        post_id = data.get('post_id')
        caption = data.get('caption')
        status = data.get('status')
        generated_media = data.get('generated_media')
        media_type = data.get('media_type')

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            sql = "INSERT INTO predis_data (brand_id, post_id, caption, status, generated_media, media_type) VALUES(%s, %s, %s, %s, %s, %s,)"
            values = (brand_id, post_id, caption, status, generated_media, media_type)

            cursor.execute(sql,values)
            connection.commit()
        
        except mysql.connector.Error as err:
            return f"Error: {err}"

        finally: 
            if connection.is_connected():
                cursor.close()
                connection.close()

    return 





if __name__ == '__main__':
    port = 3000  # Use equals sign here
    app.run(debug=True, port=port)



