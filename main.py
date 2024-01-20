from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from smtpOperation import send_mail
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def rootpage():
    return 'This Project is made for checking tensorflow operation'


@app.get('/gift/')
async def predict(gift: str = Query(..., title="")):
    try:
        send_mail(text=gift)
        return "successful"
    except Exception as e:
        print('OPERATION FAILED FOR {}'.format(e))
        return "unsuccessful"
