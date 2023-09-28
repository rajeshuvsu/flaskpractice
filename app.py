## Create a simple flask application
from flask import Flask,render_template,request,redirect,url_for
## create the flask app

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to Flask Tutorial"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passsed and the score is:" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and the score is:" + str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        avg_marks = (maths + science + history)/3

        #return render_template('results.html',results = avg_marks)
        return render_template('results.html',results = avg_marks)

        result = ""
        if avg_marks >= 50:
           result = "success"
        else:
           result = "fail"

        #return redirect(url_for(result, score = avg_marks))
       


if __name__ =='__main__':
    app.run(debug = True) # when debug  = True server restarts when any changes made 
