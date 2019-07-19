# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:04:38 2019
@author: yyn
"""
import requests
import time

url='https://map.baidu.com/?'
cid=159#本地城市所在ID
loc='112.69125,26.888519'#本地坐标
exptime='2019-05-24 13:13'#预计出发时间
sn='1$$$$12544912,3089949$$0$$$$'#出发坐标
en='1$$$$12958170.8639,4825779.76939$$0$$$$'#目的坐标
data=[
    'newmap=1',
    'reqflag=pcmap',
    'biz=1',
    'from=webmap',
    'da_par=direct',
    'pcevaname=pc4.1',
    'qt=bt',
    'c=%s'%cid,
    'sn=%s'%sn,
    'en=%s'%en,
    'sc=%s'%cid,
    'ec=%s'%cid,
    'pn=0',
    'rn=5',
    'exptype=dep',
    'version=5',
    'tn=B_NORMAL_MAP',
    'ie=utf-8',
    'exptime=%s'%exptime,
    'u_loc=%s'%loc,
]
url+='&'.join(data)
print(url)
response=requests.get(url)
Result=response.json()
for x in Result['content']:
    names,times,distances,walk_distances,infos=[],[],[],[],[]
    for i in x['lines']:
        names.append(i[0]['name'])
        times.append(str(i[2]))
        distances.append(str(i[1]))
        walk_distances.append(str(i[4]))
    for i in x['stops'][0]:
        info=[[i['getOff']['name'],i['getOn']['name']],[i['walk']['distance'],i['walk']['time']]]
        infos.append(info)
    print('/'.join(names))
    print('/'.join(times),'/'.join(distances),'/'.join(walk_distances))
    print(infos)
    break
    
    
    
#https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=walk&version=2.0&walktp=1&c=159&wdrag=0&sc=159&ec=159&sy=0&en=1$$$$12544711.88,3089370.6$$%E6%B9%96%E5%8D%97%E5%B7%A5%E5%AD%A6%E9%99%A2$$$$$$&sn=1$$$$12544929,3089974$$%E6%88%91%E7%9A%84%E4%BD%8D%E7%BD%AE$$$$$$&sq=%E6%88%91%E7%9A%84%E4%BD%8D%E7%BD%AE&eq=%E6%B9%96%E5%8D%97%E5%B7%A5%E5%AD%A6%E9%99%A2&region=0&tn=B_NORMAL_MAP&nn=0&auth=y908dw1C3%3DxdSA33LS9%3D4FSy2d6Ox1RCuxHHHNHxVRBtAmk5zC88yy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuBNtg3yw8mdwJL4ORUY9cf0IcEWe1GD8zv7u%40ZPuVtcvY1SGpuxxtoE41hjzgjyBKKKQHDQHHxhl44yBWxIookK0&u_loc=12544929,3089974&ie=utf-8&l=14&b=(12529829.334367093,3087337.199493671;12548892.358164556,3092028.4905063286)&t=1555751085364
    
    
    
    $ajax({
      method: 'get',
      url: 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=bt&c=159&sn=1$$$$12544912,3089949$$0$$$$&en=1$$$$12958170.8639,4825779.76939$$0$$$$&sc=159&ec=159&pn=0&rn=5&exptype=dep&version=5&tn=B_NORMAL_MAP&ie=utf-8&exptime=2019-06-4 13:13&u_loc=112.69125,26.888519',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      // data: {
      //   end: "我的目的地",
      //   endAddrX: bLng,
      //   endAddrY: bLat,
      //   endCid: code2,
      //   start: "我的出发地",
      //   startAddrX: aLng,
      //   startAddrY: aLat,
      //   startCid: code,
      //   startDate: c+""+q
      // }
    }).then(function (res) {
      console.log(res);
      // sessionStorage.setItem('plan',JSON.stringify(res.data.downListInfo));
      // that.$router.push({
      //   path:'/search_alike',
      //   query:{res2:[locate,locate2,c]}
      // });
    }).catch(function (err) {
      alert(err);
    });
    

https://map.baidu.com/?qt=bt&c=159&sc=159&ec=159&pn=0&rn=5&exptype=dep&version=5&u_loc=12544762,3090204&ie=utf-8&sn=1$$$$12544762,3090204$$我的位置$$0$$$$&en=1$$$$12547400.05,3091623.28$$高铁衡阳东站$$0$$$$&exptime=2019-06-03 18:13
    
    
    
    
https://map.baidu.com/?

newmap=1&
reqflag=pcmap&
biz=1&
from=webmap&
da_par=direct&
pcevaname=pc4.1&
qt=bt&
c=159&
sn=1$$$$12544912,3089949$$0$$$$&
en=1$$$$12958170.8639,4825779.76939$$0$$$$&
sc=159&
ec=159&
pn=0&
rn=5&
exptype=dep&
version=5&
tn=B_NORMAL_MAP&
ie=utf-8&
exptime=2019-06-4 13:13&
u_loc=112.69125,26.888519
    

https://map.baidu.com/?
newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=bt&
c=159&sn=1$$$$12544912,3089949$$0$$$$&en=1$$$$12958170.8639,4825779.76939$$0$$$$&sc=159&ec=159&pn=0&rn=5&exptype=dep&version=5&tn=B_NORMAL_MAP&ie=utf-8&exptime=2019-05-24%2013:13&u_loc=112.69125,26.888519
    
    
url='https://map.baidu.com/?'
cid=159#本地城市所在ID
loc='112.69125,26.888519'#本地坐标
exptime='2019-05-24 13:13'#预计出发时间
sn='1$$$$12544912,3089949$$0$$$$'#出发坐标
en='1$$$$12958170.8639,4825779.76939$$0$$$$'#目的坐标
    
    
