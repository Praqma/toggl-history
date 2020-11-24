import argparse
import sys

from history import history
from history.toggl import Toggl

parser = argparse.ArgumentParser(description='Check the history of closed Toggl months')
parser.add_argument('token', help='Toggl user token')
parser.add_argument('workspace', help='Toggl workspace id')

def main():
    args = parser.parse_args()

    toggl = Toggl(args.token, args.workspace)

    history.store(toggl, 3)

    return 0
