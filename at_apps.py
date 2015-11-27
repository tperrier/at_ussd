'''
Sample USSD apps running on the Africa's Talking Gateway using Bottle
(http://docs.africastalking.com/ussd)
'''
from bottle import Bottle, response, request
import AfricasTalkingUssd as at
import at_client
import re,random,json

app = Bottle()
app.mount('/client',at_client.client)
app.mount('/static',at_client.static)
CACHE = {}

# create the index route that only accepts post requests
@app.post('/')
def index():

    # Enable CORS (Cross Domain POST)
    response.headers['Access-Control-Allow-Origin'] = '*'

    ussd = at.AfricasTalkingUssd(request.POST)

    if ussd.text == "":
        # This is the first hit of the service so return the main menu
        menu,next_menu = at.make_menu('Simple USSD Test',[
            'Guess A Number',
            'Convert KSH',
            'Random Swahili Words',
            'My Phone Number'
        ])
        return ussd.con(menu)

    elif ussd.commands[0] == '1':
        return guessing_game(ussd)

    elif ussd.commands[0] == '2':
        return convert_ksh(ussd)

    elif ussd.commands[0] == '3':
        return text_length(ussd)

    elif ussd.commands[0] == '4':
        return ussd.end(ussd.phoneNumber)

def guessing_game(ussd):
    # Play a guessing game for numbers between 0 and 100 (inclusive)

    if len(ussd.commands) == 1:
        # This is first call to the guessing game. Set a rangom number and display start message
        CACHE[ussd.sessionId] = random.randint(0,100)
        return ussd.con("I'm thinking of a number between 0 and 100 (inclusive).\n\nCan you guess it?")

    guess = int(ussd.last)
    target = CACHE[ussd.sessionId]
    guesses = len(ussd.commands) - 1
    
    if guess < target:
        return ussd.con('Sorry, {} is not the number.\nMy number is higher.\n\nGuess count {}'.format(guess,guesses))
    elif guess > target:
        return ussd.con('Sorry, {} is not the number.\nMy number is lower.\n\nGuess count {}'.format(guess,guesses))
    elif guess == target:
        del CACHE[ussd.sessionId]
        return ussd.end('Congratulations!\n\nThe number was {}.\n\nYou guessed it in {} tries'.format(guess,guesses))

def convert_ksh(ussd):
    # Convert KSH into other currencies
    if len(ussd.commands) == 1:
        return ussd.con('Enter amount in KSH')
    ksh = float(ussd.commands[1])

    currencies = ['USD','EUR','ZAR']
    if len(ussd.commands) == 2:
        menu,next_menu = at.make_menu('Choose A Currence',currencies)
        return ussd.con(menu)

    currency = ussd.commands[2]
    if currency.isdigit():
        currency = currencies[int(currency)-1]
    currency = currency.upper()

    conversions = {'USD':0.0098,'EUR':0.0092,'ZAR':0.14}
    converted = ksh*conversions[currency]

    return ussd.end('{0:.2f} KSH\n=\n{1:.2f} {2}\n\nThanks for using USSD Converter'.format(ksh,converted,currency))

def text_length(ussd):
    # get an integer and return lisporium
    words = json.load(open('words.json'))
    if len(ussd.commands) == 1:
        return ussd.con('Enter a character length.\n\nEnter a negative number to stop.')
    char_count = int(ussd.last)

    if char_count <= 0:
        response_str = '\n'.join(['{0}. Chars {1}'.format(i+1,c) for i,c in enumerate(ussd.commands[1:])])
        response_str += '\n\n -- {} hops --'.format(len(ussd.commands))
        return ussd.end(response_str)

    response_str = ''
    while True:
        missing = char_count - len(response_str)
        if str(missing) in words.keys():
            response_str += random.choice(words[str(missing)])
            break
        elif len(response_str) > char_count:
            response_str = response_str[:char_count]
            break
        else:
            response_str += random.choice(words[random.choice(words.keys())]) + ' '

    return ussd.con(response_str)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080",debut=True,reloader=True)
