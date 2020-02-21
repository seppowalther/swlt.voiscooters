import requests

def get_otp_data():
    get_otp_data={
    "country_code": "DE",
    "phone_number": "1723910109"
    }
    return get_otp_data

def verify_otp_data(get_otp_token):
    verify_otp_data={
        "code": "280355",
        "token": get_otp_token
    }
    return verify_otp_data

def get_first_authToken_data(get_otp_token):
    get_first_authToken_data={
        "email": "seppowalther@mail.de",
        "token": get_otp_token
    }
    return get_first_authToken_data

def get_otp():
    print("testing")






def main():
    while(1):
        import pdb;pdb.set_trace()

if __name__ == "__main__":
    main()
