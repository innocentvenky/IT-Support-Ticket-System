from ticket_management import*
print("\n\n\n Name: Bhavya (task)\n\n")
print("_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  ticket_management:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])


new_bug={"ticket_id":3201,"emp_name":"Venkatesh","issue_type":"hardware","issue_description":"login problem","status":"open"}
ticket_management.append(new_bug)
ticket_management.append(new_bug)
print("\n\n Add New Bug  and asign to Venkatesh \n")
print("_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  ticket_management:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
print("\n\n update status on ticket_id ")
ticket=int(input("enter ticket_id : "))
ticket_status=input("enter status : ")
print("\n\n update status on ticket_id ",ticket)
for i in ticket_management:
	if i["ticket_id"]==ticket:
		i["status"]=ticket_status
print("_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  ticket_management:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])

print("\ndeleting duplicate ticket\n")
ticket_management.pop()
print("_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  ticket_management:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
print("\n generate bug tracking reports\n")   
status=input("enter the status : ")
d=[]
for i in ticket_management:
	if i["status"]==status:
		d.append(i)
print("_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  d:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])


		
 




