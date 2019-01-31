import os
from slackclient import SlackClient

clientID = 2868852952.316329619239
client_secret = 'ce77f69acb1fdbc92c85541c42b04ca4'
verification_token = 'o78UxMIhmbLgLEM7zvJtvDyr'

test_token = 'xoxp-2868852952-145784863250-316323958567-7bc80792806e97d685249a02dedd54e6'

try:
    slack_client = SlackClient(test_token)
except:
	slack_client.api_call(
      "chat.postMessage",
      channel="#wintersun-pixlites",
      text="slack token not working!"
    )

pixlites_down = []
response = []
send_it = False
hostname = "google.com"

ip_addresses = ['10.200.1.16',
'10.200.1.15',
'10.200.1.21',
'10.200.1.22',
'10.200.1.20',
'10.200.1.17',
'10.200.1.18',
'10.200.1.19',
'10.200.1.39',
'10.200.1.40',
'10.200.1.26',
'10.200.1.42',
'10.200.1.43',
'10.200.1.44',
'10.200.1.36',
'10.200.1.35',
'10.200.1.38',
'10.200.1.37',
'10.200.1.23',
'10.200.1.25',
'10.200.1.22',
'10.200.1.24',
'10.200.1.32',
'10.200.1.34',
'10.200.1.31',
'10.200.1.33',
'10.200.1.30',
'10.200.1.28',
'10.200.1.29',
'10.200.1.27',
'10.200.1.14',
'10.200.1.11',
'10.200.1.13',
'10.200.1.12',]
google_response = os.system("ping -c 1 " + hostname)
for ip in ip_addresses:
    response.append(os.system("ping -c 1 " + ip))


for index, resp in enumerate(response):
    if resp != 0:
        print ip_addresses[index]
        pixlites_down.append(ip_addresses[index])

#print response
if google_response == 0:
	google_status = 'Google ping works - internet is working!\n'
else:
	google_status = 'Google ping failed - internet may be down!\n'
if pixlites_down:
    pixlites_status = 'The following pixlite IP addresses are down: ' + str(pixlites_down)
    send_it = True
else:
    pixlites_status = 'All pixlites are up and running! '	
full_status = google_status + pixlites_status

if send_it:
    slack_client.api_call(
      "chat.postMessage",
      channel="#wintersun-pixlites",
      text=full_status +' :fire:'
    )


