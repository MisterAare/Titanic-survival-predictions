from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('bill_auth.pkl','rb'))

@app.route('/')
def home():
    return 'Welcome to Bill Authentication Page'

if __name__=="__main__":
   app.run(debug=True)