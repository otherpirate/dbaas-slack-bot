from os import getenv


DBAAS_URL = getenv('DBAAS_URL', 'http://127.0.0.1:8000')
DBAAS_USER = getenv('DBAAS_USER', 'dbaas_bot')
DBAAS_PASSWORD = getenv('DBAAS_PASSWORD', 'bot_pwd')
DBAAS_HTTPS_VERIFY = getenv('DBAAS_HTTPS_VERIFY', 'False').upper() == 'TRUE'


SLACK_TOKEN = getenv('SLACK_BOT_TOKEN')
SLACK_BOT_ID = getenv('SLACK_BOT_ID')
SLACK_HTTP_PROXIES = getenv('SLACK_HTTP_PROXY', None)
SLACK_HTTPS_PROXIES = getenv('SLACK_HTTPS_PROXY', None)
SLACK_PROXIES = None
if SLACK_HTTP_PROXIES or SLACK_HTTPS_PROXIES:
    SLACK_PROXIES = {}
    if SLACK_HTTP_PROXIES:
        SLACK_PROXIES['http'] = SLACK_HTTP_PROXIES
    if SLACK_HTTPS_PROXIES:
        SLACK_PROXIES['https'] = SLACK_HTTPS_PROXIES


DBAAS_SENTINEL_ENDPOINT = getenv('DBAAS_SENTINEL_ENDPOINT', 'redis:127.0.0.1:6379/0')
DBAAS_SENTINEL_ENDPOINT_SIMPLE = getenv('DBAAS_SENTINEL_ENDPOINT_SIMPLE')
DBAAS_SENTINEL_SERVICE_NAME = getenv('DBAAS_SENTINEL_SERVICE_NAME')
DBAAS_SENTINEL_PASSWORD = getenv('DBAAS_SENTINEL_PASSWORD')

REDIS_KEY_TTL = getenv('REDIS_KEY_TTL', 86400)  # 1 Day


API_ENDPOINT = getenv('API_ENDPOINT', 'http://127.0.0.1:5000')
