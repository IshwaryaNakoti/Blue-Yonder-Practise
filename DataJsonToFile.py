import json
import Company

data = Company.Sample_data


with open("Data.json", 'w') as file:
    # file.write(json.dumps(data))  ---converts into the string
    json.dump(data, file, indent = 4) #---stores like a dictionary only
with open("Data.json", 'r') as file:
    s= file.read()
    #print(json.loads(s)) ---if file.write is used
    print(s)