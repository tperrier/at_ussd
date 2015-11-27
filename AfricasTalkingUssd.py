from bottle import response, request

class AfricasTalkingUssd(object):

    def __init__(self,post):
        '''
        Creates and AfricasTalkingUssd object from the POST responce to the
        Africas Talking USSD gateway. http://docs.africastalking.com/ussd
        :param post (dict): POST values from Africas Talking. Should include:
            * 'sessionId'
            * 'serviceCode'
            * 'phoneNumber'
            * 'text'
        '''

        self.sessionId = post.get('sessionId')
        self.serviceCode = post.get('serviceCode')
        self.phoneNumber = post.get('phoneNumber')
        self.text = post.get('text')

        # Get array of all commands sent to far
        self.commands = self.text.split('*')
        self.last = self.commands[-1]

    def con(self,strfmt,**kwargs):
        return self.response('CON',strfmt,**kwargs)

    def end(self,strfmt,**kwargs):
        return self.response('END',strfmt,**kwargs)

    def response(self,prefix,strfmt,**kwargs):
        text = strfmt.format(**kwargs)
        return '{0} {1}'.format(prefix,text)

def make_menu(title='',items=None,limit=7,item_length=25):
    response = title
    if response:
        response += '\n'
    response += '\n'.join(['{0:d}. {1:s}'.format(idx+1,item[:item_length]) for idx,item in enumerate(items[:limit])])

    if len(items) > limit:
        response += '\n98. Next'

    return response,items[limit:]

def enable_cors(fn):
    '''
    Cross Domain access decorator
    '''
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors
