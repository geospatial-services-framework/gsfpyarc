"""
Command-line utility for creating gptools from gsf
"""
import argparse
import sys

# Python 3
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from gsfarc.gptoolbox import GPToolbox
from gsf import Server

parser = argparse.ArgumentParser(
    description='Creates an ESRI GPToolbox that wraps gsf tasks.')
parser.add_argument('service_url', help='the url of the gsf service')
parser.add_argument('task_name', nargs='+', help='a list of task names to wrap as gptools')
parser.add_argument('--output', dest='output', help='the output file of the generated toolbox. Default is the service name')

args = parser.parse_args()

print('Connecting to: ' + args.service_url)
parsed_url = urlparse(args.service_url)
parsed_netloc = parsed_url.netloc.split(':')
host = parsed_netloc[0]
port = parsed_netloc[1] if len(parsed_netloc) > 1 else '9191'

split_path = parsed_url.path.split('/')
if len(split_path) < 4:
    print('service name not found in url')
    sys.exit(1)

service_name = split_path[3]

server = Server(host, port)
service = server.service(service_name)
tasks = []
for task_name in args.task_name:
    tasks.append(service.task(task_name))

print('Initializing toolbox factory')
toolbox = GPToolbox(tasks)

output = args.output if args.output else service_name
print('Creating toolbox: ' + output)
toolbox.create_toolbox(output)

print('Finished')