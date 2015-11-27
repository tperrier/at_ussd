'''
A translation of the Africas Talking USSD Tutorial (http://docs.africastalking.com/ussd)
from PHP to Python. This project creates a simple bottle web app.
'''
from libs.bottle import run, post, request, response as bottle_response, hook

# create the index route that only accepts post requests
@post('/')
def index():

    # Enable CORS (Cross Domain POST)
    bottle_response.headers['Access-Control-Allow-Origin'] = '*'

    # Reads the variables sent via POST from our gateway
    sessionId = request.POST.get('sessionId')
    serviceCode = request.POST.get('serviceCode')
    phoneNumber = request.POST.get('phoneNumber')
    text = request.POST.get('text')

    response = ""

    if text == "":
        # This is the first request. Note how we start the response with CON
        response  = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number"

    elif text == "1":
        # Business logic for first level response
        response = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"

    elif text == "2":
        # Business logic for first level response
        phoneNumber = "+254711XXXYYY"
        # This is a terminal request. Note how we start the response with END
        response = "END Your phone number is {}".format(phoneNumber)

    elif text == "1*1":
        # This is a second level response where the user selected 1 in the first instance
        accountNumber  = "ACC1001"
        # This is a terminal request. Note how we start the response with END
        response = "END Your account number is {}".format(accountNumber)

    elif text == "1*2":
        # This is a second level response where the user selected 1 in the first instance
        balance  = "KES 1,000"
        # This is a terminal request. Note how we start the response with END
        response = "END Your balance is {}".format(balance)

    # Return the response as an HTTP request
    return response

# Run the default bottle app
run(host='0.0.0.0',port='8080',debut=True,reloader=True)
