from ticket_management import *

print("\n\n Name : DURGA SREE\n")
print("_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  ticket_management:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
print("_________________________________________________________________________________________")


print("\n Assign tickets to the Employees\n")
ticket=int(input("enter the ticket_id : "))
assign=input("enter the employee name to assign ticket : ")
for i in ticket_management:
	if i["ticket_id"]==ticket:
		i["emp_name"]=assign

print("\n\n_________________________________________________________________________________________")
print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
print("_________________________________________________________________________________________")
for i in  ticket_management:
	print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
print("_________________________________________________________________________________________")
 
print("\n Display employee-wise assigned tickets \n")   
employee_name=input("enter the employee name  : ")
for i in ticket_management:
	if i["emp_name"]==employee_name:
		print("\n\n_________________________________________________________________________________________")
		print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
		print("_________________________________________________________________________________________")
		print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
		print("_________________________________________________________________________________________")
print("\n Update Employee Ticket Workload \n")
employee_name = input("Enter employee name : ")
new_workload = int(input("Enter new workload : "))
for i in ticket_management:
	if i["emp_name"] == employee_name:
		i["workload"] = new_workload
		print("\n\n_________________________________________________________________________________________")
		print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
		print("_________________________________________________________________________________________")
		print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
		print("_________________________________________________________________________________________")

 
print("\n Generate Assignment Summary Report  By Employee Name \n")
name=input("Enter the employee name : ")
for i in ticket_management:
	if i["emp_name"] == name:
		print("\n\n_________________________________________________________________________________________")
		print("Ticket_id\temp_name\tissue_type\tissue_description\tstatus")
		print("_________________________________________________________________________________________")
		print(i["ticket_id"],"\t\t",i["emp_name"],"\t", i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"])
		print("_________________________________________________________________________________________")

      



        


      
        


	     