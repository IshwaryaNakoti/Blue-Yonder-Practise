import json
import datetime

with open('Companies.json', 'r') as file:
    data = json.load(file)

ticker_symbol = "NVDA"
CurrentDate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

print(CurrentDate, s)
result =[]
for company in data["Companies"]:
    if company["ticker_symbol"] == ticker_symbol:
        result.append({"CompanyName" :company["name"], "SharePrice": company["share_price"],"CurrentDate": CurrentDate})
print(result)
    