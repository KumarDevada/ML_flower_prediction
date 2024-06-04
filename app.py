# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# model = pickle.load(open('iri.pkl', 'rb'))

# app = Flask(__name__)



# @app.route('/')
# def man():
#     return render_template('home.html')


# @app.route('/predict', methods=['POST'])
# def home():
#     data1 = request.form['a']
#     data2 = request.form['b']
#     data3 = request.form['c']
#     data4 = request.form['d']
#     arr = np.array([[data1, data2, data3, data4]])
#     pred = model.predict(arr)
#     return str(pred)


# # if __name__ == "__main__":
# #     app.run(debug=True)


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def man():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():
    data = request.get_json()  # Get JSON data from the request
    data1 = data['a']
    data2 = data['b']
    data3 = data['c']
    data4 = data['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return jsonify(pred.tolist())  # Return the prediction as JSON

# if __name__ == "__main__":
#     app.run(debug=True)















