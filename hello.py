
from flask import Flask, request, jsonify, redirect, url_for
app = Flask(__name__)
import calculations

################################# HOME API ##############################
@app.route('/')
def welcome():
    return 'Hello everyone, welcome to Flask session.'

################################# API WITH NAME ############################
@app.route('/curious')
def curious():
    return 'I am curious to learn the things about flask.'

################################ API WITH VARIABLE #########################
@app.route('/person/<name>')
def person(name):
    return 'Name of the person is ' + name

@app.route('/Pass/<int:numbers>')
def Pass(numbers):
    return 'The student has been passed in exam and marks are ' + str(numbers)

@app.route('/fail/<int:numbers>')
def fail(numbers):
    return 'The student has been failed in exam and marks are ' + str(numbers) 

@app.route('/Add')
def adds():
    input_data = request.form
    print('Input data is: ', input_data)

    a = int(input_data['a'])
    b = eval(input_data['b'])
    result = calculations.addition(a,b)
    return jsonify({'Result':f'Addition of {a} and {b} is {result}'})

@app.route('/result/<int:marks>')
def result(marks):
    result = ''
    if marks < 40:
        result = 'fail'
    else:
        result = 'Pass'
    return redirect(url_for(result, numbers=marks ))
    
    


if __name__ == '__main__':
    app.run(debug=True)