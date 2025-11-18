from fasc_api.client.service_client import ServiceClient

from init_demo_data import InitDemoData
api_client = InitDemoData.api_client
access_token = ServiceClient.get_access_token_value(api_client)

print('token = %s' % access_token)
