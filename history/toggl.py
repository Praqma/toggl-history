import sys

from toggl.TogglPy import Toggl as TogglClient


class Toggl(object):
    def __init__(self, token, workspace):
        self.client = TogglClient()
        self.workspace = workspace

        self.client.setAPIKey(token)
        self.client.setUserAgent('toggl-history')


    def get_month_report_page(self, from_date, to_date, page):
        request = {
            "workspace_id": self.workspace,
            "since": from_date.isoformat(),
            "until": to_date.isoformat(),
            "page": page
        }

        return self.client.getDetailedReport(request)


    def get_month_report(self, from_date, to_date):
        page = 0
        expectedResultCount = 1
        currentResults = []

        print(f"requesting from {from_date} to {to_date}")
        while len(currentResults) < expectedResultCount:
            page = page + 1
            result = self.get_month_report_page(from_date, to_date, page)
            currentResults.extend(result["data"])
            expectedResultCount = result["total_count"]
            sys.stdout.write(f'received page {page} - requested {len(currentResults)} out of {expectedResultCount}\r')
            sys.stdout.flush()
        print()

        return currentResults
