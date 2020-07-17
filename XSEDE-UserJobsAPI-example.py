from fair_research_login.client import NativeClient
from fair_research_login import JSONTokenStorage, ConfigParserTokenStorage
import requests

cli = NativeClient(client_id='32bb1e11-d7bb-4889-b3f1-ee0ed2a0fbae', token_storage=JSONTokenStorage('mytokens.json'), app_name='Scope Test')
tokens = cli.login(requested_scopes=['openid', 'profile', 'https://auth.globus.org/scopes/info.dyn.xsede.org/apis'])

print("Your access token for xsede_info_servers_oauth is:")
print(tokens["xsede_info_servers_oauth"]["access_token"])

endpoint = "https://info.xsede.org/wh1/glue2-views-api/v1/userjobs/"
access_token = tokens["xsede_info_servers_oauth"]["access_token"]
headers = {"Authorization": "Bearer {}".format(access_token)}

print("Your results from the XSEDE User Jobs API are:")
print(requests.get(endpoint, headers=headers).json())

