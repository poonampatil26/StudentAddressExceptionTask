from ProjectTaskStudent import *

class InvalidInput(Exception):
    def __init__(self,msg):
        self.msg=msg

def len_pincode(pincode):
    count=0
    while pincode>0:
        count+=1
        pincode=pincode//10
    return count


def add_pincode_check(pin):
    if len_pincode(pin)>6 or len_pincode(pin)<6:
        raise InvalidInput("Pincode should be 6 digits only")

    else:
        return pin

def check_pincode(pin):
    if any(pin in s1 for s1 in Addresslist)==False:
            raise InvalidInput("This city is not available please select Another pincode ")
    else:
        return pin
    


        
        

def check_marks(mark):
    if mark > 100 or mark <= 0:
        raise InvalidInput("Marks must not be less than zero or greater than 100")
    else:
        return mark


Addresslist=[]
studentlist=[]
while True:
    ch=int(input("----select operation----"\
                 "\n1.Address"\
                 "\n2.Student"\
                 "\n3.Exit"\
                 "\nEnter your choice for operation : "))
    if ch==1:
        while True:
            ch1=int(input("\n1.Create Address"\
                          "\n2.Update Address"\
                          "\n3.Delete Address"\
                          "\n4.Show Address"\
                          "\n5.Exit"\
                          "\nEnter your choice: "))
            if ch1==1:
                no_of_address=int(input("Enter no of cities u want to add : "))
                for i in range(no_of_address):
                    citylist=[]
                    while True:
                        try:
                            pin=add_pincode_check(int(input(f"Enter pincode of city {i+1} : ")))
                            break
                        except (ValueError,InvalidInput) as e:
                            print(e)
                    city=input(f"Enter city {i+1} : ")
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    citylist.append(a1.get_pincode())
                    citylist.append(a1.get_city())
                    print(citylist)
                    for i in Addresslist:
                        if citylist[0] in i:
                            print(citylist)
                            print("This pincode available already: ")
                    Addresslist.append(citylist)
                

            elif ch1==2:
                if len(Addresslist)==0:
                    print("No addresses Available ")
                else:
                    while True:
                        try:
                            pin=check_pincode(int(input("Enter pincode u want to change: ")))
                            print(pin)
                            break
                        except (InvalidInput) as e:
                            print(e)
                    for i in Addresslist:
                        if i[0]==pin:
                            new_city=input("Enter new city name: ")
                            i[1]=new_city
                    print(Addresslist)
            elif ch1==3:
                    while True:
                        try:
                            pin=check_pincode(int(input("Enter pincode: ")))
                            print(pin)
                            break
                        except (InvalidInput) as e:
                            print(e)
                    for i in Addresslist:
                        if i[0]==pin:
                            Addresslist.remove(i)

            elif ch1==4:
                for i in Addresslist:
                    print(i)

            elif ch1==5:
                break

            else:
                print("\n Wrong choice")
                          
                            
    elif ch==2:           
        while True:
            ch1=int(input("1.Create Student"\
              "\n2.Update Student"\
              "\n3.Delete Student"\
              "\n4.Show Student"\
            "\n5.Show student by descending marks "\
              "\n6.Exit"\
            "\nEnter your choice: "))
            if ch1==1:
                if len(Addresslist)==0:
                    citylist=[]
                    print("No cities available please add city first")
                    pin=add_pincode_check(int(input("Enter pincode of city : ")))
                    city=input("Enter city : ")
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    citylist.append(a1.get_pincode())
                    citylist.append(a1.get_city())
                    Addresslist.append(citylist)
                    print(f"\n{a1.get_pincode()} {a1.get_city()} added successfully")

                no_of_students=int(input("Enter no of student u want to add: "))
                for i in range(no_of_students):
                    students=[]
                    rn=int(input("Enter Roll no: "))
                    name=input("Enter Name: ")
                    while True:
                        try:
                            mark=check_marks(int(input("Enter Marks: ")))
                            break
                        except InvalidInput as e:
                            print(e)
                    while True:
                        try:
                            address=check_pincode(int(input("Enter pincode: ")))
                            break
                        except (InvalidInput) as e:
                            print(e)
                            
                    s1.set_rn(rn)
                    s1.set_name(name)
                    s1.set_marks(mark)
                    if any(address in s1 for s1 in Addresslist)==True:
                        for subarray in Addresslist:
                            if address in subarray:
                                position=Addresslist.index(subarray)
                                
                                s1.set_address(Addresslist[Addresslist.index(subarray)])
                    print(s1.get_address())
                    students.append(s1.get_rn())
                    students.append(s1.get_name())
                    students.append(s1.get_marks())
                    students.extend(s1.get_address())
                    studentlist.append(students)
                print(studentlist)
                    
            elif ch1==2:
                if len(studentlist)==0:
                    print("No students Available ")
                else:
                    rn=int(input("Enter roll no u want to update the data: "))
                    for i in studentlist:
                        if i[0]==rn:
                            print(f"\nCurrently Avaialble information of roll no {rn}","\n",i)
                            
                    while True:
                        ch2=int(input("----select operation for student info update----"\
                                     "\n1.change name"\
                                     "\n2.change marks"\
                                     "\n3.change address"\
                                     "\n4.Exit"\
                                     "\nEnter your choice for operation : "))
                        if ch2==1:
                            new_name=input("Enter New name: ")
                            for i in studentlist:
                                if i[0]==rn:
                                    i[1]=new_name
                                
                        elif ch2==2:
                            new_mark=int(input("Enter New marks: "))
                            for i in studentlist:
                                if i[0]==rn:
                                    i[2]=new_mark
                            
                        elif ch2==3:
                            
                            print("Currently available cities")
                            for i in Addresslist:
                                print(i)
                            while True:
                                try:
                                    new_address=check_pincode(int(input("Select pincode form Currently available cities for changing address: ")))
                                    break
                                except (InvalidInput) as e:
                                    print(e)
                           
                            for subarray in Addresslist:
                                if new_address in subarray:
                                    position=Addresslist.index(subarray)
                                    for i in studentlist:
                                        if i[0]==rn:
                                            add_new_address=Addresslist[position]
                                            print(add_new_address)
                                            i.pop()
                                            i.pop()
                                            i.extend([add_new_address])
                                    
                                

                            
                        elif ch2==4:
                            break

                        else:
                            print("Wrong Choice")
                                    
                            
                        

            elif ch1==3:
                if len(studentlist)==0:
                    print("No students Available ")
                else:
                    rn=int(input("\nEnter Roll no u want to Delete : "))
                    for i in studentlist:
                        if i[0]==rn:
                            studentlist.remove(i)
                            print(f"Deleted Successfully roll no {rn}")
            
                

            elif ch1==4:
                if len(studentlist)==0:
                    print("No students Available ")
                else:
                    for i in studentlist:
                        print(i)


            elif ch1==5:
                marks_list=[]
                for i in studentlist:
                    marks_list.append(i[2])
                    
                new_list=sorted(marks_list)
                print(new_list)
                
                for i in reversed(new_list):
                    for j in studentlist:
                        if i==j[2]:
                            print(j)

            elif ch1==6:
                break

            else:
                print("\n Wrong choice")
                
                
       
                
       
