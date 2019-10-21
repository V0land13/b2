import sentry_sdk
import os

from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="sentry ссылку сюда",
    integrations=[BottleIntegration()]
)

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Main page</title>
  </head>
  <body>
    <div class="container">
      <h1>This is main page</h1>
      <p>Below are 2 links to the Success page and the Error page</p>
      </br>
      <p><a href="/success">SUCCESS</a></p>
      <p><a href="/fail">FAIL</a></p>
    </div>
  </body>
</html>
"""
    return html

@route('/success')  
def success():  
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Success page</title>
  </head>
  <body>
    <div class="container">
      <h1>This is Success page</h1>
      </br>
      <p><a href="/">Main</a></p>
      <p><a href="/fail">FAIL</a></p>
    </div>
  </body>
</html>
"""
    return html

@route('/fail')  
def fail():  
    raise RuntimeError("There is an error!")
  
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
