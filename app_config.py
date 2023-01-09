from gfss_parameter import using, app_name

if using.startswith('PROD'):
    BASE = f'/home/gfss/{app_name}'
    host = 'gfss'
    os = 'unix'
    debug_level = 2
    port = 5050
else:
    BASE = f'C:/Projects/{app_name}'
    os = '!unix'
    debug_level = 4
    host = 'localhost'
    port = 80

LOG_FILE = f'{BASE}/gfss-admin.log'
UPLOAD_PATH = f'{BASE}/reports'
debug = True
language = 'ru'
src_lang = 'file'
trace_malloc = False
move_at_once = False

print(f"=====> CONFIG. using: {using}, BASE: {BASE}, app_name: {app_name}")


