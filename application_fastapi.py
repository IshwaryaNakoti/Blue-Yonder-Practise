from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import json
import snowflake.connector

conn_params = {
    "account" : "rhtnrmg-ka34159",
    "user" : "ISHWARYANAKOTI",
    "password" : "Ishu@2541",
    "warehouse" : "COMPUTE_WH",
    "database" : "Dummy",
    "schema" : "Application"
}

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str = None
    price: float
    tax: float = None

# @app.get('/')
# def hello():
#     return "hello world"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if item_id is None:
        raise HTTPException(status_code = 404, detail = "User not found") #this method is usually used if we are fetching the data from database
    return {"item_id": item_id, "q":q}

@app.post('/saveData')
async def saveData(request: Request):
    try:
        data = await request.json()
        return data
    except Exception as e:
        return "I'm not a good developer"


@app.put('/updateData')
async def updateData(request: Request):
    try:
        Sample_data = await request.json()
        ticker_symbol = 'NVDA'
        for company in Sample_data['Companies']:
            if ticker_symbol == company['ticker_symbol']:
                company['name'] = "Nvida corp"
                with open('Companies.json', 'w') as file:
                    json.dump(Sample_data, file, indent=4)
                return [Sample_data,{"messsage" : f"Details for {ticker_symbol} updated Successfully"}]
        return {"Error" : f"Data for ticker symbol {ticker_symbol} not found"}, 404
    except Exception as e:
        return "Some Exception has occured"

@app.get('/checkData')
@app.post('/checkData')
async def checkData(request: Request):
    if request.method == 'GET':
        return {"message":"Get is choosen"}
    elif request.method == 'POST':
        data = "{'a':'b'}"
        return data

if __name__ == '__main__':
    try:
        conn = snowflake.connector.connect(**conn_params)
        cursor = conn.cursor()
        print("Connected to Snowflake")
    except Exception as e:
        print("Error connecting to Snowflake:", e)
    
    try:
        cursor.execute("INSERT INTO PERSONS (PERSONID,LASTNAME, FIRSTNAME) VALUES (1, 'NAKOTI', 'ISHWARYA')")
        cursor.execute("SELECT * FROM PERSONS")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error executing SQL query:", e)

