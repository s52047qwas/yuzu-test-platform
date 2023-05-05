import os


if os.environ.get('ENV') == 'production':
    from .pro_setting import *
else:
    from .env_setting import *