import multiprocessing
from gfss_parameter import app_name

bind = "10.15.15.14:5005"
workers = int(multiprocessing.cpu_count()*1.3) + 1
chdir = f"/home/gfss/{app_name}"
wsgi_app = "wsgi:app"
loglevel = 'info'
access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s"  "%(a)s"'
accesslog = "gfss-gunicorn-access.log"

error_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s"  "%(a)s"'
errorlog = "gfss-gunicorn-error.log"
proc_name = 'GFSS-ADMIN'
# Перезапуск после N кол-во запросов
max_requests = 0
# Перезапуск, если ответа не было более 60 сек
timeout = 60
# umask or -m 007
umask = 0x007
# Проверка IP адресов, с которых разрешено обрабатывать набор безопасных заголовков
forwarded_allow_ips = '10.51.203.165,10.51.203.167,127.0.0.1'
#preload увеличивает производительность - хуже uwsgi!
#preload_app = 'True'
