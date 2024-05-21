password = 8959
password_ =int(input("Enter the password:"))
if password_ == password:
    print("successfull executed...!!")
    print("Super correct your good punda neetha oru pepund /n sirkathada pepunda /n odayumda un manda /vilanguthada en ppunda ")
elif password_!=password:
    from twilio.rest import Client
    account_sid = 'AC7dd98e775ad9032f2b4e24da1b65b256'
    auth_token = '187762a1465f78e1759e0aba32104c86'
    Client = Client(account_sid,auth_token)
    to_number = '+919894277506'
    from_number = '+14423334147'
    call = Client.calls.create(
        twiml = '<Response><Dial>+918754859090</Response></Dial>',
        to = to_number,
        from_=from_number
    )
    print(call.sid)
