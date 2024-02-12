import requests

cookies = {
    'SESSION': '9bd0ddf3-db10-4459-bdee-b50a644886f4',
    'XSRF-TOKEN': 'd417a8b0-4d81-4349-b0a0-6d18ba930003',
    'ROUTEID': '.tkgch2',
    'visid_incap_1445108': 'G0pNDTRDSMWiZV+1GtYlurQKyGUAAAAAQUIPAAAAAACffU7NIOrw+QFjSUllrRkx',
    'nlbi_1445108': 'KjjiatnyLRkoqhhVFLCm0wAAAAABMjtuOi28pvHLSqEMYEDx',
    'incap_ses_1596_1445108': 'ayVra62dd0ILkbFMICImFrUKyGUAAAAA5aTPhUQXy3ald8bXoOv7wQ==',
    'reese84': '3:qR+94BN9K2cvfl6Tp4x5SA==:fh7o8CHDNLz/3DE/FLBhWMVgBQS+la5ZzgR7aXaRV7uKLONRfhHgU+1wFucwnOgbXN0xHNRid6+158lzkeKZXItCNxrDxl+B/F+xfqeHgiMj6RzSqFeApBNE40h3VVDKdAaj7Q2DrjL0DQoAZfCrFrIIVoJkipeNtUXDH3wot2UbeNSRf1u7bA6HP3kV41qcJT5P8oCG2sQShKjYkHPsvof+/S+OS4Fw3nBJJG+xUC8buuaNVAHnp/CQerMxHEGkiRY5qdqbO9C2vpGF53jTtyYIEwzSU8avzsuO4WEo+lMjzTL9LuInzreiun7i45FfSM9R26kUUENq6DyBe/8cpImVIRghZGFVCW6SpnRYqXoIAfSdLW7bHGargSf2jMoHDJFjLcrs8ZEyhiEEh+ByCC6S7usOfyVuANXtwAsIHkf+znkk4EivaLXmlrXiGy/XS3CUsSlYhHamUJY1lw6F5++3v4dB6fxStCNUUSiFxPo=:rKlrBRKxvkBo8dcHJaXzkm6xC560rLwp941DvhJvGYI=',
    'okta_override': 'null',
    'MOBILE_APP': 'null',
    'MOBILE_PLATFORM': 'null',
    'OKTA_MOBILE_USER_LOGIN': 'null',
    'mobile_webview': 'null',
    'okta_redirect_uri': 'https://www.powerofvitality.com/vitality/login/complete_login',
    'USER_PRODUCT': 'us',
    'MNCPORTAL_LANGUAGE': 'en',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+10+2024+18%3A45%3A59+GMT-0500+(Eastern+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.powerofvitality.com%2Fvitality%2Flogin&groups=C0003%3A0%2CC0002%3A0%2CC0001%3A1%2CC0004%3A0',
    'okta-oauth-redirect-params': '{%22responseType%22:[%22code%22]%2C%22state%22:%221wEPbJqdhkbUy1SkNlSorpY030Y0LLKFxPXudOBiHYQSXSPEdAuvXDUs0DBW6OTr%22%2C%22nonce%22:%22q4CFfA8yuvw2U9cAgbAgrpOyZAMwHjcLA4zYuDMKQvb6qGcLYOQIETfPreZ8P9CU%22%2C%22scopes%22:[%22openid%22%2C%22profile%22%2C%22email%22]%2C%22clientId%22:%220oajntygg6PQ8hXAZ5d6%22%2C%22urls%22:{%22issuer%22:%22https://login.powerofvitality.com/oauth2/default%22%2C%22authorizeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/authorize%22%2C%22userinfoUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/userinfo%22%2C%22tokenUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/token%22%2C%22revokeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/revoke%22%2C%22logoutUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/logout%22}%2C%22ignoreSignature%22:false}',
    'okta-oauth-nonce': 'q4CFfA8yuvw2U9cAgbAgrpOyZAMwHjcLA4zYuDMKQvb6qGcLYOQIETfPreZ8P9CU',
    'okta-oauth-state': '1wEPbJqdhkbUy1SkNlSorpY030Y0LLKFxPXudOBiHYQSXSPEdAuvXDUs0DBW6OTr',
    'VITALITYPORTAL_WD_WLJSESSIONID': 'A-qVanx7YhEBZ2GaYiUqTyy9x9KkEGMN6gikxD7C58CRKCwWIrRR!1218535588',
    'nlbi_1445108_2147483392': 'A58jewqAmF+3nPIhFLCm0wAAAABQU4dl68CLIKOyFGQ/3MlT',
    'dtCookie': 'v_4_srv_6_sn_0FFEF5E48FD97CC6AAB8FF2E894EE4A5_perc_100000_ol_0_mul_1_app-3A2c36208e7dc0785b_1_app-3Aa300a63665cac321_1_app-3Af705364a6360debd_1_rcs-3Acss_0',
}

headers = {
    'authority': 'www.powerofvitality.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8',
    # 'content-length': '0',
    # 'cookie': 'SESSION=9bd0ddf3-db10-4459-bdee-b50a644886f4; XSRF-TOKEN=d417a8b0-4d81-4349-b0a0-6d18ba930003; ROUTEID=.tkgch2; visid_incap_1445108=G0pNDTRDSMWiZV+1GtYlurQKyGUAAAAAQUIPAAAAAACffU7NIOrw+QFjSUllrRkx; nlbi_1445108=KjjiatnyLRkoqhhVFLCm0wAAAAABMjtuOi28pvHLSqEMYEDx; incap_ses_1596_1445108=ayVra62dd0ILkbFMICImFrUKyGUAAAAA5aTPhUQXy3ald8bXoOv7wQ==; reese84=3:qR+94BN9K2cvfl6Tp4x5SA==:fh7o8CHDNLz/3DE/FLBhWMVgBQS+la5ZzgR7aXaRV7uKLONRfhHgU+1wFucwnOgbXN0xHNRid6+158lzkeKZXItCNxrDxl+B/F+xfqeHgiMj6RzSqFeApBNE40h3VVDKdAaj7Q2DrjL0DQoAZfCrFrIIVoJkipeNtUXDH3wot2UbeNSRf1u7bA6HP3kV41qcJT5P8oCG2sQShKjYkHPsvof+/S+OS4Fw3nBJJG+xUC8buuaNVAHnp/CQerMxHEGkiRY5qdqbO9C2vpGF53jTtyYIEwzSU8avzsuO4WEo+lMjzTL9LuInzreiun7i45FfSM9R26kUUENq6DyBe/8cpImVIRghZGFVCW6SpnRYqXoIAfSdLW7bHGargSf2jMoHDJFjLcrs8ZEyhiEEh+ByCC6S7usOfyVuANXtwAsIHkf+znkk4EivaLXmlrXiGy/XS3CUsSlYhHamUJY1lw6F5++3v4dB6fxStCNUUSiFxPo=:rKlrBRKxvkBo8dcHJaXzkm6xC560rLwp941DvhJvGYI=; okta_override=null; MOBILE_APP=null; MOBILE_PLATFORM=null; OKTA_MOBILE_USER_LOGIN=null; mobile_webview=null; okta_redirect_uri=https://www.powerofvitality.com/vitality/login/complete_login; USER_PRODUCT=us; MNCPORTAL_LANGUAGE=en; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+10+2024+18%3A45%3A59+GMT-0500+(Eastern+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.powerofvitality.com%2Fvitality%2Flogin&groups=C0003%3A0%2CC0002%3A0%2CC0001%3A1%2CC0004%3A0; okta-oauth-redirect-params={%22responseType%22:[%22code%22]%2C%22state%22:%221wEPbJqdhkbUy1SkNlSorpY030Y0LLKFxPXudOBiHYQSXSPEdAuvXDUs0DBW6OTr%22%2C%22nonce%22:%22q4CFfA8yuvw2U9cAgbAgrpOyZAMwHjcLA4zYuDMKQvb6qGcLYOQIETfPreZ8P9CU%22%2C%22scopes%22:[%22openid%22%2C%22profile%22%2C%22email%22]%2C%22clientId%22:%220oajntygg6PQ8hXAZ5d6%22%2C%22urls%22:{%22issuer%22:%22https://login.powerofvitality.com/oauth2/default%22%2C%22authorizeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/authorize%22%2C%22userinfoUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/userinfo%22%2C%22tokenUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/token%22%2C%22revokeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/revoke%22%2C%22logoutUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/logout%22}%2C%22ignoreSignature%22:false}; okta-oauth-nonce=q4CFfA8yuvw2U9cAgbAgrpOyZAMwHjcLA4zYuDMKQvb6qGcLYOQIETfPreZ8P9CU; okta-oauth-state=1wEPbJqdhkbUy1SkNlSorpY030Y0LLKFxPXudOBiHYQSXSPEdAuvXDUs0DBW6OTr; VITALITYPORTAL_WD_WLJSESSIONID=A-qVanx7YhEBZ2GaYiUqTyy9x9KkEGMN6gikxD7C58CRKCwWIrRR!1218535588; nlbi_1445108_2147483392=A58jewqAmF+3nPIhFLCm0wAAAABQU4dl68CLIKOyFGQ/3MlT; dtCookie=v_4_srv_6_sn_0FFEF5E48FD97CC6AAB8FF2E894EE4A5_perc_100000_ol_0_mul_1_app-3A2c36208e7dc0785b_1_app-3Aa300a63665cac321_1_app-3Af705364a6360debd_1_rcs-3Acss_0',
    'origin': 'https://www.powerofvitality.com',
    'referer': 'https://www.powerofvitality.com/v3/employee-portal/home/activities/Workouts/25694433/Self-reported%20workout/Self%20captured?form=selfworkout&entryPoint=Workouts',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'translate-to': 'EN_US',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-xsrf-token': 'd417a8b0-4d81-4349-b0a0-6d18ba930003',
}

# params = {
#     'programEnrolmentCohortActivityId': '25694433',
#     'activityValue': 'handstand',
#     'date': '2024-01-27T05:00:00.062Z',
# }
#
# response = requests.post(
#     'https://www.powerofvitality.com/v3/bff/activity/api/v1/program-enrolment-cohort-activity/activity/complete',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )
for day in range(1, 32):
    day_long = f'0{day}' if day < 10 else str(day)
    params = {
        'programEnrolmentCohortActivityId': '25694433',
        'activityValue': 'handstand',
        'date': f'2024-01-{day_long}T05:00:00.062Z',
    }

    response = requests.post(
        'https://www.powerofvitality.com/v3/bff/activity/api/v1/program-enrolment-cohort-activity/activity/complete',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(f'{day_long} - {response.status_code}')
