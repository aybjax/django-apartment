# gmail smtp
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "gmail"
EMAIL_HOST_PASSWORD = 'your password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'send from gmail directly from django'

# django-q
Q_CLUSTER = {
    'name': 'DJANGO_APARTMENT_AWS_SQS_MESSAGE_BROKER',
    'recycle': 200,  # memory
    'workers': 4,  # cpu
    'timeout': None,  # time seconds spent before termination
    'ack_failures': True,  # failure good?
    'max_attempts': 1,  # for failed task
    'retry': None,  # seconds for finishing task to present again; > timeout
    'compress': True,
    'queue_limit': 2,
    'bulk': 5,
    'label': 'AWS SQS FOR DJANGO_Q',
    'sqs': {
        'aws_region': 'ap-northeast-1',  # optional
        'aws_access_key_id': 'access_key',  # optional
        'aws_secret_access_key': 'password'  # optional
    }
}

#  django-storage
AWS_ACCESS_KEY_ID = 'access_key'
AWS_SECRET_ACCESS_KEY = 'password'
AWS_STORAGE_BUCKET_NAME = 'bucket-name'