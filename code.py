import datetime as dt
import requests, json, sys, socket, warnings, os, time, base64

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

path = sys.argv[1]

# instantiate
config = ConfigParser()

# parse existing file
config.read(path)

# read values from a section
client_id = config.get('config', 'client_id')
client_secret = config.get('config', 'client_secret')
output_folder = config.get('config', 'output_folder')
#proxy = config.get('config', 'proxy')
#proxy_port = config.getint('config', 'proxy_port')

# Static variables
oauth2_url = "/oauth/token"
logs_url = "/api/v1/log_events"
base_url = "https://api.aperture.paloaltonetworks.com"
logfile_date_format = "%Y-%m-%d-%H"
#

# Code logic variables
access_token = "none"
last_logs = "none"
generation_time = dt.datetime.now()
expiration_time = dt.datetime.now()
#

# Code Functions
def getOAuth2(client_id, client_secret):
    global oauth2_url
    global base_url
    auth_key = "Basic " + (base64.b64encode((client_id + ":" + client_secret).encode('ascii'))).decode('utf-8')
    headers = {'Authorization': auth_key}
    data = {'grant_type': 'client_credentials', 'scope': 'api_access'}
    generation_time = dt.datetime.now()
    r = requests.post((base_url + oauth2_url), headers=headers, data=data)
    json_var = json.loads(r.text)
    expiration_date = generation_time + dt.timedelta(seconds=json_var['expires_in'])
    access_token = (json_var['access_token'])
    return json_var, expiration_date, generation_time

def get_logs(access_token):
    global logs_url
    global base_url
    token_new = "Bearer " + access_token
    headers = {'Authorization': token_new, 'Accept': 'application/json'}
    r = requests.get((base_url + logs_url), headers=headers)
    return r.text

def appendFile(content, filename):
        with open(filename, "a+") as f:
                f.write(content)
# Code

while True:
    if access_token == "none":
        access_token, expiration_time, generation_time = getOAuth2(client_id, client_secret)
    if expiration_time <= dt.datetime.now():
        access_token, expiration_time, generation_time = getOAuth2(client_id, client_secret)
    logs = get_logs(access_token['access_token'])
    if last_logs != logs:
        appendFile(("\n" + logs), (output_folder + "output-" + (dt.datetime.now().strftime(logfile_date_format)) + ".json"))
        last_logs = logs
