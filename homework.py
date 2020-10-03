print("Robot: What's your name ?")
name = input('User: ')
print("Robot: Nice to meet you,", name)
print("Robot: What's your birthdate (dd/mm/yy) ?")
birthdate = input('User: ')
day, month, year = birthdate.split("/")
if int(year) > 30:
    year = '19' + year
else:
    year = '20' + year

birthdate = '/'.join([day, month, year])
print(birthdate)

isConvert = input("Robot: Do you want to convert the year to Buddhism year ?  (y/n): ")

if isConvert == 'y':
    bdYear = int(year) + 543
    print("Robot:", year, "-->", bdYear)
    print("Robot: Thank you to talk to me.")
else:
    print("Robot: Ok, Byeeeee~")


# github.com/adadesions/python-afternoon