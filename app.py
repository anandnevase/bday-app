from flask import Flask
from flask import request
from flask import jsonify
from flask import json
import datetime
import sqlite3

from flask import g

app = Flask(__name__)
#userlist={"userlist":[]}

@app.route('/hello', methods=['GET'])
def get_userlist():
    if request.method == 'GET':
        myuserlist = query_db('select * from user')
        return jsonify({"userlist": myuserlist}),200

@app.route('/hello/<username>', methods=['GET','PUT'])
def hello_world(username):
    if request.method == 'GET':
        user_found = False
        user = query_db('select * from user where username = ?',(username,), one=True)
        if user is not None:
            if user["username"] == username:
                user_found = True
                dob = datetime.datetime.strptime(user["dateOfBirth"], '%Y-%m-%d')
               
                if check_dob_today(dob):
                    return display("Hello, %s! Happy Birthday!" %(user["username"]))
                else:
                    days = calculate_dates(dob)
                    return display("Hello, %s! Your birthday is in %s day(s)" %(user["username"], days))
        else:
            if user_found == False:
                return display("username %s not found" % (username)), 400
        
    if request.method == 'PUT':
        #check username contains only letters
        if not username.isalpha():
            return display("Username shoud contains only letters"), 400
        
        request_data = json.loads(request.data)
        
        if request_data!=None and request_data != {}:
            dob = request_data.get('dateOfBirth')
            if dob:
                #check date format YYYY-MM-DD
                if not validate_dob(dob):
                    return display("Incorrect data format, should be YYYY-MM-DD"), 400
                #check dateofbirth is less then todays date
                if datetime.datetime.strptime(dob, '%Y-%m-%d').date() >= datetime.date.today():
                    return display("Birth day should be less than equal to todays date: "+str(datetime.date.today())), 400
            else:
                return display("Request params are missing. Please pass dateOfBirth. E.g {'dateOfBirth': '1988-01-02'}"), 400

            user = query_db('select * from user where username = ?',(username,), one=True)
            print("PUT:: user:"+str(user))
            if user is None:
                query_db('insert into USER (username, dateOfBirth) values(?,?)',(username,dob,), insert_update=True)
                return display('username successfully added!'), 204
            else:
                query_db('update USER set dateOfBirth=? where username=?',(dob,username,),insert_update=True)
                return display('username successfully updated!'), 204
            #userlist['userlist'].append({'username': username, "dateOfBirth":dob})
        

def display(msg):
    return jsonify({"message":msg})

def validate_dob(date_text):
    is_date_valid = True
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        is_date_valid = False
    return is_date_valid

def check_dob_today(original_date):
    now = datetime.datetime.now()
    if now.day == original_date.day and now.month == original_date.month:
        return True
    return False

def calculate_dates(original_date):
    now = datetime.datetime.now()
    delta1 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime.datetime(now.year+1, original_date.month, original_date.day)
    days = (max(delta1, delta2) - now).days
    return days

DATABASE = './database/revolut.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('./database/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False, insert_update=False):
    con = get_db()
    con.row_factory = dict_factory
    cur = con.cursor()
    cur = cur.execute(query, args)
    if not insert_update:
        rv = cur.fetchall()
        cur.close()
        result= (rv[0] if rv else None) if one else rv
        print("Type:"+str(type(result)))
        return result
    else:
        con.commit()
    cur.close()
        
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

if __name__ == '__main__':
    try:
        init_db()
    except:
        print("DB already Exists!!")
    app.run(debug=True)