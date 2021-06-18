from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  users = [
      {'name': 'ケイスケ', 'age': 22},
      {'name': 'ダイスケ', 'age': 26},
      {'name': 'セイジ', 'age': 18},
  ]
  return render_template('users.html', users=users)

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')
