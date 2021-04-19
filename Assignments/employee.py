class Employee:
	def __init__(self, name, ID, department, jobTitle):
		self.__name = name
		self.__ID = ID
		self.__dept = department
		self.__job = jobTitle
	def setDepartment(self, department):
		self.__dept = department
	def setJobTitle(self, jobTitle):
		self.__job = jobTitle
	def getName(self):
		return self.__name
	def getID(self):
		return self.__ID
	def getDepartment(self):
		return self.__dept
	def getJobTitle(self):
		return self.__job
	def __str__(self):
		return "Name: " + self.__name + "\nID Number: " + str(self.__ID) + "\nDepartment: " + self.__dept + "\nJob Title: " + self.__job
	
susan = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
mark = Employee("Mark Jones", 39119, "IT", "Programmer")
joy = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
	
print(susan, end = "\n\n")
print(mark, end = "\n\n")
print(joy)