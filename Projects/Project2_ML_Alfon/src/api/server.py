from flask import Flask, request, render_template
from functions import read_json
import json, os

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
    S = 'J53812814'
    token_id = request.args.get('token')
    return render_template('index.html', name=token_id)

    # if token_id == S:
    #     return render_template('json_page.html')
    # else:
    #     return 'Something went wrong, please check if token_id is correct'

@app.route("/get_predictions")
def get_predictions():
    return 'predictions'

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(os.path.dirname(os.getcwd()))
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # settings_file = os.path.dirname(os.getcwd()) + "/settings.json"
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

if __name__ == "__main__":
    main()