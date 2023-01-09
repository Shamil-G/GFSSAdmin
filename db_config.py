from gfss_parameter import using
from model.logger import log
#import redis

if using.startswith('PROD'):
    LIB_DIR = r'/home/pdd/instantclient_21_4'
    dsn = '192.168.20.64:1521/gfss'
else:
    LIB_DIR = r'C:\Shamil\instantclient_21_3'
    dsn = '192.168.20.64:1521/gfss'

username = 'shamil'
password = 'shamil'
encoding = 'UTF-8'
timeout = 60       # В секундах. Время простоя, после которого курсор освобождается
wait_timeout = 15000  # Время (в миллисекундах) ожидания доступного сеанса в пуле, перед тем как выдать ошибку
max_lifetime_session = 2800  # Время в секундах, в течении которого может существоват сеанс
pool_min = 4
pool_max = 20
pool_inc = 4
Debug = True


print(f"=====> DB CONFIG. using: {using}, LIB_DIR: {LIB_DIR}, DSN: {dsn}")
log.info(f"=====> DB CONFIG. using: {using}, LIB_DIR: {LIB_DIR}, DSN: {dsn}")


class SessionConfig:
    # secret_key = 'this is secret key qer:ekjf;keriutype2tO287'
    SECRET_KEY = 'this is secret key qer:ekjf;keriutype2tO287'
    if using.startswith('DEV'):
        SESSION_TYPE = "filesystem"
    else:
        SESSION_TYPE = "filesystem"
        #SESSION_TYPE = 'redis'
        #SESSION_REDIS = redis.from_url('redis://@10.15.15.11:6379')
    SESSION_USE_SIGNER = True
    # SESSION_REDIS = Redis(host='10.51.203.144', port='6379')
    # SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 36000
    # SQLALCHEMY_DATABASE_URI = f'oracle+cx_oracle://{username}:{password}@{dsn}'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    print(f"----------> TYPE SESSION: {SESSION_TYPE}")


