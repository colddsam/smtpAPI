from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from smtpOperation import send_mail
from birthdayOperation import BirthDayInfo

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


@app.get('/mail/')
async def predict(text: str = Query(..., title=""),sender:str=Query(...,title="")):
    try:
        send_mail(text=text,sender=sender)
        return "successful"
    except Exception as e:
        print('OPERATION FAILED FOR {}'.format(e))
        return "unsuccessful"
    
@app.get('/birthday')
async def birthday():
    try:
        bthInfo=BirthDayInfo()
        name=bthInfo.birthdayName()
        return {
            "name":name
        }
    except Exception as e:
        print('OPERATION FAILED GETTING BIRTHDAY INFO {}'.format(e))
        return {
            "name":"Unknown"
        }