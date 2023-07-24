from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

def load_models():
    try:
        local_classifier = pickle.load(open('classifier.pickle', 'rb'))
        local_scaler = pickle.load(open('sc.pickle', 'rb'))
        return local_classifier, local_scaler
    except FileNotFoundError as e:
        raise FileNotFoundError("Error loading pickle files. Make sure 'classifier.pickle' and 'sc.pickle' exist in the current directory.")
    except Exception as e:
        raise Exception("Error loading models: " + str(e))

@app.route('/model', methods=['POST'])
def predict():
    try:
        local_classifier, local_scaler = load_models()
        request_data = request.get_json(force=True)
        age = request_data.get('age')
        salary = request_data.get('salary')

        if age is None or salary is None:
            return "Error: 'age' and 'salary' must be provided in the JSON request.", 400

        # Convert age and salary to float if necessary
        age = float(age)
        salary = float(salary)

        # Make prediction
        input_data = np.array([[age, salary]])
        pred_proba = local_classifier.predict_proba(local_scaler.transform(input_data))[:, 1]

        return "The prediction probability is {:.2f}".format(pred_proba[0]), 200
    except Exception as e:
        return "Error: {}".format(str(e)), 500

if __name__ == "__main__":
    app.run(port=8005, debug=True)
