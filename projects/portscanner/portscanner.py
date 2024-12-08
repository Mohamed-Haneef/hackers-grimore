import argparse
import socket
from urllib.parse import urlparse

# Arguments section

parser = argparse.ArgumentParser(prog="portscanner", description='A Complete portscanner', epilog='Developed by @MohamedHaneef')

parser.add_argument('-u', '--url')
parser.add_argument('-i', '--ip')
parser.add_argument('-p', '--port', action='store_const')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-S', '--stealth', action='store_true')
parser.add_argument('-O', '--os_detection', action='store_true')
parser.add_argument('-o', '--save_output', action='store_true')

argument = parser.parse_args()

# Main Variables

target_url = argument.url
target_ip = argument.ip
port_scanning = argument.port
verbose_mode = argument.verbose
stealth_scan = argument.stealth
os_detection = argument.os_detection
save_output = argument.save_output


# print(target_url, target_ip, verbose_mode, stealth_scan, os_detection, save_output)

# Get URL Details

def process_url(url):
	url_details = urlparse(url)
	print(url_details)
	url_ip = socket.gethostbyname(url_details.hostname)
	url_port = url_details.port if url_details.port else None
	url_scheme = url_details.scheme if url_details.scheme else None
	return {'url_ip': url_ip, 'url_port': url_port, 'url_scheme': url_scheme}

if(target_url and target_ip):
	raise Exception ('Enter either URL or IP, you cannot use both')

if(target_url):
	url_result = process_url(target_url)
	print(url_result)
