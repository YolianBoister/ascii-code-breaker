print("Type a number or type finish to finish")
flag = False
while flag == False:
    num = input("")
    if num == "finish":
        print("Program Finished")
        flag = True
    else:
        num = int(num)
        num_char = chr(num)
        print(num_char)
