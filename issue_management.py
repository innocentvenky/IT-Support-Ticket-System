# Priority Based Issue Management System
# Tirumala Rao

from ticket_management import *
from bug_tracking import *
from assign import *

print("\n\n Name : TIRUMALA RAO\n")

# Assign default priority if missing

for i in ticket_management:
    if "priority" not in i:
        i["priority"] = "low"

high = 0
medium = 0
low = 0

print("________________________________________________________________________________")
print("Ticket_id\temp_name\t\tpriority\tstatus")
print("________________________________________________________________________________")

for i in ticket_management:

    print(i["ticket_id"], "\t\t", i["emp_name"], "\t\t", i["priority"], "\t\t", i["status"])

    if i["priority"] == "high":
        high = high + 1

    elif i["priority"] == "medium":
        medium = medium + 1

    else:
        low = low + 1

print("________________________________________________________________________________")

print("\n--- Priority Wise Report ---\n")

print("High Priority Issues   :", high)
print("Medium Priority Issues :", medium)
print("Low Priority Issues    :", low)

print("\n--- Filter Tickets By Priority ---\n")

priority = input("Enter priority (high/medium/low) : ")

print("________________________________________________________________________________________________")
print("Ticket_id\temp_name\t\tissue_type\tissue_description\t\tstatus\t\t\tpriority")
print("________________________________________________________________________________________________")

for i in ticket_management:

    if i["priority"] == priority:

        print(i["ticket_id"], "\t\t",
              i["emp_name"], "\t\t",
              i["issue_type"], "\t\t",
              i["issue_description"], "\t\t",
              i["status"], "\t\t",
              i["priority"])

print("________________________________________________________________________________________________")

print("\n--- Unresolved High Priority Issues ---\n")

print("________________________________________________________________________________")
print("Ticket_id\temp_name\t\tpriority\tstatus")
print("________________________________________________________________________________")

for i in ticket_management:

    if i["priority"] == "high" and i["status"].strip() != "resolved":

        print(i["ticket_id"], "\t\t",
              i["emp_name"], "\t\t",
              i["priority"], "\t\t",
              i["status"])

print("________________________________________________________________________________")
