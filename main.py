import json

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Templates')


@app.route('/', methods=['GET', 'POST'])
def fetch_ex():
    return render_template('main.html',
                           The_title = 'Sample')


@app.route('/saveQuestions', methods=['GET', 'POST'])
def saveQuestions():
    if request.method == "POST":
        question = request.json['a']
        answer = request.json['b']
        return {"success": "saved sucessfully"}


# app.run(debug=True)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
