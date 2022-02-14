import argparse
import os
import sys

from netaddr import *
from reader import FileReader

def filter_data(parsed):
  ip_list = []
  for ip in parsed:
    is_valid = False
    try:
      ip_network = IPNetwork(ip)
      ip_list.append(ip_network)
      is_valid = True
    except:
      pass
    try:
      if(is_valid is not True):
        ip_address = IPAddress(ip)
        ip_list.append(ip_address)
    except:
      print(f'Error parsing {ip} into IP into IP address or network')
  return ip_list

def parse_file(file):
  parsed = []
  reader = FileReader()
  data = reader.read(file)
  results = data.split('\n')
  for r in results:
    if r.strip():
      parsed.append(r)
  return parsed


def options():
  parser = argparse.ArgumentParser(description = "A simple IP range summarizer")

  parser.add_argument("-p", "--path", type = str, nargs = 1,
                      metavar = "path", default = None,
                      help = "Open and read specified text file for IP range summarization.")
  args = parser.parse_args()
  if args.path != None:
    if os.path.exists(args.path[0]):
      return args.path[0]
  print(f'File {args.path[0]} does not exist, exiting program.')
  return sys.exit()

def main():
  test_file = options()
  parsed = parse_file(test_file)
  ip_list = filter_data(parsed)
  route_summarization = cidr_merge(ip_list)
  print(f'summarizing {test_file} to route {route_summarization}')
  for r in route_summarization:
    print(f'{str(r)}: {r.network} - {r.broadcast}')

if __name__ == "__main__":
  sys.exit(main())