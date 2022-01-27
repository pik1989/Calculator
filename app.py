import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/_calculate')
def calculate():
    n1 = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    n2 = request.args.get('number2', '0')
    # validating the input data
    m = re.match(r'^\-?\d*[.]?\d*$', n1)
    n = re.match(r'^\-?\d*[.]?\d*$', n2)

    if m is None or n is None or operator not in '+-*/':
        return jsonify(result='Error!')

    if operator == '/':
        result = eval(n1 + operator + str(float(n2)))
        result = round(result,2)
    else:
        result = eval(n1 + operator + n2)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
