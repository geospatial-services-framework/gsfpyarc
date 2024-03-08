"""
Command-line utility for creating gptools from gsf
"""
import argparse
import sys

from urllib.parse import urlparse

from gsfarc.gptoolbox import GPToolbox
from gsf import Server

def create(args):
    """Creates a new gptoolbox"""
    print('Connecting to: ' + args.service_url)
    parsed_url = urlparse(args.service_url)
    parsed_netloc = parsed_url.netloc.split(':')
    host = parsed_netloc[0]
    port = parsed_netloc[1] if len(parsed_netloc) > 1 else '9191'

    split_path = parsed_url.path.split('/')
    if len(split_path) < 3:
        print('service name not found in url')
        sys.exit(1)

    service_name = split_path[2]
    print(service_name)
    server = Server(host, port)
    service = server.service(service_name)
    tasks = []
    for task_name in args.task_name:
        tasks.append(service.task(task_name))

    print('Initializing toolbox factory')
    print(tasks)
    toolbox = GPToolbox(tasks)

    output = args.output if args.output else service_name
    print('Creating toolbox: ' + output)
    toolbox.create_toolbox(output)

    print('Finished')

def parse_args(args):
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help='sub-command help')

    create_parser = subparser.add_parser('create',
        help='Creates an ESRI GPToolbox that wraps gsf tasks.')
    create_parser.add_argument('service_url', help='the service url e.g. http://host:9191/services/ENVI')
    create_parser.add_argument('task_name', nargs='+', help='a list of task names to wrap as gptools')
    create_parser.add_argument('--output', dest='output', help='the output file of the generated toolbox. Default is the service name')
    create_parser.set_defaults(func=create)

    # Parse the incoming args
    parsed_args = parser.parse_args(args)
    parsed_args.func(parsed_args)

def main():
    """Main command-line entry point.  Runs parse_args with arguments from the command-line.
    """
    parse_args(sys.argv[1:])

if __name__ == '__main__':
    main()