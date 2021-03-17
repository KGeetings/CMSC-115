# def is_sorted(stuff):    
#     for i in range(1,len(stuff)):
#         if stuff[i - 1] > stuff[i]:
#             return False
#         return True

# #def isSorted(stuff):
#     #return all(b >= a for a, b in 
#         #zip(stuff, stuff[1:]))

# #def isSorted(stuff):
#     #for index, item in enumerate(stuff):
#         #try:
#             #if item > stuff[index + 1]:
#                 #return False
#         #except IndexError:
#             #return True
# #all(l[i] <= l[i+1] for i in range(len(l)-1))

# lst = list(input("Enter list:"))
# lst = list(filter(' ', lst))
    
# if sorted(lst) == lst:
#     print("hello")

# print(lst)
# if is_sorted(lst) == False:
#     print("The list is sorted")
# elif isSorted(lst) == True:
#     print("The list is not sorted")
 

#test_list = input("Enter list:")
## printing original list  
#print ("Original list : " + str(test_list)) 
#test_list = [int(s) for s in test_list.split(' ')]
## using naive method to  
## check sorted list  
#flag = 0
#i = 1
#while i < len(test_list): 
    #if(test_list[i] < test_list[i - 1]): 
        #flag = 1
    #i += 1
      
## printing result 
#if (not flag) : 
    #print ("Yes, List is sorted.") 
#else : 
    #print ("No, List is not sorted.") 
    
# # # test_list = input("Enter list:")
# # # test_list = [int(s) for s in test_list.split(' ')]

# # # print(test_list)
# # # def isSorted(test_list):
# # #     i = 1
# # #     flag = 0
# # #     while i < len(test_list): 
# # #         if(test_list[i] < test_list[i - 1]): 
# # #             flag = 1
# # #         i += 1
# # #     return flag

# # # print(isSorted(test_list))
# # # if isSorted(test_list) == 1: 
# # #     print ("The list is sorted.") 
# # # else: 
# # #     print ("The list is not sorted.")

lst = input("Enter list:")
newLst=lst.split(" ")

def isSorted(lst):
	copyLst = lst[:]
	copyLst.sort()
	if copyLst == newLst:
		print("The list is already sorted.")
	else:
		print("The list is not sorted.")

isSorted(newLst)
