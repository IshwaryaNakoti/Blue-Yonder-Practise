from flask import Flask, jsonify, request
from datetime import datetime
import json


company = Flask(__name__) #initialising flask app
company.json.sort_keys = False

# Sample_data = {
#     "name" : "Ishwarya",
#     "age" : 22,
# }
result =[]
with open ('Companies.json', 'r') as file:
    Sample_data = json.load(file)


@company.route('/getCompanyDetails/<ticker_symbol>', methods=['GET'])
def getCompanyDetails(ticker_symbol):
    currentDate = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    flag = 0
    for company in Sample_data["Companies"]:
        if ticker_symbol == company["ticker_symbol"]:
            flag = 1
            result.append({"CompanyName" :company["name"], "SharePrice": company["share_price"],"CurrentDate": currentDate})

    
    if flag:
        return jsonify(result)
    else:
        return f"Data for Ticker Symbol '{ticker_symbol}' is not present"


@company.route('/getData', methods = ['GET'])
def getData():
    return Sample_data

@company.route('/saveData', methods = ['POST'])
def saveData():
    data = result
    if data:
        try:
            with open("Data.json", 'w') as file:
                json.dump(data, file, indent=4)
            return jsonify({"message": "Data saved Successfully"})
        except Exception as e:
            return jsonify({"error": "str(e)"}), 500
    else:
        return jsonify({"error":"No data provided"}), 100
    
if __name__ == '__main__':
    company.run(debug=True)
