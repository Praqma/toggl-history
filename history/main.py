import argparse

from history import history
from history.toggl import Toggl
from utils.time import get_month_range

parser = argparse.ArgumentParser(description='Check the history of closed Toggl months')
parser.add_argument('token', help='Toggl user token')
parser.add_argument('workspace', help='Toggl workspace id')

def main():
    args = parser.parse_args()

    toggl = Toggl(args.token, args.workspace)

    months = get_month_range((2020, 9), (2020, 11))

    history.store(toggl, months)

    return 0
