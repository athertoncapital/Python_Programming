current_time = input("What is the current time (in hours)? ")
waiting_time = input("How many hours do you have to wait? ")
#convert stri to int
current_time_int = int(current_time)
waiting_time_int = int(waiting_time)

hours = current_time_int + waiting_time_int

result = hours % 24

print("Your result= ",result)
