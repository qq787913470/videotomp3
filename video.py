import requests
#  视频下载  作者pqyang
#只需要修改Cookie值
hd = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "Cookie": "login_sid_t=7e19501307dc737ef37c30cebb085c51; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=8953991044739.6.1577954110366; SINAGLOBAL=8953991044739.6.1577954110366; ULV=1577954110372:1:1:1:8953991044739.6.1577954110366:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWwMvd4fF3MAWXKl06jogDi5JpX5K2hUgL.Fo2cSK-7She7e052dJLoIEqLxK-L1hnL1-zLxK.L1h5LBKWcMEH8Sb-4SFHF1CH8SC-Rxb-415tt; ALF=1609490115; SSOLoginState=1577954116; SCF=AoivvyDyJP8RoHJZu94ae7HauLittFjT3w-jYukkPjtKKeasXe6shDIHPqqIfZ2PHW04abcByFk40Yp3cljhUPM.; SUB=_2A25zCdsUDeRhGedI7lcR9C3MyDyIHXVQf0vcrDV8PUNbmtAKLUujkW9NVzYJMpplmqm6lw58-TxoILsYR74NKxgF; SUHB=0oUpoh9IsYuh3r; un=yangpeiqing2009@sina.com; wvr=6; webim_unReadCount=%7B%22time%22%3A1577954130309%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A2%2C%22allcountNum%22%3A81%2C%22msgbox%22%3A0%7D",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Content - Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive",
        "Referrer Policy": "no-referrer-when-downgrade",
        }
print("开始下载")
url = 'http://play.rumyvideo.com/video/wemedia/60231d8448ab4ce9bd679c24e46da36b/feaf564984fdaa3bcc44a81715e82612-2473070262-2-0-2.mp4?auth_key=1586591927-cebb22a5fdd846398e6b8cd7e439d738-0-d3bbc225b90ba63fcc24cac854863a9d'
r = requests.get(url, headers=hd, stream=True)
#print(r.content)
with open('少年.mp4', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp4.write(chunk)
 
print("下载结束")