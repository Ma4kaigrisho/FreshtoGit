import requests
import json
import os
freshdesk_key = os.environ["FRESHDESK_API"]
github_key = os.environ["GITHUB_API"]
freshdesk_headers = { "Content-Type" : "application/json" }
github_headers = { 'Accept' : 'application/vnd.github+json', 'Authorization' : f'Bearer {github_key}', 'X-GitHub-Api-Version' : '2022-11-28'}
print("Enter username: ")
username= input()
print("Enter domain: ")
domain = input()
password = "x"

github_response = requests.get(f"https://api.github.com/users/{username}", headers = github_headers)
userdata = json.loads(github_response.text)
if not userdata["email"]:
  print("Enter email address: ")
  userdata["email"] = input();
contact_info = { "name" : username, "email" : userdata["email"]}
check_existance = requests.get(f"https://{domain}.freshdesk.com/api/v2/contacts?Contact={username}", auth=(freshdesk_key,""));
existing_user = json.loads(check_existance.text);
if existing_user:
  update_freshdesk = requests.put(f"https://domain.freshdesk.com/api/v2/contacts?Contact={username}", auth=(freshdesk_key, ""), data=json.dumps(contact_info), headers=freshdesk_headers)
else:
  r = requests.post("https://" + domain + ".freshdesk.com/api/v2/contacts", auth=(freshdesk_key, ""), data=json.dumps(contact_info), headers=freshdesk_headers);

#if r.status_code == 201:
  #print("Contact created successfully, the response is given below")
  #print(r.content)
 # print("Location Header : " + r.headers['Location'])
#else:
 # print("Failed to create contact, errors are displayed below,")
  #response = json.loads(r.content)
 # print(response["errors"])

  #print("x-request-id : " + r.headers['x-request-id'])
 # print("Status Code : " + str(r.status_code))