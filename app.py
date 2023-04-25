from flask import Flask
import exchanges


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/average/<code>/<date>", methods=['GET'])
def avg(code, date):
    return exchanges.get_average_exchange_rate(code, date)


@app.route("/minmax/<code>/<number>", methods=['GET'])
def min_max(code, number):
    return exchanges.get_min_max_exchange_rates(code, number)


@app.route("/difference/<code>/<number>", methods=['GET'])
def diff(code, number):
    return exchanges.get_difference_between_buy_ask_rates(code, number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)