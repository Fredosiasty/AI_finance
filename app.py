from flask import Flask, render_template, request, palm


api = "AIzaSyBcXAU-ZRyUPaW2joQOVmSqWXHW4awuhKY"
palm.configure(api_key=api)
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/financial_QA', methods=['GET', 'POST'])
def financial_QA():
    return render_template('financial_QA.html')

@app.route('/makersuite', methods=['GET', 'POST'])
def makersuite():
    q = request.form.get("q")
    r = palm.chat(prompt=q, **model)
    return render_template('makersuite.html', r=r.last)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction.html')

@app.route('/joke', methods=['GET', 'POST'])
def prediction():
    return render_template('joke.html')

if __name__ == '__main__':
    app.run()
