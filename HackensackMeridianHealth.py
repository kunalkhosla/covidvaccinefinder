import requests
import json

def findSlots():
    headers = {'Connection' : 'keep-alive', 'sec-ch-ua' : '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'Accept' : '*/*','X-Requested-With' : 'XMLHttpRequest', 'sec-ch-ua-mobile' : '?0', '__RequestVerificationToken' : 'KcwmzGszJ-XzFUGvHbC0t8iUe5FHCPT1tiiitwdIR0z03FbER9u61RwtewlBs0pR2pShcZATPd-xgRsmnot21A2f__01', 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36', 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin' : 'https://mychart.hmhn.org', 'Sec-Fetch-Site' : 'same-origin', 'Sec-Fetch-Mode' : 'cors', 'Sec-Fetch-Dest' : 'empty', 'Referer' : 'https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916', 'Accept-Language' : 'en-US,en;q=0.9', 'Cookie' : 'MyChart_Session=lbhokln0azx3kprq5tx2dw25; __RequestVerificationToken_L015Y2hhcnQ1=7xH8Osh0tZnX_qN4YrM58e0_EZMMbNcnTr7kVevqLYxizaVmquVpL7O-BxK02lhS-9ZO4AbtlAUJ_A-JG7hy9LeJAYk1; MyChartLocale=en-US; .WPCOOKIE4mychart=91F7BBA3BDEF781F3EE488B44EA4E27BD794E9C14D1CE711A2731FA50EA984C448B19D5FB17F0232E8176F4B2BD6F28D6D0D4576A30D91FB60422B3DB65D78A81A929B93DE7C843A34E13C0AB7B8AE3C57BE41EBCBDC97A18183919428CD3529236D22CB8C715D7DE5DC83383CDDD991C2D8EA9E94EA1C4A93185E08EABAF5E1CF376F9C0B7A8D6F44E425D91EB45C012C2CBEB58E6837073DE8D296F9C3816AEE1CCB40756AD7C7EA34579BB688665CDE42C328E2BB462B636A1E16595429C5A49D79ACA0B7327B1B774B7D6812C8E8023404998EA39ABBB591E08E2D14C85A99986E80C4AC7F09C5C8E358567662586DE47206; MyChartPersistence=3901807370.47873.0000'}
    payload = 'vt=112916&dept=1110101656%2C1110301124&view=grouped&start=&filters=%7B%22Providers%22%3A%7B%7D%2C%22Departments%22%3A%7B%7D%2C%22DaysOfWeek%22%3A%7B%7D%2C%22TimesOfDay%22%3A%22both%22%7D'
    receive = requests.get(
        'https://mychart.hmhn.org/Mychart/OpenScheduling/OpenScheduling/GetOpeningsForProvider?noCache=0.7057904056949817', headers = headers, json = payload)
    print(receive.text)
    # Currently giving 500 Internal Servicer Error

if __name__ == '__main__':
    findSlots()
