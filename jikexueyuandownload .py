import thre
import re
import os
import requests



cookies = {
'BAIDU_SSP_lcr':'http://www.baidu.com/link?url=LYyCM5Ci_GBbDXJ4AkRc5olj0pillr06acfOgAm-4DL4GXb8Y7xDKumYQbWDvnTQ&wd=&eqid=fb1867e9001359920000000457870205',
'channel':'invite_100w_sharebutton_copy1',
'stat_ssid':'1469234323971',
'stat_uuid':'1468465593946196112385',
'gr_user_id':'6c90e263-90d6-40cf-a8b5-8cd6922d09fc',
'gr_session_id_aacd01fff9535e79':'bf1a1146-55bb-49af-ae9e-bc978642b7b8',
'gr_cs1_bf1a1146-55bb-49af-ae9e-bc978642b7b8':'uid%3A5263688',
'undefined':'',
'stat_isNew':'0',
'uname':'jike_1964935',
'uid':'5263688',
'code':'DBI78K',
'authcode':'6e97H1hRXgMMk2xYscarKKQ9WSuYhgCVO4uBn7MfgwgjK3KeC%2F2BttK4upS6y05sr3M9e88XafhjhTS1YMefw7u%2BJsbmRPQ9LAdRTrL21IEYHf1BThjp7ISjA3Zwuym9',
'level_id':'3',
'is_expire':'0',
'domain':'1372071482',
'Hm_lvt_f3c68d41bda15331608595c98e9c3915':'1468465674',
'Hm_lpvt_f3c68d41bda15331608595c98e9c3915':'1468465674',
'_ga':'GA1.2.1294261761.1468465674',
'_gat':'1',
'stat_fromWebUrl':'baidu.com',
'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%22155e75ffa6f42a-06aba12ec3f8b3c-293e1d4e-100200-155e75ffa7047a%22%7D',
'looyu_id':'7dac2137b4a01f395716ce01cf5f9455bb_20001269%3A1',
'looyu_20001269':'v%3A7dac2137b4a01f395716ce01cf5f9455bb%2Cref%3Ahttp%253A//www.baidu.com/link%253Furl%253DLYyCM5Ci_GBbDXJ4AkRc5olj0pillr06acfOgAm-4DL4GXb8Y7xDKumYQbWDvnTQ%2526wd%253D%2526eqid%253Dfb1867e9001359920000000457870205%2Cr%3A%2Cmon%3Ahttp%3A//m9100.talk99.cn/monitor%2Cp0%3Ahttp%253A//www.jikexueyuan.com/course/',
'connect.sid':'s%3AG2puVGuJs5BUqiA2bHYelRgrhewhecPm.OARu%2FhGz1Db1h5qoi4nW8knC7pUIO3YSoyBmSaJ%2BVKk',
'QINGCLOUDELB':'7e36c8b37b8339126ed93010ae808701d562b81daa2a899c46d3a1e304c7eb2b|V4cCE|V4cCD'

    }


def fit3(url):   
    r=requests.get(url,headers=httphead,cookies=cookies,allow_redirects=1)#,
    s = r.text
    ur = re.findall(r"http://www.jikexueyuan.com/course/[0-9]{2,5}.html", s)
    uv = set()
    for u in ur:
        uv.add(u)
    uv=list(uv)    
    for url in uv:
        fit2(url)


def fit2(url):
    ux = set()
    r=requests.get(url,headers=httphead,cookies=cookies,allow_redirects=1)
    s = r.text
    ur = re.findall(r"http://www.jikexueyuan.com/course/.+?ss=1", s)
    for u in ur:
        ux.add(u)
    ux=list(ux)
    for url in ux:
        fit(url)
    

def fit(url):
    s = list(url)
    e = s[-11]#第几课时
    r=requests.get(url,headers=httphead,cookies=cookies,allow_redirects=1)
    s = r.text
    k = re.findall(r"(?<=<title>).+?(?=</title>)",s)
    mv = re.findall(r"http.+?mp4",s)

    #mkd = os.getcwd()
    r = re.findall(r'a href="http://www.jikexueyuan.com/course/[0-9]{2,4}.html">.+?</a',s)
    if r:
        r =re.findall(r'(?<=>).+?(?=<)',r[-1])
        if r:
            dr = r[-1]
            #mkdr = mkd + '\\' + dr
            mkdr = '.\\' + dr
            if os.path.exists(mkdr)==False:            
                os.mkdir(mkdr)
            

   
    if k:
        inf = re.compile('-极客学院')
        ks = inf.sub('',k[-1])

        if mv:
            url = mv[-1]
            output = mkdr +'\\' + e +"--" + ks + ".mp4"
            thre.download( url, output, blocks=3, proxies={} )



def judge(url):
    if list(url)[-12]=="_":
        print('fit')
        fit(url)
    elif (''.join(url[-4:]))=="html":
        print('fit2')
        fit2(url)
    else:
        fit3(url)
        print('fit3')

        

print('请输入链接地址;',end="")
url = input()

httphead={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

judge(url)

 




