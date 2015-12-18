#asks for the starting day number and the length of your stay
number_time_string = input("What day is the day you are leaving (Type a number to represent the day: Monday types 1, Tuesday types 2, Wednesday types 3, Thursday types 4, Friday types 5, Saturday types 6, and Sunday types 0)? ")


length_time_string = input("After how many nights you have ftp be back? ")

number_time_int = int(number_time_string)
length_time_int = int(length_time_string)

result=(length_time_int+number_time_int)%7



print('The day you will be back= ',result)
