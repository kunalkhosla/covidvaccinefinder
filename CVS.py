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
        if location["status"] == "Available":
            print(location["city"] + ' might have slots. Check https://www.cvs.com/immunizations/covid-19-vaccine')
            headersforLocation = {'authority' : 'www.cvs.com', 'sec-ch-ua' : '\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"', 'accept' : 'application/json', 'sec-ch-ua-mobile' : '?0', 'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36','content-type' : 'application/json','origin' : 'https://www.cvs.com', 'sec-fetch-site' : 'same-origin', 'sec-fetch-mode' : 'cors', 'sec-fetch-dest' : 'empty', 'referer' : 'https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select', 'accept-language' : 'en-US,en;q=0.9', 'cookie' : 'QuantumMetricUserID=c50eea59a46f3a91d1f092e144d246e6; pe=p1; acctdel_v1=on; adh_new_ps=on; adh_ps_pickup=on; adh_ps_refill=on; buynow=off; sab_displayads=on; dashboard_v1=off; db-show-allrx=on; disable-app-dynamics=on; disable-sac=on; dpp_cdc=off; dpp_drug_dir=off; dpp_sft=off; getcust_elastic=on; echomeln6=off-p0; enable_imz=on; enable_imz_cvd=on; enable_imz_reschedule_instore=off; enable_imz_reschedule_clinic=off; flipp2=on; gbi_cvs_coupons=true; ice-phr-offer=off; v3redirecton=false; mc_cloud_service=on; mc_hl7=on; mc_home_new=off1; mc_ui_ssr=off-p2; mc_videovisit=on; memberlite=on; pauth_v1=on; pivotal_forgot_password=off-p0; pivotal_sso=off-p0; pbmplaceorder=off; pbmrxhistory=on; ps=on; refill_chkbox_remove=off-p0; rxdanshownba=off; rxdfixie=on; rxd_bnr=on; rxd_dot_bnr=on; rxdpromo=on; rxduan=on; rxlite=on; rxlitelob=off; rxm=on; rxm_phone_dob=off-p1; rxm_demo_hide_LN=off; rxm_phdob_hide_LN=on; rxm_rx_challenge=on; s2c_akamaidigitizecoupon=on; s2c_beautyclub=off-p0; s2c_digitizecoupon=on; s2c_dmenrollment=off-p0; s2c_herotimer=off-p0; s2c_newcard=off-p0; s2c_papercoupon=on; s2c_persistEcCookie=on; s2c_smsenrollment=on; s2cHero_lean6=on; sft_mfr_new=on; sftg=on; show_exception_status=on; v2-dash-redirection=on; ak_bmsc=C2CE3798C91FFF0454B600BB4DC7BD86684D9F3FCA710000A59B4E607835D760~plkHe+02f7tyZeHnQw9XpruD9Czc/dIbn7dFpYUxwUhP3To8kQKmillohBURwjUeTLabHfgZl24FYn7lyJXkMvl7N/HCdjWtqXw4ghEWC6GW8xdrJ4C/cGO2IJszMLRM8zqXyHe/9cUZQQlimp/Zkt0aZM+GA9nhQs74kjkJfCwbM4INW6xUM/A4DmRZ4PVgSAAh1F2m88VSIrsQdWPx3nTNJP8GSvvcWv8vR6i71tvas=; bm_sz=97AC65D21684ADCAAEC701FDD51CBBC6~YAAQP59NaKgEHhp4AQAAHwAQMwt4M+WxU1yYT1MOrxq1F9PN6cHeMk7vpYFUbC77cGgAIJ1mtxkvufzYimHpTONr2/65aeVTT7ZKV3LXGFGYYfAy4wfDHBJk4DmLC8GtaSLqTx1stNMtRDaGjJNAeffkjz8foyRVtQPQMwePk1Z5ujKNPjmSf+4fY2U=; mt.v=2.1379306187.1615764390340; _group1=quantum; mt.sc=%7B%22i%22%3A1615764390647%2C%22d%22%3A%5B%5D%7D; AMCVS_06660D1556E030D17F000101%40AdobeOrg=1; AMCV_06660D1556E030D17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C18701%7CMCMID%7C17129657402499001813476679218754461198%7CMCAAMLH-1616369191%7C7%7CMCAAMB-1616369191%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615771591s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; s_cc=true; _gcl_au=1.1.1268641049.1615764393; gbi_sessionId=ckm9segyc00003g96f6irbixi; gbi_visitorId=ckm9segyd00013g96nfr43mj0; _4c_mc_=f7f525bc-56d2-4d9f-8a71-6b3dae4c4eb5; QuantumMetricSessionID=831d5826c9b5d398acf04e9e4fa286c8; CVPF=3b-llOZCI9ElxVgQ_SrXQz8x1KHuS0EIg_dT5xm1bDOGu06EmEWnEig; akavpau_vp_www_cvs_com_vaccine_covid19=1615765820~id=a6ad6cd7396dce3c25ab359984dc24ca; mt.cem=210201-Rx-Immunization-COVIDvax - A-Iteration; mt.mbsh=%7B%22fs%22%3A1615765299896%2C%22sf%22%3A1%2C%22lf%22%3A1615765299898%7D; _abck=31829C6275C6B759CF3B1708FFC54268~0~YAAQIZcwFxL0KRJ4AQAA9GAeMwXwQ5bM957in991fMHee+25PdIE15CMrko3w/w0w6L5t/YBPar3YvRCvUXHjyZs1edJytinbtUv2Ym/ckkNQtrQZwcvkxD6/z6n5/WeswRjvrojGlytUHeVPqeDUD0MgbOGwF2Jjd3U5rr0qWMmxIU16SdqdgSBX++FTFqe8yqzGKVvIwJKnlc+XknqXD1uXPJ3HsmcmTp4i9cJ7FpDcFX/4oPF3ybIsurW28MgIgW1czFpEEe8fUDg+mnVg5Sy9Y6ZTBdfJaic7PSDEwgtPPf3SQxEwPv+qjP9QPP7EETXCef6VM77sy1xrVAkPLBEazpp1N0Q6AZ7jsnf8qmHuRFP4dp9dx9R58eaAWBF4wvAW1LYOTxMq+t5i3Uu9ALXTa1g~-1~-1~-1; akavpau_vp_www_cvs_com_vaccine=1615765941~id=aeb093b9c824c7ae06732d81cb70c8c1; akavpau_www_cvs_com_general=1615765761~id=4f3640975f97c792d87a8088f779ee3c; bm_sv=EFE1C0AE0B6C57BC14ED0C8A7ECC8715~xaMPWwkqJwrMGpGYC9QHnIRvKZ34INCRMbHuLzS/uu+OgIhFFOrA8oH5E9jkWBWtOdZn9eNuUNwDC1Ew22/J6xNZY7npuAbepIjRmYwYVgfvtik1qOEoJI0b/WIqYTsYHn6G7Kxj8Zi2MlPIM9P/TQ==; s_sq=%5B%5BB%5D%5D; gpv_e5=cvs%7Cdweb%7Cvaccine%7Cintake%7Cstore%7Ccvd-store-select%7Crx%3A%20immunizations%3A%20first%20dose%20scheduler; gpv_p10=www.cvs.com%2Fvaccine%2Fintake%2Fstore%2Fcvd-store-select%2Ffirst-dose-select; RT=\'z=1&dm=cvs.com&si=833d2cfd-ceec-457c-9847-e2984ba6cf2e&ss=km9seec2&sl=e&tt=6nc&bcn=%2F%2F36ebc234.akstat.io%2F&ld=nf09\'; qmexp=1615767300823; utag_main=v_id:0178331002a400192404353802af03078003207000fb8$_sn:1$_ss:0$_pn:4%3Bexp-session$_st:1615767301948$ses_id:1615764390564%3Bexp-session$vapi_domain:cvs.com'}
            payloadForLocation = '{"requestMetaData":{"appName":"CVS_WEB","lineOfBusiness":"RETAIL","channelName":"WEB","deviceType":"DESKTOP","deviceToken":"7777","apiKey":"a2ff75c6-2da7-4299-929d-d670d827ab4a","source":"ICE_WEB","securityType":"apiKey","responseFormat":"JSON","type":"cn-dep"},"requestPayloadData":{"selectedImmunization":["CVD"],"distanceInMiles":35,"imzData":[{"imzType":"CVD","ndc":["59267100002","59267100003","59676058015","80777027399"],"allocationType":"1"}],"searchCriteria":{"addressLine":"' + location["city"] + '}}}'
            locationResponse = requests.get('https://www.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores', headers = headersforLocation, json = payloadForLocation)
            print(locationResponse)


if __name__ == '__main__':
    findSlots('NJ')
