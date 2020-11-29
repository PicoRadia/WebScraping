import requests
import json

url = "https://www.ws.public.oatms.tms.aws.toyota.com/v1/pe/calculations/110?clientId=cc6b26e89b334ff782cad81203962c13&x-api-key=eI64ESPBv39pqVDblhXZ56tGw96izAPP4F5P42Th&content-type=application/json&user-agent=Mozilla/5.0 (X11; Linux x86_64) "

payload="[{\"type\":\"lease\",\"msrp\":null,\"tier\":\"1+\",\"term\":\"24\",\"model\":\"yaris\",\"offers\":[{\"advertised\":true,\"compatibility\":[\"Down Payment Assistance\",\"Dealership Personnel Sales Tracking\",\"Dealership Personnel TFS Contract Reward\",\"Sales Manager Flat Cash\",\"Non-Cash Certificate\",\"Dealership Personnel % Stair Step (Dealership Personnel Sales)\",\"Retention Program\",\"Payment Waiver\",\"Dealer Unit Stair Step\",\"Dealer Wholesale Program\",\"Loyalty\",\"Closing Cash\",\"Dealership Personnel Trip\",\"College Graduate\",\"Dealer Hit and Win\",\"Targeted Certificate\",\"Military\",\"Dealership Personnel Cash Bash\",\"TFS APR Cash\",\"Dealer Sales Tracking\",\"Campaign\",\"Dealership Personnel Non-VIN\",\"Dealer Points\",\"Complimentary First Payment\",\"Bonus\",\"Dealer % Stair Step\",\"Dealership Personnel Hit and Win\",\"Dealer Pot of Gold\",\"Sales Person Flat Cash\",\"Dealer Cash\",\"Dealer Trip Incentive\",\"Dealership Personnel Variable Payment\",\"TFS Lease Cash\",\"Conquest\",\"Dealership Personnel Override\",\"Dealership Personnel Pot of Gold\",\"Other Dealership Personnel Flat Cash\",\"Dealership Personnel Points\",\"Trade-in Assistance\",\"Dealership Personnel Stair Step\",\"Dealership Personnel % Stair Step (Dealership Sales)\",\"Event\"],\"isBase\":true,\"offerType\":\"Customer Cash\",\"offerId\":\"yaris_cash_264516\",\"isSubvented\":false,\"type\":\"CUSTOMER_CASH\",\"amount\":1000,\"amountDown\":1000}],\"tradeIn\":0,\"mileage\":null,\"baseMsrp\":16645,\"trimCode\":\"6267\",\"modelYear\":\"2020\",\"pricingArea\":\"001 - CA\",\"downPayment\":null}]"
headers = {
  'Host': 'www.ws.public.oatms.tms.aws.toyota.com',
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
  'x-api-key': 'eI64ESPBv39pqVDblhXZ56tGw96izAPP4F5P42Th',
  'Adresse': '165.22.225.136:443',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)
res = response.text
print([x.strip() for x in res.split(",")])