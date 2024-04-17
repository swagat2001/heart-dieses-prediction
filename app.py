from flask import Flask,render_template,request
import pickle
import numpy as np
import sklearn
model = pickle.load(open('RandomForest_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')

def heart():
    return render_template("index.html")

@app.route('/Predict',methods=['POST'])

def heart_d_pred():
    male = int(request.form.get('male'))
    age= int(request.form.get('age'))
    currentSmoker = int(request.form.get('currentSmoker'))
    cigsPerDay = float(request.form.get('cigsPerDay'))
    BPMeds = float(request.form.get('BPMeds'))
    prevalentStroke = int(request.form.get('prevalentStroke'))
    prevalentHyp = int(request.form.get('prevalentHyp'))
    diabetes  = int(request.form.get('diabetes'))
    totChol = float(request.form.get('totChol'))
    sysBP = float(request.form.get('sysBP'))
    diaBP = float(request.form.get('diaBP'))
    BMI = float(request.form.get('BMI'))
    heartRate = float(request.form.get('heartRate'))
    glucose = float(request.form.get('glucose'))




    result = model.predict(np.array([male,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]).reshape(1,-1))
    if result[0]==0:
        result = 'Not'
    else:
        result = 'Yes'
    return render_template('index.html',result=result)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)