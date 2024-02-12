import requests

cookies = {
    'SESSION': 'cf1a5dce-4528-4be2-afbc-5ca85db5f9ab',
    'XSRF-TOKEN': '0c21514a-2d03-47f1-8433-6e51d3fff0d6',
    'visid_incap_1445108': 'lKkW/0JZQ7iNgQRFycDYJAN3rmUAAAAAQUIPAAAAAABAU2x2LpHpAdRp2gP4sM7c',
    'okta_override': 'null',
    'MOBILE_APP': 'null',
    'MOBILE_PLATFORM': 'null',
    'OKTA_MOBILE_USER_LOGIN': 'null',
    'mobile_webview': 'null',
    'USER_PRODUCT': 'us',
    'MNCPORTAL_LANGUAGE': 'en',
    'ROUTEID': '.tkgch2',
    'nlbi_1445108': 'WYRWVN9m9WK/IHbLFLCm0wAAAAAoSN39tFa34Q4HlZ/Y9GT0',
    'incap_ses_1814_1445108': 'X2CHKt+rqSLOWbqQcZ8sGXJFw2UAAAAAdYzUTWboSRGRjNsQ4w5wkw==',
    'rxVisitor': '170729611693865A56NM0H91SBNACOGQP8O2QS8G3UD74',
    'incap_ses_1596_1445108': 'hr8ldrcmXmJ2C6xMICImFvoByGUAAAAAt13LJUPh1eEYsge9RKwTBQ==',
    'reese84': '3:psIN33Kp3gUYOlqmq4jpZQ==:bYmTFlcVHyrEmTDoeMnH/c0GlHqaCjKe7iPqnSv1uK0flTLFcXrJYb/LS1K85qkticci4vN6vMUnfx7ul09zoTiwK0DEOBRbaMMzFrFhzQdLSJ3es0csYIc6LDuh/YoqukJPbbTOFDg4rWblQzZvp0rmpuOjbzyJN/xmbuDsv6QafpPkjH/L5BOoc9zTEHwWpn04vvPqaHPrN49j3/aLXK+Dza5h3dWIKw9UEsJ4dHVidx+zXWcbeB2r+zWb/GjSHEMWZ/sNjrZQHwsz8tu9KoCb/E/HB0wQzdjgjzX/SJt30XR4f9bEwjMeswm4sIi1ptpxi2rm9hxczIln+tK/rpvtN9cvuPLEsRVpoz85bGPOt+4huc2a8tD2W0FxeelZGWq6yDsXGSAbfTha2U0PWUja8wTKchYkesvEZZzP5XNAHH3qF9xjfkjk4vOdkebPpuNP0ZXLxfYCdjlBUJgLUSuz46de5HRqAMhUojKul0s=:vEaBoLaHX/uP2J2yDGK9yUzQOX+zcqYOb1IqBrXmoTY=',
    'okta_redirect_uri': 'https://www.powerofvitality.com/vitality/login/complete_login',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+10+2024+18%3A08%3A44+GMT-0500+(Eastern+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.powerofvitality.com%2Fvitality%2Flogin&groups=C0003%3A0%2CC0002%3A0%2CC0001%3A1%2CC0004%3A0',
    'okta-oauth-redirect-params': '{%22responseType%22:[%22code%22]%2C%22state%22:%22X85hSG3tbO9jeiDgwJRUollgoS9xWBZDiOgACJyEUo4RE92PtrzMvkAZvQOLF9YK%22%2C%22nonce%22:%22js8gBuafSLUxkxT7KwykQksJgRWPOsVchsRxKXkWNg7pTQ46RAiStNSCrhfUVXIp%22%2C%22scopes%22:[%22openid%22%2C%22profile%22%2C%22email%22]%2C%22clientId%22:%220oajntygg6PQ8hXAZ5d6%22%2C%22urls%22:{%22issuer%22:%22https://login.powerofvitality.com/oauth2/default%22%2C%22authorizeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/authorize%22%2C%22userinfoUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/userinfo%22%2C%22tokenUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/token%22%2C%22revokeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/revoke%22%2C%22logoutUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/logout%22}%2C%22ignoreSignature%22:false}',
    'okta-oauth-nonce': 'js8gBuafSLUxkxT7KwykQksJgRWPOsVchsRxKXkWNg7pTQ46RAiStNSCrhfUVXIp',
    'okta-oauth-state': 'X85hSG3tbO9jeiDgwJRUollgoS9xWBZDiOgACJyEUo4RE92PtrzMvkAZvQOLF9YK',
    'VITALITYPORTAL_WD_WLJSESSIONID': '7MyVR_OzTXbNGo0Co5B85aboonaNUk63uiBGDyIKT-kBNZIya46P!876725269',
    'dtSa': '-',
    'nlbi_1445108_2147483392': '7txdFH8JSmMg30uSFLCm0wAAAACYH2nYM7a+0bUJXQRkBa4X',
    'rxvt': '1707608340880|1707606523814',
    'dtPC': '3$6537804_613h-vKUHBJRGPFDCVHCLRERKCEKMMSERPFISQ-0e0',
    '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D',
    '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22s%22%3A%22%22%2C%22p%22%3A%22%22%2C%22m%22%3A%22%22%2C%22a%22%3A%22%22%7D%7D%2C%22region%22%3A%22USFL%22%2C%22lim%22%3A%5B%22CMP%22%5D%2C%22reg%22%3A%22%22%2C%22v%22%3A%222.1%22%7D',
    '_shopify_y': '62be15f4-18c8-4d1a-a85c-5c44ffd8992a',
    '_orig_referrer': 'https%3A%2F%2Fwww.powerofvitality.com%2F',
    '_landing_page': '%2F',
    '_shopify_sa_p': '',
    '_shopify_s': '15e499bc-7449-4190-b45c-2b2d04b5f91e',
    '_shopify_sa_t': '2024-02-10T23%3A19%3A57.360Z',
    'dtCookie': 'v_4_srv_3_sn_14953603A320B71727F1F66B504C401E_perc_100000_ol_0_mul_1_app-3A2c36208e7dc0785b_1_app-3Aa300a63665cac321_1_app-3Af705364a6360debd_1_rcs-3Acss_0',
}

headers = {
    'authority': 'www.powerofvitality.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    # 'cookie': 'SESSION=cf1a5dce-4528-4be2-afbc-5ca85db5f9ab; XSRF-TOKEN=0c21514a-2d03-47f1-8433-6e51d3fff0d6; visid_incap_1445108=lKkW/0JZQ7iNgQRFycDYJAN3rmUAAAAAQUIPAAAAAABAU2x2LpHpAdRp2gP4sM7c; okta_override=null; MOBILE_APP=null; MOBILE_PLATFORM=null; OKTA_MOBILE_USER_LOGIN=null; mobile_webview=null; USER_PRODUCT=us; MNCPORTAL_LANGUAGE=en; ROUTEID=.tkgch2; nlbi_1445108=WYRWVN9m9WK/IHbLFLCm0wAAAAAoSN39tFa34Q4HlZ/Y9GT0; incap_ses_1814_1445108=X2CHKt+rqSLOWbqQcZ8sGXJFw2UAAAAAdYzUTWboSRGRjNsQ4w5wkw==; rxVisitor=170729611693865A56NM0H91SBNACOGQP8O2QS8G3UD74; incap_ses_1596_1445108=hr8ldrcmXmJ2C6xMICImFvoByGUAAAAAt13LJUPh1eEYsge9RKwTBQ==; reese84=3:psIN33Kp3gUYOlqmq4jpZQ==:bYmTFlcVHyrEmTDoeMnH/c0GlHqaCjKe7iPqnSv1uK0flTLFcXrJYb/LS1K85qkticci4vN6vMUnfx7ul09zoTiwK0DEOBRbaMMzFrFhzQdLSJ3es0csYIc6LDuh/YoqukJPbbTOFDg4rWblQzZvp0rmpuOjbzyJN/xmbuDsv6QafpPkjH/L5BOoc9zTEHwWpn04vvPqaHPrN49j3/aLXK+Dza5h3dWIKw9UEsJ4dHVidx+zXWcbeB2r+zWb/GjSHEMWZ/sNjrZQHwsz8tu9KoCb/E/HB0wQzdjgjzX/SJt30XR4f9bEwjMeswm4sIi1ptpxi2rm9hxczIln+tK/rpvtN9cvuPLEsRVpoz85bGPOt+4huc2a8tD2W0FxeelZGWq6yDsXGSAbfTha2U0PWUja8wTKchYkesvEZZzP5XNAHH3qF9xjfkjk4vOdkebPpuNP0ZXLxfYCdjlBUJgLUSuz46de5HRqAMhUojKul0s=:vEaBoLaHX/uP2J2yDGK9yUzQOX+zcqYOb1IqBrXmoTY=; okta_redirect_uri=https://www.powerofvitality.com/vitality/login/complete_login; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+10+2024+18%3A08%3A44+GMT-0500+(Eastern+Standard+Time)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.powerofvitality.com%2Fvitality%2Flogin&groups=C0003%3A0%2CC0002%3A0%2CC0001%3A1%2CC0004%3A0; okta-oauth-redirect-params={%22responseType%22:[%22code%22]%2C%22state%22:%22X85hSG3tbO9jeiDgwJRUollgoS9xWBZDiOgACJyEUo4RE92PtrzMvkAZvQOLF9YK%22%2C%22nonce%22:%22js8gBuafSLUxkxT7KwykQksJgRWPOsVchsRxKXkWNg7pTQ46RAiStNSCrhfUVXIp%22%2C%22scopes%22:[%22openid%22%2C%22profile%22%2C%22email%22]%2C%22clientId%22:%220oajntygg6PQ8hXAZ5d6%22%2C%22urls%22:{%22issuer%22:%22https://login.powerofvitality.com/oauth2/default%22%2C%22authorizeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/authorize%22%2C%22userinfoUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/userinfo%22%2C%22tokenUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/token%22%2C%22revokeUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/revoke%22%2C%22logoutUrl%22:%22https://login.powerofvitality.com/oauth2/default/v1/logout%22}%2C%22ignoreSignature%22:false}; okta-oauth-nonce=js8gBuafSLUxkxT7KwykQksJgRWPOsVchsRxKXkWNg7pTQ46RAiStNSCrhfUVXIp; okta-oauth-state=X85hSG3tbO9jeiDgwJRUollgoS9xWBZDiOgACJyEUo4RE92PtrzMvkAZvQOLF9YK; VITALITYPORTAL_WD_WLJSESSIONID=7MyVR_OzTXbNGo0Co5B85aboonaNUk63uiBGDyIKT-kBNZIya46P!876725269; dtSa=-; nlbi_1445108_2147483392=7txdFH8JSmMg30uSFLCm0wAAAACYH2nYM7a+0bUJXQRkBa4X; rxvt=1707608340880|1707606523814; dtPC=3$6537804_613h-vKUHBJRGPFDCVHCLRERKCEKMMSERPFISQ-0e0; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22s%22%3A%22%22%2C%22p%22%3A%22%22%2C%22m%22%3A%22%22%2C%22a%22%3A%22%22%7D%7D%2C%22region%22%3A%22USFL%22%2C%22lim%22%3A%5B%22CMP%22%5D%2C%22reg%22%3A%22%22%2C%22v%22%3A%222.1%22%7D; _shopify_y=62be15f4-18c8-4d1a-a85c-5c44ffd8992a; _orig_referrer=https%3A%2F%2Fwww.powerofvitality.com%2F; _landing_page=%2F; _shopify_sa_p=; _shopify_s=15e499bc-7449-4190-b45c-2b2d04b5f91e; _shopify_sa_t=2024-02-10T23%3A19%3A57.360Z; dtCookie=v_4_srv_3_sn_14953603A320B71727F1F66B504C401E_perc_100000_ol_0_mul_1_app-3A2c36208e7dc0785b_1_app-3Aa300a63665cac321_1_app-3Af705364a6360debd_1_rcs-3Acss_0',
    'origin': 'https://www.powerofvitality.com',
    'pragma': 'no-cache',
    'referer': 'https://www.powerofvitality.com/v3/employee-portal/home/activities/Workouts/69810358/Self-reported%20workout/Self%20captured?form=selfworkout&entryPoint=Workouts',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'translate-to': 'EN_US',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-xsrf-token': '0c21514a-2d03-47f1-8433-6e51d3fff0d6',
}

# params = {
#     'programEnrolmentCohortActivityId': '69810358',
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
for day in range(1, 29):
    day_long = f'0{day}' if day < 10 else str(day)
    params = {
        'programEnrolmentCohortActivityId': '69810358',
        'activityValue': 'handstand',
        'date': f'2024-02-{day_long}T05:00:00.062Z',
    }

    response = requests.post(
        'https://www.powerofvitality.com/v3/bff/activity/api/v1/program-enrolment-cohort-activity/activity/complete',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(f'{day_long} - {response.status_code}')
