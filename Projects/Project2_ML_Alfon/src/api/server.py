from flask import Flask, request, render_template
from functions import read_json
import json, os
import cv2
from tensorflow.keras.models import load_model
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Mandatory
app = Flask(__name__)     # En este caso __name__ = __main__

# ---------- Flask functions ----------
@app.route("/")  # @ representa el decorador
def home():
    return app.send_static_file('greet.html')

@app.route("/verify")
def ask_token():
    return app.send_static_file('token_page.html') 

@app.route("/g_json")
def get_json():
    token_id = request.args.get('token')
    S = 'J53812814'
    if token_id == S:
        return app.send_static_file('json_choose.html')
    else:
        return 'Something went wrong, please check if token_id is correct'

@app.route('/clean_data_json')
def get_clean_data():
    f = open('../../reports/clean_data.json')
    return json.load(f)

@app.route('/predictions_json')
def get_predictions_json():
    f = open('../../reports/predictions.json')
    data = json.load(f)
    return data

@app.route("/get_predictions")
def get_predictions():
    return app.send_static_file('predictions_df.html')

@app.route("/predict_from_file") #, methods=['GET', 'POST'])
def predict_from_file():
    img_filename = request.args.get('img')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('../../data/chest_pneumonia')
    wd = os.getcwd()
    fol1 = ['train', 'test']
    fol2 = ['normal', 'pneumonia']
    for i in os.listdir(wd):
        if i in fol1:
            for j in os.listdir(i):
                if j in fol2:
                    if img_filename in os.listdir(i + '/' + j):
                        a = i[:]
                        b = j[:]
                        print('Found the file')
    os.chdir(wd + '/' + a + '/' + b)
    wd_n = os.getcwd()
    print('Updated directory:', wd_n)
    img = cv2.imread(wd_n + '/' + img_filename, 0)
    if img.shape != (291, 291):
        img = cv2.resize(img, dsize=(291, 291), interpolation= cv2.INTER_CUBIC)
    img = img.reshape(1, 291, 291, 1)
    model = load_model('../../../../models/model_pneu.h5')
    prediction = np.argmax(model.predict(img), axis=-1)
    code = {1: 'Healthy', 0: 'Bacterial', 2: 'Virus'}
    
    return f'Predicted label for image {img_filename} was {code[prediction[0]]}'

# @app.route("/predict_from_file2", methods=['POST'])
# def predict_from_file2():
#     img_filename = request.args.get('img2')
#     if request.method == ['POST']:
#         img = request.files['img2']
#     return img_filename

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(os.path.dirname(os.getcwd()))
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    settings_file = os.path.dirname(__file__) + os.sep + "/settings.json"
    # Load json from file 
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")

print('Current directory:', os.getcwd())


if __name__ == "__main__":
    main()
