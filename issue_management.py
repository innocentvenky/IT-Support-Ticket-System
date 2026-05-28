# Priority Based Issue Management System

from ticket_management import *
from bug_tracking import *
from assign import *
for i in ticket_management:
    if i["issue_type"] == "hardware":
        i["priority"] = "High"
    elif i["issue_type"] == "software":
        i["priority"] = "Medium"
    else:
        i["priority"] = "Low"
print("---Issue Management System---")
high = 0
medium = 0
low = 0
print("\nTicket Reports\n")
for ticket in ticket_management:
    if i["priority"] == "High":
        high = high + 1
    elif i["priority"] == "Medium":
        medium = medium + 1
    else:
        low = low + 1
print("High Priority Issues  :", high)
print("Medium Priority Issues:", medium)
print("Low Priority Issues   :", low)
print("\nUnresolved High Priority Issues\n")
for i in ticket_management:
    if i["priority"] == "High" and i["status"] != "resolved":
        print("Ticket Id :", i["ticket_id"])
        print("Employee  :", i["emp_name"])
        print("Status    :", i["status"])
        print()
