from fastapi import FastAPI
from chromedriver.main import parser, driver


app = FastAPI()



@app.get("/")
def marks(object):
    url = "https://edu2.aues.kz/"
    url_transcript = "https://edu2.aues.kz/transcript?load=true&?"
    return parser(url, url_transcript, object)
