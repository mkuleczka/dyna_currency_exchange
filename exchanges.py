from urllib.request import urlopen
import json


def get_data_nbp(address: str) -> [dict, str]:
    try:
        response = urlopen(address)
        data = json.loads(response.read())
    except Exception as e:
        data = str(e.code) + " " + e.reason
    return data


def get_average_exchange_rate(code: str, date: str) -> [str, dict]:
    url = "http://api.nbp.pl/api/exchangerates/rates/a/{}/{}/?format=json".format(code, date)
    data = get_data_nbp(url)
    if isinstance(data, str):
        return data
    else:
        avg_ex_rate = {'avg': data['rates'][0]['mid']}
        return avg_ex_rate


def get_min_max_exchange_rates(code: str, number: str) -> [str, dict]:
    url = "http://api.nbp.pl/api/exchangerates/rates/a/{}/last/{}/?format=json".format(code, number)
    data = get_data_nbp(url)
    if isinstance(data, str):
        return data
    else:
        avg_ex_rates = [data['rates'][i]['mid'] for i in range(int(number))]
        min_max = {'min': min(avg_ex_rates), 'max': max(avg_ex_rates)}
        return min_max


def get_difference_between_buy_ask_rates(code: str, number: str) -> [str, dict]:
    url = "http://api.nbp.pl/api/exchangerates/rates/c/{}/last/{}/?format=json".format(code, number)
    data = get_data_nbp(url)
    if isinstance(data, str):
        return data
    else:
        diff_buy_ask_rates = {'max_diff': max([round((data['rates'][i]['ask']-data['rates'][i]['bid']), 4)\
                                         for i in range(int(number))])}
        return diff_buy_ask_rates
