from prometheus_client import Gauge,start_http_server
import random


g = Gauge('random_number', 'get a random number',['robin'])


start_http_server(9100)
while True:
	g.labels(mylabelname='robin').set(random.random()*1000)

