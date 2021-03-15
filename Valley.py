import requests
import json

def findSlots():
    headers = {'authority' : 'www.zocdoc.com','sec-ch-ua-mobile' : '?0','user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36','content-type' : 'application/json','accept' : '*/*','origin' : 'https://www.zocdoc.com','sec-fetch-site' : 'same-origin','sec-fetch-mode' : 'cors','sec-fetch-dest' : 'empty','referer' : 'https://www.zocdoc.com/wl/valleycovid19vaccination/practice/64268?reason_visit=5243','accept-language' : 'en-US,en;q=0.9','cookie' : 'firstTimeVisitor=de852416-c389-4dbb-a997-78a5ac21b931; referrer_dab8e37c077d4175a3c533c0a45521c4=www.valleyhealth.com%2F; cvt=64268; visid_incap_523493=IOf5Ut6OSqq3wGtbIpSS3FO4TmAAAAAAQUIPAAAAAADKNc3WhcYKbph538IsuFJ+; nlbi_523493=8kJtEXRRpm47MzSsDaeObwAAAADbfJn+P0rphD2nV1BKkcUf; incap_ses_1329_523493=+KBOf/qej1kGC5TAhY5xElO4TmAAAAAA6qA0D5Vx+ilE/QPTmrSRmw==; originalReferrer=https://www.valleyhealth.com/; mostRecentReferrer=https://www.valleyhealth.com/; spt=NJ; bsid=dab8e37c077d4175a3c533c0a45521c4_2103150130; lbuid=dab8e37c077d4175a3c533c0a45521c4_2103150130; AWSALB=jMKu5lXm4SPRPqJmq3wG9ft4+VyxnY/wpSkxsBqJGnffEv05KxpOkzSh6wwbvOAdCjdWhyC/jfbqwrXLzM8QoaR7sJQcHWAOfUUNiSdNWhKLUq7NFhsQ7NfHDARR; AWSALBCORS=jMKu5lXm4SPRPqJmq3wG9ft4+VyxnY/wpSkxsBqJGnffEv05KxpOkzSh6wwbvOAdCjdWhyC/jfbqwrXLzM8QoaR7sJQcHWAOfUUNiSdNWhKLUq7NFhsQ7NfHDARR; paset=out_20210315013050'}
    payload = {'BusinessUnit':'PatientWebApp','Name':'Action', 'Version':'4.1.0','EventData':'[{"BrowserTimestamp":"2021-03-15T01:31:01.826Z","PageId":"fee1d78750582d289be99f73091d64a7","SessionId":"dab8e37c077d4175a3c533c0a45521c4","TrackingId":"de852416-c389-4dbb-a997-78a5ac21b931","UserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36","BookingId":null,"Page":"Private White Label","Section":null,"Component":"Vaccine Confirmation Modal","Element":"Continue Button","Initiator":"user","InteractionType":"click","EventDetails":null,"ZlogRollupBucket":"Practice","ZlogPageType":"Practice","Category":"PracticeProfile","Action":"Click to continue to private white label","Name":"[PracticeProfile] Click to continue to private white label"}]'}
    receive = requests.post(
        'https://www.zocdoc.com/eventslogging/v1/event', headers = headers, json = payload)
    print(receive.text)

if __name__ == '__main__':
    findSlots()