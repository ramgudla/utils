import requests
from requests.auth import HTTPBasicAuth

job_name='my_custom_metrics_job'
instance_name='a.b.c.d:9000'
team_name='Team A'
metric_key='my_custom_metric'
metric_value='21.90'

response = requests.post('http://<pushgateway_host>:9091/metrics/job/{j}/instance/{i}/team/{t}'.format(j=job_name, i=instance_name, t=team_name), auth=HTTPBasicAuth('user', 'pwd'), verify=False, data='{k} {v}\n'.format(k=metric_key, v=metric_value))
print(response.status_code)
