#Jason Glotzbach solution to 1.a:

print("****1.a answer:")
def wrong_add_function(arg1,arg2):
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      print('arg1 is currently' ,arg1)
      print('arg_2_sum is currently' ,arg_2_sum) 
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      print('arg_2_sum is now' ,arg_2_sum)
      print('arg1 is now' ,arg1) 
      print('arg1_index is now' ,arg1_index)
      print('we are making an error in the loop') 
      print(f"The correct answer for arg1 index {arg1_index} is supposed to be {arg1[arg1_index]} plus {arg2[arg1_index]}")
      arg1[arg1_index]=arg_2_sum 
      arg1_index+=1
   return arg1
   print(arg1) 

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)
print("****\n")



#Jason Glotzbach solution to 1.b:

print("****1.b answer:")
def correct_add_function(arg1,arg2):
   arg1_index=0
   arg2_index=0 
   while arg1_index < len(arg1):
      arg_sum = 0
      print('arg1 is currently' ,arg1)
      print('arg_sum is currently' ,arg_sum) 
      for arg2_elements in arg2:
         arg_sum = sum([arg1[arg1_index]+arg2[arg2_index]])
      print('arg_sum is now' ,arg_sum)
      print('arg1 is now' ,arg1) 
      print('arg1_index is now' ,arg1_index)
      print('arg2_index is now' ,arg2_index) 
      print(f"The correct answer for arg1 index {arg1_index} is supposed to be {arg1[arg1_index]} plus {arg2[arg1_index]}")
      arg1[arg1_index]=arg_sum 
      arg1_index+=1
      arg2_index+=1 
   return arg1
   print(arg1) 

arg1 = [1,2,3]
arg2 = [1,1,1]

correct_add_function(arg1, arg2)
print("****\n")



#Jason Glotzbach solution to 2.a:

print("****2.a answer:")
def correct_add_function(arg1,arg2):
   arg1_index=0
   arg2_index=0 
   while arg1_index < len(arg1):
      arg_sum = 0 
      for arg2_elements in arg2:
         arg_sum = sum([arg1[arg1_index]+arg2[arg2_index]])
      arg1[arg1_index]=arg_sum 
      arg1_index+=1
      arg2_index+=1 
   print(arg1)  

arg1 = [1,2,3]
arg2 = [1,1,1]

correct_add_function(arg1, arg2)
print("****\n")



#Jason Glotzbach solution to 2.b:

print("****2.b answer:")
def exception_add_function(arg1,arg2):
    arg1_index=0
    arg2_index=0 
    try: 
        while arg1_index < len(arg1):
            for element in arg1:
                if isinstance(arg1[arg1_index], int):
                    arg1_index+=1
                else: 
                    input_arg1 = arg1[arg1_index]
                    input_element1 = arg1_index
                    u = arg1[arg1_index] + 1
    except TypeError:
        print (f"Your input argument {input_arg1} at element {input_element1} of arg1 is not of the expected type. Please change this and rerun")
    else:    
        try: 
            while arg2_index < len(arg2):
                for element in arg2:
                    if isinstance(arg2[arg2_index], int):
                        arg2_index+=1
                    else: 
                        input_arg2 = arg2[arg2_index]
                        input_element2 = arg2_index
                        z = arg2[arg2_index] + 1
        except TypeError:
            print (f"Your input argument {input_arg2} at element {input_element2} of arg2 is not of the expected type. Please change this and rerun")
        else:
            arg1_index=0
            arg2_index=0
            while arg1_index < len(arg1):
                arg_sum = 0 
                for arg2_elements in arg2:
                    arg_sum = sum([arg1[arg1_index]+arg2[arg2_index]])
                arg1[arg1_index]=arg_sum 
                arg1_index+=1
                arg2_index+=1 
            return arg1   

arg1 = ["5",2,5]
arg2 = [1,1,1]

exception_add_function(arg1, arg2) 
print("****\n")


#Jason Glotzbach solution to 2.c:

print("****2.c answer:")
def correction_add_function(arg1,arg2):
        arg1_index=0
        arg2_index=0
        try: 
            while arg1_index < len(arg1):
                for element in arg1:
                    if isinstance(arg1[arg1_index], str):
                        arg1_index+=1
                    else: 
                        input_list_str1 = []
                        for element in arg1:
                            input_list_str1.append(str(element))
                        arg1 = input_list_str1 
        except IndexError:
            print('there was an error in the arg1 inputs, working to fix it')
            new_arg1 = list(map(str, arg1))
            print("new arg1 = ",new_arg1)
            wrong_add_function(new_arg1,arg2)
        try:    
            arg1_index=0
            arg2_index=0
            while arg2_index < len(arg2):
                for element in arg2:
                    if isinstance(arg2[arg2_index], str):
                        arg2_index+=1
                    else: 
                        input_list_str2 = []
                        for element in arg2:
                            input_list_str2.append(str(element))
                        arg2 = input_list_str2    
        except IndexError:
            print('there was an error in the arg2 inputs, working to fix it')
            new_arg2 = list(map(str, arg2))
            print("new arg2 = ",new_arg2)
            wrong_add_function(arg1,new_arg2)

def wrong_add_function(arg1,arg2):
   print("checking to see if all inputs are same type:") 
   arg1_check = all(isinstance(sub, type(arg1[0])) for sub in arg1[1:])
   arg2_check = all(isinstance(sub, type(arg2[0])) for sub in arg2[1:])
   print("arg1_check = ",arg1_check)
   print("arg2_check = ",arg2_check) 
   if arg1_check == 0:
       correction_add_function(arg1,arg2)
   elif arg2_check == 0:
       correction_add_function(arg1,arg2)
   else:
       if sum([type(i)==int for i in arg1])==len(arg1) and \
          sum([type(i)==int for i in arg2])==len(arg2):
             print("it looks like we have all integers")
             arg1_index=0
             while arg1_index < len(arg1):
                arg_2_sum = 0
                for arg2_elements in arg2:
                   arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
                arg1[arg1_index]=arg_2_sum  
                arg1_index+=1
             print(arg1)
       elif sum([type(i)==str for i in arg1])==len(arg1) and \
          sum([type(i)==str for i in arg2])==len(arg2):
             print("it looks like we have all strings")
             arg1_index = 0
             while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                   arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
             print(arg1)


arg_str_1=['1','2','3']
arg_str_2=['1','1',1]

wrong_add_function(arg_str_1,arg_str_2)
print("****\n")