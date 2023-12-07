from flask import Flask, request
import requests
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'user_1',
    'password': 'pass.c0m',
    'database': 'abhishek'
}

@app.route('/store', methods=['GET', 'POST'])
def request_get():
    url = 'https://callback-test-oe2t.onrender.com/store'
    params = {"brand_id": "656890e90866e3d38a426d4f"}
    headers = {"Authorization": "k5esldhz7TkrK9rYqN69RbzifYTd9u2J"}

    if request.method == 'GET':
        data = requests.get(url, params=params, headers=headers)
        if data.status_code == 200:
            json_data = data.json()
            brand_id = json_data.get('brand_id')
            post_id = json_data.get('post_id')
            caption = json_data.get('caption')
            status = json_data.get('status')
            generated_media = json_data.get('generated_media')
            media_type = json_data.get('media_type')

            try:
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()

                sql = "INSERT INTO predis_data (brand_id, post_id, caption, status, generated_media, media_type) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (brand_id, post_id, caption, status, generated_media, media_type)

                cursor.execute(sql, values)
                connection.commit()

            except mysql.connector.Error as err:
                return f"Error: {err}"

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    return "Data stored successfully"

if __name__ == '__main__':
    app.run(debug=True)
