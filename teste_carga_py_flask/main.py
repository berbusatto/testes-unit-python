from flask import *
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def go_home():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="api"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM name")

    myresult = mycursor.fetchall()
    return jsonify({
        "app": myresult
    })


if __name__ == '__main__':
    app.run(port=8888)
