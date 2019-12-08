import requests
import json
import socket
import time
import sys
import os

def main():
    # open config.json
	with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json", 'r') as cf:
		config = json.load(cf)
	
	device_info = socket.gethostbyname_ex(socket.gethostname() + ".local")
	info_txt = \
		"{}\n\"{}\" is Connected :globe_with_meridians:\nIP Address: {}"    \
		.format(time.asctime(), device_info[0], device_info[2])

	requests.post(config["slack"]["wh_url"], data=json.dumps({"text":info_txt}))


if __name__ == "__main__":
	main()
