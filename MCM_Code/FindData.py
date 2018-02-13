from urllib.request import urlopen
from urllib.request import Request
from urllib.error import HTTPError
import json
import GlobalList
url = "https://www.tesla.com/all-locations"
output_file_path = open("./Data/data.txt", 'w', encoding='utf-8')
def SetReq(url):
    headers_1 = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
        #'Connection': 'keep-alive'
    }
    headers_2 = {
        'User=Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    }
    req = Request(url=url, headers=headers_1)
    print("Set the header successfully!")
    return req

def GetHtmlJson(req):
    html = urlopen(req).read()
    hjson = json.load(html)
    return hjson

if __name__ == '__main__':
    req = SetReq(url)
    response = urlopen(url).read()
    jsonResponse = json.loads(response.decode('utf-8'))
    print("Get the json data successsfully! ")
    for temp in jsonResponse:
        #print(temp, file=output_file_path)
        nid = temp['nid']
        country = temp['country']
        if (country == 'United States'):
            latitude = temp['latitude']
            longitude = temp['longitude']
            location_type = temp['location_type'][0]
            open_soon = temp['open_soon']
            province = temp['province_state']
            GlobalList.Data_Counter += 1
            if(str(open_soon) == '0'):
                print(str(nid) + "," + str(province) + "," + str(latitude) + "," + str(longitude) + "," + str(location_type) + "," + str(open_soon), file=output_file_path)
                GlobalList.Data_Counter_open = GlobalList.Data_Counter_open + 1
    print("Total: "+str(GlobalList.Data_Counter)+" Unopened: "+str(GlobalList.Data_Counter_open))