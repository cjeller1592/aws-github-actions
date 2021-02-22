from minik.core import Minik
import requests

app = Minik()

@app.get('/')
def get_greetings():
    app.response.headers = {"Content-Type": "text/html; charset=utf-8"}

    return """    <html>
    <head>
        <title>Hello World!</title>
        <style>
            body {
            font-family: helvetica, arial, sans-serif;
            margin: 2em;
            }

            h1 {
            font-style: italic;
            color: #0072ce;
            }
        </style>
    </head>
    <body>
        <h1>Hello EAB</h1>
        <p>My name is CJ. I'd like to join the Cloud Ops Team!</p>
    </body>
    </html>"""

@app.get('/joke/{subject}')
def get_why(subject):
    # Get teh joke
    r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke = r.json()['joke']

    app.response.headers = {"Content-Type": "text/html; charset=utf-8"}

    return """
    <html>
    <head>
        <title>Hello World!</title>
        <style>
        body {
            font-family: helvetica, arial, sans-serif;
            margin: 2em;
            }

        h1 {
            font-style: italic;
            color: #0072ce;
            }
        </style>
    </head>
    <body>
        <h1>Want a joke about %s?</h1>
        <p>How about something else instead?</p>
        <p>%s</p>
    </body>
    </html>""" % (subject, joke)
