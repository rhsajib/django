import os
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()  


print(os.getenv('API_KEY'))
print(os.getenv('USER'))
print(os.getenv('PASSWORD'))
print(os.getenv('EMAIL'))


print(os.getenv('DOMAIN'))
print(os.getenv('ADMIN_EMAIL'))
print(os.getenv('ROOT_URL'))


# override .env variables
# In this case environment variables will override .env variables
load_dotenv(override=False)

USER='user'
print(os.getenv('USER'))


# remain .env variables unchanged
# In this case .env variables will override environment variables
load_dotenv(override=True)     # this is same as load_dotenv()  

USER='new-user'
print(os.getenv('USER'))


# dotenv_values
from dotenv import dotenv_values

config = dotenv_values(".env")    # it is a dictionary
print(config)                     
print(config['API_KEY'])


# all environment variables
print(os.environ)

# Iterating over all environment variables
for var in os.environ.items():
    print(var)
