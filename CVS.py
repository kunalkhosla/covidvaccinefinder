import requests
import json

def findSlots(statecode):
    headers = {'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine'}
    receive = requests.get(
        'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.' + statecode + '.json?vaccineinfo', headers = headers)
    print(receive.text)
    responsejson = json.loads(receive.text)
    for location in responsejson["responsePayloadData"]["data"][statecode]:
        print(location["city"] + ' is ' + location["status"])
        if not location["status"] and location["status"] != "Fully Booked":
            print(location["city"] + ' might have slots. Check https://www.cvs.com/immunizations/covid-19-vaccine')
            print(location)


if __name__ == '__main__':
    findSlots('NJ')
