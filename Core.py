'''
import requests
import json
import urllib.request

# IP address to test
apiKey = 'cd443cee99fc491b8a49a7fd4db1a7c4'
ipur = 'https://api.ipgeolocation.io/ipgeo?apiKey='
ipurr = '&ip='
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print('Target IP Addr is : '+external_ip)
ip_address = external_ip
# URL to send the request to
request_url = ipur + apiKey + ipurr+ external_ip
# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
result  = json.loads(result)

IP=result['ip']
continent_code = result['continent_code']
continent_name = result['continent_name']
country_code = result['country_code2']

for key, value in result.items():
    print(key, ' : ', value)
'''