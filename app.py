from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello():
  return 'hello from hello page'

@app.route('/api', methods=['GET', 'POST'])
def api():
  if request.method == 'POST':
    return request.form['name']
  
  if request.method == 'GET':
    return 'get request recieved'

if __name__ == '__main__':
  app.run(debug=True)
