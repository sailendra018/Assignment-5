dict1 = {'Alice':85,'Bikash':95, 'Chinmay':76,'Dev': 88,'Elly':90}

a=input("Enter the Student's name: ")
b=dict1.get(a)
if (b == None):
    print("Student not found.")

else:
    print("{}'s marks: {}".format(a,dict1[a]) )

