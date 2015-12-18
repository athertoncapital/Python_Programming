def formula(conversion,input):
    if conversion == "inches_to_centimeters":
        input=float(input)
        input = input*2.54
    elif conversion =="centimeters_to_inches":
        input=float(input)
        input = input/2.54
    elif conversion =="Fahrenheit_to_Celsius":
        input=float(input)
        input = (input-32)/1.8
    elif conversion =="Celsius_to_Fahrenheit":
        input=float(input)
        input = 32 + (input*1.8)
    elif conversion =="bytes_to_kilobytes":
        input=float(input)
        input=input/1000
    elif conversion =="kilobytes_to_bytes":
        input=float(input)
        input=input/1000
    elif conversion =="bytes_to_megabytes":
        input=float(input)
        input=input/1000000
    elif conversion =="megabytes_to_bytes":
        input=float(input)
        input=input*1000000

    return input

