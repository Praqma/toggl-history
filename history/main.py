import sys
import argparse

from history import history
from toggl.api_client import TogglClientApi

parser = argparse.ArgumentParser(description='Check the history of closed Toggl months')
parser.add_argument('token', help='Toggl user token')
parser.add_argument('workspace', help='Toggl workspace id')

def main():
    args = parser.parse_args()

    settings = {
        'token': args.token,
        'workspace_id': args.workspace,
        'user_agent': 'toggl-history'
    }

    client = TogglClientApi(settings)

    history.store(client, 3)

    return 0
