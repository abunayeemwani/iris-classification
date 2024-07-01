from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('./model.sav', 'rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    result = ''
    if request.method == 'POST':
        sepal_length = float(request.form.get('sepal_length'))
        sepal_width = float(request.form.get('sepal_width'))
        petal_length = float(request.form.get('petal_length'))
        petal_width = float(request.form.get('petal_width'))
        
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
