from flask import Flask, render_template, redirect, url_for, request
import pickle

model = pickle.load(open('lr_classifier.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    pred = ''
    return render_template('index.html', **locals())

@app.route('/pridict', methods = ['POST'])
def predict():
    if (request.method == 'POST'):
        p1 = float(request.form['p1'])
        p2= float(request.form['p2'])
        p3 = float(request.form['p3'])
        p4 = float(request.form['p4'])
        pred = model.predict([[p1, p2, p3, p4]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)