from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def api():
    import pandas as pd
    # Getting url to import data
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    df = pd.read_csv(url)
    # Constraints of group C
    mask = (df['location'] == "Spain") | (df['location'] == "Iran") | (df['location'] == "Brazil") | (df['location'] == "Mexico") | (df['location'] == "Netherlands")
    # Changing date series to datetime fromat
    df['date'] = pd.to_datetime(df['date'])
    a = df[mask].groupby('date').mean()[['total_cases']]
    a = a.rename(columns={"total_cases": "t_c_avg"})
    a = a.to_json
    return jsonify(a)

if __name__ == '__main__':
    app.run()