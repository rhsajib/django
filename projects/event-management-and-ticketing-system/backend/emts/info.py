# settings.py

EMAIL_USE_TLS = True                             # Enable TLS encryption
EMAIL_HOST = 'smtp.gmail.com'                    # Replace with your SMTP server host
EMAIL_HOST_USER = 'rhsajib15@gmail.com'          # Replace with your email address
EMAIL_HOST_PASSWORD = 'password'                 # Replace with your email password
EMAIL_PORT = 587                                 # Replace with the SMTP server port

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# DEFAULT_FROM_EMAIL = 'your_email@example.com'     # Replace with your email address
