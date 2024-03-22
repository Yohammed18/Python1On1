import requests

r = requests.get('https://api.github.com')
# this should play 200 HTTP response if the request was successful
print('{}\n'.format(r))
# dir() function returns a list of valid attributes and methods associated with a given request
print(dir(r))
# to get a better understanding of the apy substance use the help func
# print(help(r))

# create a function that taskes a status code request and prompts the weather the request was received or rejected

def code_response(code):
    if code == 200:
        print('\n{} Response:\nRequest has been recevied!'.format(code))
    elif code == 404:
        print("\n{} Response:\nThe server cannot find the requested resource!!".format(code))
    
# create a response with a url that return a 404 repsonse. i.e. http://www.google.com/404
response_404 = requests.get('http://www.google.com/404')


code_response(r.status_code) # 202
code_response(response_404.status_code) # 404

