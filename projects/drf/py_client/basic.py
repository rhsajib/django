import requests

# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'      # endpoint = 'http://127.0.0.1:8000/'
# remember local host is 'http' not 'https'

get_response = requests.post(endpoint, params={'product_id': 123})





# get_response = requests.get(endpoint) # http request
# get_response = requests.get(endpoint, params={'product_id': 123},json={'query': 'Hello World'})
# here params are query parameter
# here for params endpoint would be 'http://localhost:8000/api/?abc=123'


# it will print data in javascript syntex
# print(get_response.text)    # print raw text response
# print(get_response.status_code)

# it will print data in python dictionary format
print(get_response.json())
# print(get_response.json()['message'])


# HTTP request --> HTML
# REST API HTTP request --> JSON


"""

# I can pass my own data at endpoints json file
get_response = requests.get(endpoint, json={'query': 'Hello World'}) # http request
print(get_response.text)
print(get_response.json())
# look at data and json item inside the json file in the terminal after running it


# I can pass my own data with different name instead of json
# for instance 
# json={'query': 'Hello World'}
# data={'query': 'Hello World'}

get_response = requests.get(endpoint, data={'query': 'Hello World'}) # http request
print(get_response.text)
print(get_response.json()) # it will insert data inside 'form' key # also compare 'content type'

"""