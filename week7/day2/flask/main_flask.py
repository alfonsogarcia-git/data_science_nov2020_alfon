from flask import Flask, request, render_template
from utils.functions import read_json
import json, os

# Mandatory
app = Flask(__name__)     # En este caso __name__ = __main__

# ---------- Flask functions ----------
@app.route("/")  # @ representa el decorador
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/c_json")
def create_json():
    return '{"clave":"valor", "clave_2":3}'

@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['id']
    return request.args

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
