from flask import Flask
from flasgger import Swagger
import exchanges


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
swagger = Swagger(app)


@app.route("/average/<code>/<date>", methods=['GET'])
def avg(code, date):
    """Get average exchange rate for a day
    ---
    parameters:
      - name: code
        in: path
        type: string
        required: true
        description: 'Currency code'
      - name: date
        in: path
        type: string
        required: true
        description: 'Date in format YYYY-MM-DD'
    definitions:
      Average:
        type: object
        properties:
          avg:
            type: float
            items: '#/definitions/Value'
      Value:
        type: float
    responses:
      200:
        description: 'Successfully read average exchange rate'
        content:
          application/json:
            schema:
              $ref: '#/definitions/Average'
        examples:
          application/json: { 'avg': 4.0234 }
"""
    return exchanges.get_average_exchange_rate(code, date)


@app.route("/minmax/<code>/<number>", methods=['GET'])
def min_max(code, number):
    """Get min and max average exchange rates during N last days
    ---
    parameters:
      - name: code
        in: path
        type: string
        required: true
        description: 'Currency code'
      - name: number
        in: path
        type: string
        required: true
        description: 'Number of last days'
    definitions:
      Averages:
        type: object
        properties:
          min:
            type: float
            items: '#/definitions/Value'
          max:
            type: float
            items: '#/definitions/Value'
      Value:
        type: float
    responses:
      200:
        description: 'Successfully read min and max average exchange rates'
        content:
          application/json:
            schema:
              $ref: '#/definitions/Average'
        examples:
          application/json: { 'min': 4.0234, 'max': 5.9876 }
"""
    return exchanges.get_min_max_exchange_rates(code, number)


@app.route("/difference/<code>/<number>", methods=['GET'])
def diff(code, number):
    """Get max difference between the buy and ask rates during N last days
    ---
    parameters:
      - name: code
        in: path
        type: string
        required: true
        description: 'Currency code'
      - name: number
        in: path
        type: string
        required: true
        description: 'Number of last days'
    definitions:
      Difference:
        type: object
        properties:
          diff:
            type: float
            items: '#/definitions/Value'
      Value:
        type: float
    responses:
      200:
        description: 'Successfully read max difference rate
        content:
          application/json:
            schema:
              $ref: '#/definitions/Difference'
        examples:
          application/json: { 'max_diff': 0.0861 }
"""
    return exchanges.get_difference_between_buy_ask_rates(code, number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)