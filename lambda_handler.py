from minik.core import Minik
import requests

app = Minik()

@app.get('/')
def get_greetings():
    app.response.headers = {"Content-Type": "text/html; charset=utf-8"}

    return """
    <html>
    <head>
        <title>Hello EAB!</title>
    </head>
    <body>
        <h1>Hello EAB!</h1>
        <p>My name is CJ. I'd like to join the Cloud Ops Team</p>
    </body>
    </html>"""

@app.get('/why/{reason}')
def get_why(reason):
    # Get teh joke
    r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke = r.json()['joke']

    app.response.headers = {"Content-Type": "text/html; charset=utf-8"}

    return """
    <html>
    <head>
        <title>Hello EAB!</title>
    </head>
    <body>
        <p>Want a joke about %s?</p>
        <p>How about something else instead?</p>
        <p>%s</p>
    </body>
    </html>""" % (reason, joke)
