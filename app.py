from flask import Flask, request
app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    result = eval(code)  # 🔴 This is vulnerable to code injection!
    return str(result)

@app.route('/')
def home():
    return "Welcome to the vulnerable app!"

if __name__ == '__main__':
    app.run(debug=True)
