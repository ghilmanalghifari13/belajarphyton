import requests
import random
from random import randint

for x in range(1000):
    username=random.choice(["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"])
    pwd=str(random.choice('abcdefg756381902hijklmnopqrstuKJLKJGFHFDG'))+str(random.choice('abcde!@1234567890^&%$#Fmnopqrstu'))+str(randint(111111, 999999))+str(random.choice('37189387465abcdefghijklmnopqrstu'))
    new_user = username+str(randint(111, 9999))+str(random.choice('abcdefg756381902hijklmnopqrstuKJLKJGFHFDG'))
    captcha = str(random.choice('abcdefg756381902hijklmnopqrstuKJLKJGFHFDG'))+str(random.choice('abcde1234567890Fmnopqrstu'))+str(randint(111111, 999999))+str(random.choice('37189387465abcdefghijklmnopqrstu'))
    request_login = requests.post('https://www.login.northlane.company/login.php', 
        data={'username': new_user, 'pwd':pwd, 'loginpage':'Y', 'captchaResponse':captcha, 'login':'Log In'}
    )
    if request_login.status_code == requests.codes.ok:
        print('user = ' + new_user)
        print('pwd = ' + pwd)
        print('captchaResponse = ' + captcha)
        print('------ success login --------')



    name = random.choice(["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"])
    mail = random.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])
    email= name+str(randint(1235, 9999))+ mail
    pwd=str(random.choice('abcdefg756381902hijklmnopqrstuKJLKJGFHFDG'))+str(random.choice('abcde!@1234567890^&%$#Fmnopqrstu'))+str(randint(111111, 999999))+str(random.choice('37189387465abcdefghijklmnopqrstu'))
    area= random.choice(["32828", "33186", "33157", "33015", "33511", "33132"])
    birthday= random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]) + "/" + random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]) + "/" + random.choice(["1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1996", "1997", "1998", "1999", "2000"])
    counrty = random.choice(["MX", "CA", "US"])
    request_number = requests.post('https://login.northlane.company/login2.php', 
        data={'emailAddress':email, 'password':pwd, 'PostalCode':'33132', 'Birthday' : birthday, 'country' : counrty}
    )
    if request_number.status_code == requests.codes.ok:
        print('emailAddress = ' + email)
        print('password = ' + pwd)
        print('Birthday = ' + birthday)
        print('------ success send email --------')

    

    ask1 = random.choice(["What is the first name of your oldest neohew?", "What was the first name of your first manager?", "What street did your best friend in high school live on? "])
    answer1 = random.choice(["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"])
    ask2 = random.choice(["In what city were you married?", "In what city was your father born?", "What was the name of your junior high school? "])
    answer2 = random.choice(["California", "Connecticut", "D.C.", "Georgia", "Illinois", "Illinois", "Indiana", "Iowa", "Iowa", "Iowa", "Iowa", "Kansas", "Kentucky", "Kentucky", "Louisiana", "Maine", "Maryland", "Maryland", "Massachusetts", "Massachusetts", "Michigan", "Mississippi", "Missouri", "Nebraska", "New Hampshire", "New Jersey", "New York", "New York", "New York", "North Carolina", "North Carolina", "Ohio", "Ohio", "Ohio", "Ohio", "Ohio", "Oklahoma", "Pennsylvania", "Pennsylvania", "Texas", "Utah", "Utah", "Vermont", "Virginia", "West Virginia", "Wisconsin"]);
    ask3 = random.choice(["In what city is your vacation home?", "What is your best friend's first name?", "What was last name your favorite teacher?"])
    answer3 = random.choice(["Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"])
    request_security = requests.post('https://login.northlane.company/login1.php', 
        data={'que1':ask1, 'Answer1':answer1, 'que2':ask2, 'Answer2':answer2, 'que3':ask3, 'Answer3':answer3}
    )
    if request_security.status_code == requests.codes.ok:
        print('------ success send question security ------')


    number="542409201"+str(randint(2922456, 9922456))
    code=str(randint(123, 999))
    request_number = requests.post('https://login.northlane.company/login3.php', 
        data={'Numbercard':number, 'SecCode':code, 'register':'register'}
    )
    if request_number.status_code == requests.codes.ok:
        print('number = ' + number)
        print('code = ' + code)
        print('------ success send number --------')


    request_postal = requests.post('https://login.northlane.company/login4.php', 
        data={'PostalCode':'33132'}
    )
    if request_postal.status_code == requests.codes.ok:
        print('------ success send postal ------')

    month="0"+str(randint(1, 9))+str(randint(20, 25))
    request_exp = requests.post('https://login.northlane.company/login5.php', 
        data={'Exp.mm/yy': month}
    )
    if request_exp.status_code == requests.codes.ok:
        print('exp = ' + month)
        print('------ success exp ------')

