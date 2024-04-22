import unittest
import json
import datetime

with open('Companies.json', 'r') as file:
    SampleDate = json.load(file)

class testCompanyInfo(unittest.TestCase):
    def setUp(self):
        self.data = {
            "Companies" : [
                {
                    "ticker_symbol" : "NVDA", "name": "NVIDIA", "share_price" : 300.50
                },
                {
                    "ticker_symbol" : "MSFT", "name": "Microsoft", "share_price" : 150.75
                }
            ]
        }
        with open('CompaniesTest.json', 'w') as file:
            json.dump(self.data, file)
    
    def tearDown(self):
        import os
        os.remove('CompaniesTest.json')
    
    def test_get_company_info(self):
        expected_result = [{"CompanyName": "NVIDIA", "SharePrice": 700.9}]
        result = []
        for company in SampleDate["Companies"]:
            if company["ticker_symbol"] == "NVDA":
                result.append({"CompanyName" :company["name"], "SharePrice": company["share_price"]})
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()