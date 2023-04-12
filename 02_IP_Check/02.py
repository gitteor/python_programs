import socket
import requests
import re

# 내부 아이피
# in_ip_addr = socket.gethostbyname(socket.gethostname())
in_ip_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_ip_addr.connect(("www.google.com", 443))
print(in_ip_addr.getsockname()[0])

# 외부 아이피
reqst = requests.get("http://ipconfig.kr")
out_ip_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', reqst.text)[1]
print(out_ip_addr)
