import calendar
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
        totalResults = 1
        allResults = []

        print(f"requesting from {from_date} to {to_date}")
        while len(allResults) < totalResults:
            page = page + 1
            result = self.get_month_report_page(from_date, to_date, page)
            allResults.extend(result["data"])
            totalResults = result["total_count"]
            sys.stdout.write(f'received page {page} - requested {len(allResults)} out of {totalResults}\r')
            sys.stdout.flush()
        print()

        return allResults
