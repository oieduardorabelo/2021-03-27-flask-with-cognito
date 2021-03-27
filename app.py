from flask import Flask, request
app = Flask(__name__)

@app.route('/cognito_redirect')
def cognito_redirect():
    try:
      code = request.args.get('code')
      return "Code is: " +  code
    except:
      return 'Hello, World!'
