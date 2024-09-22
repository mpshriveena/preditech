from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SECRET_KEY'] = 'secretkey'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = 'somesalt'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'

model = joblib.load('house_price_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    errors={}
    overall_quality = data['overall_quality']
    if (overall_quality<0):
        errors["error1"]="Provide positive Overall Quality"
    if (overall_quality>10):
        errors["error1"]='Overall Quality must be less than or equal to 10'
    gr_liv_area = data['gr_liv_area']
    if gr_liv_area<=200:
        errors["error2"]='Ground Living area must be greater than 200'
    garage_cars = data['garage_cars']
    if garage_cars<=0:
        errors["error3"]='Garage cars must be greater than 0'
    garage_area = data['garage_area'] 
    if garage_area<=100:
        errors["error4"]='Garage area must be greater than 100'
    total_bsmt_sf = data['total_bsmt_sf']  
    if total_bsmt_sf<=100:
        errors["error5"]='Total Basement must be greater than 100'
    if errors:
        return jsonify(errors), 404
    input_data = [[overall_quality, gr_liv_area, garage_cars, garage_area, total_bsmt_sf]]
    prediction = model.predict(input_data)
    return jsonify({'predicted_price': prediction[0]}), 200

if __name__ == '__main__':
    app.run(debug=True)