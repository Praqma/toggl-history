from collections import defaultdict
from utils import time

def store(toggl, months):
    for day_in_month in months:
        from_date, to_date = time.get_month_day_range(day_in_month)

        # format
        month_report = toggl.get_month_report(from_date, to_date)
        collapsed_report = collapse_month_report(month_report)
        raw_csv, pretty_csv = collapsed_report_to_csv(collapsed_report)

        # save to some files for now
        raw_filename = f'{day_in_month.month}-raw.csv'
        print(f'Saving to {raw_filename}')
        raw_file = open(raw_filename, "w")
        raw_file.write(raw_csv)
        raw_file.close()

        pretty_filename = f'{day_in_month.month}-pretty.csv'
        print(f'Saving to {pretty_filename}')
        pretty_file = open(pretty_filename, "w")
        pretty_file.write(pretty_csv)
        pretty_file.close()


# FIXME: https://docs.python.org/3/library/itertools.html
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
            client=first_entry["client"],
            pid=first_entry["pid"],
            project=first_entry["project"],
            tid=first_entry["tid"],
            task=first_entry["task"],
            is_billable=first_entry["is_billable"],
            dur=duration,
            ids=",".join(str(id) for id in entry_ids),
        ))

    return collapsed_entries

# FIXME: https://docs.python.org/3/library/csv.html
def collapsed_report_to_csv(month_report):
    raw_header = "user_id;client;project_id;task_id;is_billable;duration;entry_ids\n"
    pretty_header = "user;client;project;client;task;is_billable;duration\n"

    raw_lines = []
    pretty_lines = []
    for entry in month_report:
        raw_lines.append(
            f'{entry["uid"]};{entry["client"]};{entry["pid"]};{entry["tid"]};{entry["is_billable"]};{entry["dur"]};{entry["ids"]}')
        pretty_lines.append(
            f'{entry["user"]};{entry["client"]};{entry["project"]};{entry["task"]};{"billable" if entry["is_billable"] else "non-billable"};{time.format_ms_as_hhmmss(entry["dur"])}')

    raw_lines.sort()
    pretty_lines.sort()
    raw = raw_header + "\n".join(raw_lines)
    pretty = pretty_header + "\n".join(pretty_lines)

    return raw, pretty
