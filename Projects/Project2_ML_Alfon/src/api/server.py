from flask import Flask, request, render_template
from functions import read_json
import json, os

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
    return 'clean datasss json here'

@app.route('/predictions_json')
def get_predictions_json():
    f = open('../../reports/predictions.json')
    data = json.load(f)
    return data

@app.route("/get_predictions")
def get_predictions():
    return app.send_static_file('predictions_df.html')

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
