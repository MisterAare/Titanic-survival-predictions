from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('bill_auth.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():
    Variance = float(request.form['Variance'])
    Skewness = float(request.form['Skewness'])
    Curtosis = float(request.form['Curtosis'])
    Entropy = float(request.form['Entropy'])

    prediction = model.predict([[Variance, Skewness, Curtosis, Entropy]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Quality of Bill Authentication is {}'.format(output))
    

if __name__=="__main__":
   app.run(debug=True)