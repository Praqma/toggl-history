from utils import time


def store(toggl, monthCount):
    day_in_month = time.get_previous_month()

    for i in range(monthCount):
        from_date, to_date = time.get_month_day_range(day_in_month)

        month_report = toggl.get_month_report(from_date, to_date)
        raw_csv, pretty_csv = month_report_to_csv(month_report)

        print("=== raw ===")
        print(raw_csv)
        print()
        print("=== pretty ===")
        print(pretty_csv)
        print()

        day_in_month = time.get_previous_month(day_in_month)


def month_report_to_csv(month_report):
    raw_header = "user_id;project_id;task_id;entry_id;duration;is_billable\n"
    pretty_header = "user;project;task;duration;is_billable"

    raw_lines = []
    pretty_lines = []
    for entry in month_report:
        raw_lines.append(f'{entry["uid"]};{entry["pid"]};{entry["tid"]};{entry["id"]};{entry["dur"]};{entry["is_billable"]}')
        pretty_lines.append(f'{entry["user"]};{entry["project"]};{entry["task"]};{entry["dur"]};{entry["is_billable"]}')

    raw_lines.sort()
    pretty_lines.sort()
    raw = raw_header + "\n".join(raw_lines)
    pretty = pretty_header + "\n".join(pretty_lines)

    return raw, pretty

