from flask import Flask, request, jsonify
import datetime
from flaskext.mysql import MySQL
import time,json

mysql = MySQL()

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password@123'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/addpost', methods=['POST'])
def addpost():
    data = request.json
    q = 'insert into test_table set '
    for key, value in data.items():
       q += key+'='+'"'+value+'",'
    #query = str[:-1]
    
    query = q+'created='+'"'+str(datetime.datetime.now())+'"'
    conn = mysql.connect()
    cursor = conn.cursor()
    r = cursor.execute(query)
    conn.commit()
    print r
    print query
    return jsonify(data)

@app.route('/editpost', methods=['POST'])
def editpost():
    content = request.json
    d = json.JSONDecoder()
    fieldPlayerName = d.decode(content)
    print fieldPlayerName[0][0]
    return jsonify(content)

@app.route("/getpost")
def getpost():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from test_table")
    resultSet = cursor.fetchall()

    empList = []
    for emp in resultSet:
        dt = 'not avail'
        if emp[3] is not None:
            dt = datetime.datetime.strptime(str(emp[3]), '%Y-%m-%d %H:%M:%S')
            dt = str(dt)
        empDict = {
            'Id': emp[0],
            'Name': emp[1],
            'Month': emp[2],
            'date': dt}
        empList.append(empDict)

    output = [];
    list = {"list":empList}
    output.append(list)
    return json.dumps(output)



if __name__ == "__main__":
    app.run(debug=True)
