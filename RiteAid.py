import requests
import json

def findSlots(zipcode, radius):
    receive = requests.get(
        'https://www.riteaid.com/services/ext/v2/stores/getStores?address=' + zipcode + '&attrFilter=PREF-112&fetchMechanismVersion=2&radius=' + radius)
    print(receive.text)
    locationjson = json.loads(receive.text)
    for stores in locationjson["Data"]["stores"]:
        receive2 = requests.get(
            'https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber=' + str(stores["storeNumber"]))
        #print(receive2.text)
        slotdetails = json.loads(receive2.text)
        if slotdetails["Data"]["slots"]["1"] is False & slotdetails["Data"]["slots"]["2"] is False:
            print('No slots available in ' + stores["address"])


if __name__ == '__main__':
    findSlots('07417', '100')
