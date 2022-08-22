import http.client


conn = http.client.HTTPConnection("localhost:8000")
conn.request("GET", "/")
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data.decode("utf-8"))
