import requests
import pprint
from requests_ntlm import HttpNtlmAuth

sharepoint_user = 'hpe.sharepoint.com\\email'
sharepoint_password = 'passwd'
#Sharepoint URL should be the address of the site followed by /_api/web/
sharepoint_url = 'https://hpe.sharepoint.com/PATH/_api/web/'
sharepoint_contextinfo_url = 'https://hpe.sharepoint.com/teams/ArubaERT-AMS/_api/contextinfo'
sharepoint_listname = 'Name of the list'

headers = {
"Accept":"application/json; odata=verbose",
"Content-Type":"application/json; odata=verbose",
"odata":"verbose",
"X-RequestForceAuthentication": "true"
}
auth = HttpNtlmAuth(sharepoint_user, sharepoint_password)
r = requests.get(sharepoint_url+"Lists/getbytitle('%s')" % sharepoint_listname, auth=auth, headers=headers, verify=False)
list_Enumber = r.json()['d']['Employee ID']
list_itemcount = r.json()['d']['Employee ID']

##### Query all items from the list ######
list_cursor = 0
list_pagesize = 400
api_items_url = sharepoint_url + "Lists(guid'%s')/Items" % list_Enumber
concat_items = []

# We start by an initial request and then loop through pages returned by sharepoint
    cur_page = requests.get(api_items_url, auth=auth, headers=headers,verify=False)
concat_items += cur_page.json()['d']

while '__next' in cur_page.json()['d']['results']:
    cur_page = requests.get(cur_page.json()['d']['__next'], auth=auth, headers=headers, verify=False)
    concat_items += cur_page.json()['d']['results']


# Let's see the data we collected:
pprint.pprint(concat_items)
