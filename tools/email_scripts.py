import requests

def check_twitter(email):
    
    burp0_url = "https://twitter.com:443/i/api/i/users/email_available.json?email="+email
    burp0_cookies = {"guest_id_ads": "v1%3A169449539828820998", "guest_id_marketing": "v1%3A169449539828820998", "_ga": "GA1.2.969011217.1680331615", "g_state": "{\"i_l\":2,\"i_p\":1695971489647}", "personalization_id": "\"v1_IjDMptzlrnoSlbFQ0fsyZQ==\"", "guest_id": "v1%3A169588508039136411", "ct0": "a1683a1a7b85ede813ba4ea2807e3474", "_gid": "GA1.2.409740323.1695885087", "gt": "1707291914553246024", "_twitter_sess": "BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://twitter.com/i/flow/signup", "X-Csrf-Token": "a1683a1a7b85ede813ba4ea2807e3474", "X-Guest-Token": "1707291914553246024", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "X-Client-Transaction-Id": "/+dExioBnbqu5th+iIBrvfC23MWhRaqi5Th3aj9X0mi6nXh5E6b8bp0Xo8MffTOhjig8Ov83LbSo3drFMJ3lMFD3M4hg/g", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA", "Te": "trailers"}
    res= requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    jsonData= res.json()
     
     
    if(jsonData['valid']):
        print("Twitter : False")
    else:
        print("Twitter : True")