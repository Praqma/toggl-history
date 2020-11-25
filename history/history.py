from collections import defaultdict
from utils import time

def store(toggl, monthCount):
    day_in_month = time.get_previous_month()

    for _ in range(monthCount):
        from_date, to_date = time.get_month_day_range(day_in_month)

        month_report = toggl.get_month_report(from_date, to_date)
        collapsed_report = collapse_month_report(month_report)
        raw_csv, pretty_csv = collapsed_report_to_csv(collapsed_report)

        print("=== raw ===")
        print(raw_csv)
        print()
        print("=== pretty ===")
        print(pretty_csv)
        print()

        day_in_month = time.get_previous_month(day_in_month)


def collapse_month_report(month_report):
    grouped_entries = defaultdict(list)
    for entry in month_report:
        key = (entry["uid"], entry["pid"], entry["tid"], entry["is_billable"])
        grouped_entries[key].append(entry)

    collapsed_entries = []
    for entries in grouped_entries.values():
        first_entry = entries[0]

        entry_ids = list(map(lambda e: e["id"], entries))
        entry_ids.sort()
        duration = sum(map(lambda e: int(e["dur"]), entries))

        collapsed_entries.append(dict(
            uid=first_entry["uid"],
            user=first_entry["user"],
            pid=first_entry["pid"],
            project=first_entry["project"],
            tid=first_entry["tid"],
            task=first_entry["task"],
            is_billable=first_entry["is_billable"],
            dur=duration,
            ids=",".join(str(id) for id in entry_ids),
        ))

    return collapsed_entries


def collapsed_report_to_csv(month_report):
    raw_header = "user_id;project_id;task_id;is_billable;duration;entry_ids\n"
    pretty_header = "user;project;task;is_billable;duration\n"

    raw_lines = []
    pretty_lines = []
    for entry in month_report:
        raw_lines.append(
            f'{entry["uid"]};{entry["pid"]};{entry["tid"]};{entry["is_billable"]};{entry["dur"]};{entry["ids"]}')
        pretty_lines.append(
            f'{entry["user"]};{entry["project"]};{entry["task"]};{"billable" if entry["is_billable"] else "non-billable"};{time.format_ms_as_hhmmss(entry["dur"])}')

    raw_lines.sort()
    pretty_lines.sort()
    raw = raw_header + "\n".join(raw_lines)
    pretty = pretty_header + "\n".join(pretty_lines)

    return raw, pretty
