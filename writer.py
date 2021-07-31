from google.cloud import bigquery
import os

credentials_path = './access/pythonbq.privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'angular-blog-14cef.ng_data.ng_sensors'

rows_to_insert = [
  {u'sensorName':'data-001', u'temperature': 88.0, u'humidity': 32.1},
  {u'sensorName':'data-002', u'temperature': 90.2, u'humidity': 34.0},
  {u'sensorName':'data-003', u'temperature': 89.9, u'humidity': 35.2},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
  print('New rows added')
else:
  print(f'errors while inserting rows: {errors  }')