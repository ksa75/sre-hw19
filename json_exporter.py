from prometheus_client.core import GaugeMetricFamily, InfoMetricFamily,Metric, REGISTRY
from prometheus_client import start_http_server
import json
import requests
import sys
import time

class JsonCollector(object):
  def __init__(self, endpoint):
    self._endpoint = endpoint
  def collect(self):
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))

    lat = GaugeMetricFamily('svc_iss_position_latitude', 'ISS_position_latitude')
    lat.add_metric(labels=[],value=response['iss_position']['latitude'],timestamp=response['timestamp'])    
    yield lat

    long = GaugeMetricFamily('svc_iss_position_longitude', 'ISS_position_longitude')
    long.add_metric(labels=[],value=response['iss_position']['longitude'],timestamp=response['timestamp'])    
    yield long    

    i = InfoMetricFamily('svc_iss_status', 'ISS_status')
    i.add_metric(labels=[],value={'message':response['message']},timestamp=response['timestamp'])
    yield i


if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2]))

  while True: time.sleep(1)
