import logging
import click
from flask import Flask
from threading import Thread

app = Flask(__name__)
log = logging.getLogger('werkzeug')
app.logger.disabled = True
log.disabled = True

def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

@app.route('/')
def home():
    return "24/7 | PUT WEBSITE LINK INTO https://uptimerobot.com/"

def run():
  app.run(host='0.0.0.0',port=2021)

def keep_alive():
    t = Thread(target=run)
    t.start()
