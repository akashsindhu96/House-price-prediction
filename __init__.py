from flask import Flask, jsonify, request
import numpy as np
#flask cors is needed to enable handling Cross Orgin Requests
from flask_cors import CORS, cross_origin

#importing load_model from keras to load the trained model
from tensorflow.keras.models import load_model

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = load_model('price_predictor_model.h5')

# model._make_predict_function()

#Simple function that takes some information about a house and returns the predicted price
@app.route('/predict', methods=["POST"])
@cross_origin()
def predict_price():
    data = request.json
    value = np.array([data['crim'],
                      data['zn'],
                      data['indus'],
                      data['chas'],
                      data['nox'],
                      data['rm'],
                      data['age'],
                      data['dis'],
                      data['rad'],
                      data['tax'],
                      data['ptratio'],
                      data['b'],
                      data['lstat']])
    print(type(value[0]))
    pred = model.predict(np.array([value], dtype='float64'))
    print(type(pred[0][0]))
    prediction = {'price':pred[0].tolist()}

    return jsonify(prediction)

if __name__ == "__main__":
        app.run()