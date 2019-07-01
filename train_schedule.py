import requests,json
api='14z9ghglin'
no=input()
url=f"https://api.railwayapi.com/v2/route/train/{no}/apikey/{api}/"
print(url)
obj=requests.get(url)
res=obj.json()
if(res['response_code']==200):
    li=res['route']
    print("Train Name",res['train']['name'])
    print('{:<30}{}'.format('Station Name','Arrival Time'))
    for i in range(len(li)):
        print('{:<30}{}'.format(li[i]['station']['name'],li[i]['scharr']))


