# import pickle

# from flask import Flask, request, app, jsonify, url_for, render_template

# import numpy as np
# import pandas as pd

# # from sklearn.preprocessing import StandardScaler

# # # Define scaler in app.py
# # scaler = StandardScaler()


# # Use scaler in your code


# app=Flask(__name__)


# ##load the model
# regmodel=pickle.load(open('regmodel.pkl', 'rb'))

# @app.route('/')

# def home():
#     return render_template('home.html')

# @app.route('/predict_api', methods=['POST'])

# def predict_api():
#     data=request.json['data']
#     print(data)
#     print(np.array(list(data.values())).reshape(1,-1))
#     new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
#     output=regmodel.predict(new_data)
#     return jsonify(output[0])

# if __name__=="__main__":
#     app.run(debug=True, port=5001)    






           
# import pickle
# from flask import Flask, request, jsonify, render_template
# import numpy as np

# app = Flask(__name__)

# # Load the model
# regmodel = pickle.load(open('regmodel.pkl', 'rb'))

# # Load the scaler
# scaler = pickle.load(open('scaler.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data = request.json['data']
#     print(data)
#     # Transform the input data using the scaler
#     new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
#     # Make prediction using the loaded model
#     output = regmodel.predict(new_data)
#     return jsonify(output[0])

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)





import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))



if __name__=="__main__":
    app.run(debug=True)
   
     