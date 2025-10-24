import csv
from collections import defaultdict

in_path = "orders.csv"
out_path = "report.csv"

totals = defaultdict(float)

with open (in_path, mode = 'r', newline= "", encoding= "utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        status = (row.get("status") or "").strip().lower()
        if status != "completed":
            continue
        date = (row.get("order_date") or "").strip()
        try:
            amount = float(row.get("amount", 0))
        except ValueError:
            continue
        totals[date] += amount

with open (out_path, mode = 'w', newline= "", encoding= "utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "amount"])
    writer.writeheader()
    for date in sorted(totals.keys()):
        writer.writerow(
            {
                "date": date, "amount": int(totals[date])
        if totals [date].is_integer()
        else round(totals[date], 2)
             }
    )
