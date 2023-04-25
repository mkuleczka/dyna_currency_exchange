In this project there are two versions of API created: Flask based and Swagger based.
To query operations you can use browser with <http_address> or run command curl <http_address>

Please see requirements.txt for environment needs (or run pip install -r requirements.txt)

=================================

Flask based API:


To start the server, run this command:

python3.10 app.py 


To query operation 1, use address:

http://localhost:8000//average/<currency_code>/<date>
  
example:
  
curl http://localhost:8000//average/usd/2023-02-06

As the output you will get json output:
  
{
  "avg": 4.3833
}


To query operation 2, use address:
  
http://localhost:8000//minmax/<currency_code>/<number_of_last_days>
  
example:
  
curl http://localhost:8000//minmax/usd/10

As the output you will get json output:
  
{
  "min": 4.1649,
  "max": 4.2713
}


To query operation 2, use address:
  
http://localhost:8000//difference/<currency_code>/<number_of_last_days>
  
example:
  
curl http://localhost:8000//difference/usd/10

As the output you will get a max difference between the buy and ask USD rate for 10 last days in json format
{
  "max_diff": 0.0854
}

  
When no data will be found (selected weekend or holiday or incorrect currency code or incorrect date format) you will get message:
  
404 Not Found

=================================
  
For swagger based API:

To start the server, run this command:
  
python3.10 swagger.py


To see apidocs use address:
  
http://localhost:8001/apidocs/
  
  

To query operation 1, use address:
  
http://localhost:8001//average/<currency_code>/<date>
  
example:
  
curl http://localhost:8001//average/usd/2023-02-06

As the output you will get json output:
  
{
  "avg": 4.3833
}


To query operation 2, use address:
  
http://localhost:8001//minmax/<currency_code>/<number_of_last_days>
  
example:
  
curl http://localhost:8001//minmax/usd/10

As the output you will get json output:
  
{
  "min": 4.1649,
  "max": 4.2713
}


To query operation 2, use address:
  
http://localhost:8001//difference/<currency_code>/<number_of_last_days>
  
example:
  
curl http://localhost:8001//difference/usd/10

As the output you will get a max difference between the buy and ask USD rate for 10 last days in json format:
  
{
  "max_diff": 0.0854
}

  
When no data will be found (selected weekend or holiday or incorrect currency code or incorrect date format) you will get message:
  
404 Not Found

=========================
  
There are also two simple tests:
  
python3.10 test_exchanges.py
