import requests
r=requests.get("http://tmc.flybycloud.com/auth/login")
print(r.status_code)
print(False)
