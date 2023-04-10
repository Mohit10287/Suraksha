import flask
from flask import render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import pandas as pd
import pickle
from datetime import datetime
from sklearn.ensemble import GradientBoostingClassifier


app = flask.Flask(__name__, template_folder='Templates')

#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
#in my case password is null so i am keeping empty
app.config['MYSQL_DB'] = 'accident_severity'#database name

mysql = MySQL(app)
@app.route('/')  

#User Login   
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return(flask.render_template('login.html'))
    if flask.request.method == 'POST':
        msg=''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM userdetails WHERE username = % s and password = %s', (username, password,))
            result = cursor.fetchone()
            
        if result:
            return render_template('main.html', usernameins=username)
        else:
           msg = "Invalid Login details, kindly try again."
           return render_template('login.html', msg=msg)
       
#User registeration
@app.route('/registeruser', methods=['GET', 'POST'])
def registeruser():
    if flask.request.method == 'GET':
        return(flask.render_template('register.html'))
    if flask.request.method == 'POST':
        msg=''
        #applying empty validation
        if request.method == 'POST' and 'username' in request.form and 'role' in request.form and 'email' in request.form and 'phone' in request.form  and 'purpose' in request.form and 'password' in request.form:
            #passing HTML form data into python variable
            username = request.form['username']
            role     = request.form['role']
            email    = request.form['email']
            phone    = request.form['phone']
            purpose  = request.form['purpose']
            password = request.form['password']
            
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #query to check given data is present in database or no
        cursor.execute('SELECT * FROM userdetails WHERE username = % s and phonennumber = %s', (username, phone,))
        #fetching data from MySQL
        result = cursor.fetchone()
        if result:
            msg = 'User Details Already Exists! Please Login.'
            return render_template('register.html', msg=msg)
        else:
            #executing query to insert new data into MySQL
            cursor.execute('INSERT INTO userdetails VALUES (NULL, % s, % s, % s, % s, % s, % s, NULL)', (username, role, phone, email, purpose, password,))
            mysql.connection.commit()
            #displaying message
            msg = 'Registeration completed! Please login.'
            return render_template('login.html', msg=msg)  
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        
#Prediction
model = pickle.load(open('Model/accidentSeverityPredictor.pkl', 'rb'))
@app.route('/main', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        noofveh1 = int(flask.request.form['noofveh'])
        roveg1 = int(flask.request.form['roveh'])
        roadsurf1 = int(flask.request.form['roadsurf'])
        light1 = int(flask.request.form['light'])
        weather1 = int(flask.request.form['weather'])
        cclass1 = int(flask.request.form['cclass'])
        sex1 = int(flask.request.form['sex'])
        age1 = int(flask.request.form['age'])
        typeveg1 = int(flask.request.form['typeveh'])
        usernameins = flask.request.form['usernameins']
        place = flask.request.form['place']


        input_variables = pd.DataFrame([[noofveh1, roveg1, roadsurf1, light1, weather1, cclass1, sex1, age1, typeveg1]],
                                       columns=['Number of Vehicles', '1st Road Class', 'Road Surface','Lighting Conditions','Weather Conditions','Casualty Class','Sex of Casualty','Age of Casualty','Type of Vehicle'], dtype=float)
        prediction = model.predict(input_variables)[0]
                
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO accidentdetails VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s, %s, NULL, % s, % s)', (noofveh1, roveg1, roadsurf1, light1, weather1, cclass1,sex1,age1,typeveg1,prediction,usernameins,place,))
        mysql.connection.commit()
        
        refnum = cursor.lastrowid
        
        if prediction==1:
            prediction="Serious Accident"
        else:
            prediction="Slight Accident"
            
        if roveg1 == 0:
            roveg = 'A - Type'
        elif roveg1 == 1:
            roveg = 'A(M) - Type'
        elif roveg1 == 2:
            roveg = 'B - Type'
        elif roveg1 == 3:
            roveg = 'Motor way - Type'
        elif roveg1 == 4:
             roveg = 'Unclassified - Type'
             
        if roadsurf1 == 0:
            roadsurf = 'Dry'
        elif roadsurf1 == 1:
            roadsurf = 'Frost'
        elif roadsurf1 == 2:
            roadsurf = 'Flood'
        elif roadsurf1 == 3:
            roadsurf = 'Snow'
        elif roadsurf1 == 4:
             roadsurf = 'Wet'
             
        if roadsurf1 == 0:
            roadsurf = 'Dry'
        elif roadsurf1 == 1:
            roadsurf = 'Frost'
        elif roadsurf1 == 2:
            roadsurf = 'Flood'
        elif roadsurf1 == 3:
            roadsurf = 'Snow'
        elif roadsurf1 == 4:
             roadsurf = 'Wet'
             
        if light1 == 0:
            light = 'No street lighting'
        elif light1 == 1:
            light = 'Street lighting unknown'
        elif light1 == 2:
            light = 'Street lights present and lit'
        elif light1 == 3:
            light = 'Darkness'
            
        if weather1 == 0:
            weather = 'Fine without high winds'
        elif weather1 == 1:
            weather = 'Fog or mist – if hazardn'
        elif weather1 == 2:
            weather = 'Street lights present and lit'
        elif weather1 == 3:
            weather = 'Other'
        elif weather1 == 4:
            weather = 'Raining without high winds'
        elif weather1 == 5:
            weather = 'Raining with high winds'
        elif weather1 == 6:
            weather = 'Snowing without high winds'
        elif weather1 == 7:
            weather = 'Snowing with high winds'
        elif weather1 == 8:
            weather = 'Unknown'
            
        if cclass1 == 0:
            cclass = 'Driver'
        elif cclass1 == 1:
            cclass = 'Passenger'
        elif cclass1 == 2:
            cclass = 'Pedestrian'
        
        if sex1 == 0:
            sex = 'Female'
        elif sex1 == 1:
            sex = 'Male'
            
        
        if typeveg1 == 0:
            typeveg = 'Agri vehicle'
        elif typeveg1 == 1:
            typeveg = 'Bus'
        elif typeveg1 == 2:
            typeveg = 'Car'
        elif typeveg1 == 3:
            typeveg = 'Goods Vehicle'
        elif typeveg1 == 4:
            typeveg = 'Motorcycle'
        elif typeveg1 == 5:
            typeveg = 'Pedal cycle'
        elif typeveg1 == 6:
            typeveg = 'Other vehicle'
            
        now = datetime.now()
        accidentdate = now.strftime("%d/%m/%Y %H:%M:%S")
        
        cursor.execute('SELECT * FROM accidentdetails WHERE referencenumber = % s', (refnum, ))
        result = cursor.fetchone()
        username = result['user']
        
        cursor.execute('SELECT * FROM userdetails WHERE username = % s', (username, ))
        result = cursor.fetchone()
        phone = ''
        if result is not None:
            phone = result['phonennumber']
        
        return flask.render_template('main.html',
                                     userInput={'noofveh':noofveh1,
                                                     'roveg':roveg,
                                                     'roadsurf':roadsurf,
                                                     'light':light,
                                                     'weather':weather,
                                                     'cclass':cclass,
                                                     'sex':sex,
                                                     'age':age1,
                                                     'typeveg':typeveg,
                                                     'refnum': refnum,
                                                     'accidentdate':accidentdate,
                                                     'username':username,
                                                     'phone':phone,
                                                     'place':place,
                                                     },result=prediction, user=username)


