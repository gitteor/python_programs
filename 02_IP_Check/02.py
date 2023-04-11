import socket
import requests
import re

in_ip_addr = socket.gethostbyname(socket.gethostname())

reqst = requests.get("http://ipconfig.kr")
out_ip_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', reqst.text)[1]

# 내부 아이피
# print(in_ip_addr)
# 외부 아이피
print(out_ip_addr)