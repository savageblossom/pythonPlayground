import re

def detect_phone(string=None):
    mobile_phone_re       = re.compile(r"\+\d+\(\d{3}\)\d{3}\-\d{2}\-\d{2}")
    stationar_phone_re    = re.compile(r"\d{3}\-\d{3}")

    if(string is None):
        print('Enter your phone number (e.g. +14(888)666-14-88, 622-142):')
        string = input()

    if(mobile_phone_re.search(string)):
        print("It's a mobile phone number!")
    elif(stationar_phone_re.search(string)):
        print("It's a stationar phone number!")
    else:
        print("It isn't either home or mobile phone number")

def detect_email(string=None):
    email_re = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    # print(email_re.findall(string))
    if(string is None):
        print('Enter your e-mail:')
        string = input()

    if(email_re.search(string)):
        print('Email you\'ve entered is VALID!')
    else:
        print('Email is INVALID!')

# detect_phone()
detect_email()

# detect_email('u.as-asd@gmail.com')
# detect_phone('609-404')
# detect_phone('+7(342)666-34-12')