@app.route('/accessories', methods=['GET', 'POST'])
def accessories():
    if flask.request.method == 'GET':
        return(flask.render_template('Accessories.html'))

@app.route('/AccidentPerYear', methods=['GET', 'POST'])
def AccidentPerYear():
    if flask.request.method == 'GET':
        return(flask.render_template('AccidentPerYear.html'))
        
@app.route('/DFAccidents', methods=['GET', 'POST'])
def DFAccidents():
    if flask.request.method == 'GET':
        return(flask.render_template('DFAccidents.html'))


@app.route('/OffendersVictims', methods=['GET', 'POST'])
def OffendersVictims():
    if flask.request.method == 'GET':
        return(flask.render_template('OffendersVictims.html'))
        
@app.route('/VehicleType', methods=['GET', 'POST'])
def VehicleType():
    if flask.request.method == 'GET':
        return(flask.render_template('VehicleType.html'))
    
@app.route('/visual', methods=['GET', 'POST'])
def visual():
    if flask.request.method == 'GET':
        return(flask.render_template('visual.html'))

@app.route('/mailservice', methods=['GET', 'POST'])
def mailservice():
    if flask.request.method == 'POST':
        
        user = flask.request.form['usernameget']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        if(len(user)>0 or user != ''):
            cursor.execute('SELECT * FROM accidentdetails WHERE user = % s', (user, ))
            result = cursor.fetchall();
        else:
            cursor.execute('SELECT * FROM accidentdetails')
            result = cursor.fetchall();
            return flask.render_template('mailservice.html', resultdata=result)
     
        return flask.render_template('mailservice.html', resultdata=result)
    
    if flask.request.method == 'GET':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accidentdetails')
        result = cursor.fetchall();
        return flask.render_template('mailservice.html', resultdata=result)
    
if __name__ == '__main__':
    app.run()
