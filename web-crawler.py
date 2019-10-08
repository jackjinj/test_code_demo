import requests
import json
def write_browser_info_to_file():
    my_user_agent = requests.get("https://fake-useragent.herokuapp.com/browsers/0.1.11")
    my_user_agent = my_user_agent.text
    with open("browser_info.json", "w") as f:
        json.dump(my_user_agent, f)
#        f.write( str(my_user_agent) )
    print("hello")

write_browser_info_to_file()
import random
def get_random_browser():
    with open ("browser_info.json", "r") as f:
        browsers_json = json.load(f)
        browsers_json = json.loads(browsers_json)
        browsers = browsers_json["browsers"]
        # print (browsers)
        chrome = browsers["chrome"]
        # print(chrome)

        i = random.randint(0, len(browsers))
        browser_name = ""
        if i == 0:
            browser_name = "chrome"
        elif i == 1:
            browser_name = "opera"
        elif i == 2:
            browser_name = "firefox"
        elif i == 3:
            browser_name = "internetexplorer"
        else:
            browser_name = "safari"
        print(browser_name)
        final_browser = browsers[browser_name][random.randint(0, len(browsers[browser_name])-1)]
        # print (final_browser)
        return final_browser

import requests
import time

def get_request_url_and_headers():
    user_agent = get_random_browser()
    current_time = int(time.time())
    headers = {
        "user-agent": user_agent
    }
    base_url = "https://www.toutiao.com/api/pc/feed/?" \
                "max_behot_time="+str(current_time)+"&" \
                "category=__all__&utm_source=toutiao&widen=1&" \
                "tadrequire=true&as=A1D5DD39471E752&cp=5D970EC70532BE1&_signature=YH6GWxAYPe0TiIw0P503UGB-hk"

    proxies = {
        "url": 'http://114.235.23.172:9000'
    }
    # print (base_url, headers, proxies)
    return base_url, headers, proxies

def get_response_html():

    request_url, headers, proxies = get_request_url_and_headers()
    print (request_url)
    response = requests.get(request_url, headers=headers, proxies=proxies)
    global response_json
    # print (response.text)
    response_json = json.loads(response.text)
    # print(response_json)
    if response_json["message"] == "error":
        get_response_html()
    print (response_json)
    return response_json

json_content=get_response_html()
print(json_content)

def data_to_file():
    data = response_json["data"]
    for i in range(len(data)):
        data_dict=data[i]
        with open("toutiao.json", "a+") as f:
            json.dump(data_dict, f, ensure_ascii=False)
            f.write("\n")
data_to_file()
import pandas as pd
df = pd.read_json("toutiao.json", lines=True)
print(df)
df.to_excel("toutiao.xlsx")
