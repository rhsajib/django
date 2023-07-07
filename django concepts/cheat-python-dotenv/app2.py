import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

# Accessing a specific environment variable
print(type(os.environ))
api_key = os.environ['API_KEY']
print(f'API key: {api_key}')



config = {
    **dotenv_values('.env.development'),  # load shared development variables
    **dotenv_values('.env.secret'),    # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

print(config)




