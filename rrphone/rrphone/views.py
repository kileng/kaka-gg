from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django import forms
import datetime
import json
import re
import pymongo, json

# mghost = 'cd.1tjob.cn'
# mgport = 8484
mghost = '172.19.0.16'
mgport = 27017


def index(request):
    if request.method == 'POST':
        s_User = request.POST.get('user')
        s_Number = request.POST.get('number')
        s_Classes = request.POST.get('classes')
        s_Feiyong = request.POST.get('feiyong')
        s_Company = request.POST.get('company')
        clict = pymongo.MongoClient(host=mghost, port=mgport)
        data = clict.kileng
        table = data.phone
        df = str((datetime.datetime.now() + datetime.timedelta(0)
                  ).strftime("%Y-%m-%d"))
        print(df)
        table.save({
            "_id": s_Number,
            "number": int(s_Number),
            "user": s_User,
            "classes": s_Classes,
            "company": s_Company,
            "feiyong": s_Feiyong,
            "date": df,
        })
        clict.close()
        return HttpResponseRedirect('/')
    else:
        clict = pymongo.MongoClient(host=mghost, port=mgport)
        data = clict.kileng
        table = data.phone
        ssd = table.find().sort([(
            "company", pymongo.DESCENDING), ("classes", pymongo.DESCENDING)])
        clict.close()
    clict.close()
    return render(request, 'index.html', {"title": "手机号填报系统", 'ssd': ssd})


def pag_errow(request):
    page = '''
            _oo0oo_
            088888880
            88" . "88
            (| -_- |)
            0\ = /0
            ___/'---'\___
            .' \\\\|     |// '.
            / \\\\|||  :  |||// \\
            /_ ||||| -:- |||||- \\
            |   | \\\\\\  -  /// |   |
            | \_|  ''\---/''  |_/ |
            \  .-\__  '-'  __/-.  /
            ___'. .'  /--.--\  '. .'___
            ."" '<  '.___\_<|>_/___.' >'  "".
             | | : '- \\'.;'\ _ /';.'/ - ' : | |
            \  \ '_.   \_ __\ /__ _/   .-' /  /
             ====='-.____'.___ \_____/___.-'____.-'=====
             '=---='

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            佛祖保佑    iii    永不死机

'''
    erro = {
        'kee': ' 当你看见我时，说明你要看的这个页面飞了～～',
        'tel': ' 如需查看请联系15828232213',
        'mail': 'hengyoulin@renruihr.com',
    }
    return render(request, "404.html", {'page': page, 'erro': erro})


def pag_no_found(request):
    page = '''
 \          SORRY            /
 \                         /
 \    This page does     /
        ]   not exist yet.    [    ,'|
        ]                     [   /  |
        ]___               ___[ ,'   |
        ]  ]\             /[  [ |:   |
        ]  ] \           / [  [ |:   |
        ]  ]  ]         [  [  [ |:   |
        ]  ]  ]__     __[  [  [ |:   |
        ]  ]  ] ]\ _ /[ [  [  [ |:   |
        ]  ]  ] ] (#) [ [  [  [ :===='
 ]  ]  ]_].nHn.[_[  [  [
 ]  ]  ]  HHHHH. [  [  [
 ]  ] /   `HH("N  \ [  [
 ]__]/     HHH  "  \[__[
 ]         NNN         [
 ]         N/"         [
 ]         N H         [
 /          N           \\
 /           q,           \\
 /                          \\

    '''
    erro = {
        'kee': ' 当你看见我时，说明系统崩了！！',
        'tel': ' 请联系15828232213',
        'mail': 'hengyoulin@renruihr.com',
    }
    return render(request, "404.html", {'page': page, 'erro': erro})


def eport(request):
    tt = pymongo.MongoClient(host=mghost, port=mgport)
    tw = tt.kileng
    tb = tw.wx
    ukt = []
    ut = tb.find()
    for yy in ut:
        # print(yy)
        ukt.append(yy)
    # tryy = json.dumps(ukt)
    # print(tryy)
    return JsonResponse(ukt, safe=False)


def wx(request):
    # iplist=['172.19.0.123','101.204.230.127','172.19.3.53','172.17.11.59']
    # ip = request.META['REMOTE_ADDR']
    # print(ip)
    # if ip not in iplist:
    if request.method == 'POST':
        s_Wxname = request.POST.get('wxname')
        s_Fans = request.POST.get('fans')
        s_City = request.POST.get('city')
        s_Name = request.POST.get('name')
        s_Phone = request.POST.get('phone')
        s_Wxid = request.POST.get('wxid')
        s_Wxfi = request.POST.get('wxfi')
        s_Level = request.POST.get('level')
        s_Entername = request.POST.get('entername')
        clict = pymongo.MongoClient(host=mghost, port=mgport)
        data = clict.kileng
        table = data.wx
        df = str((datetime.datetime.now() + datetime.timedelta(0)
                  ).strftime("%Y-%m-%d"))
        print(df)
        table.save({
            "_id": ''.join(str(s_Wxid).split()),
            "fans": s_Fans,
            "wxname": s_Wxname,
            "city": s_City,
            "name": s_Name,
            "phone": s_Phone,
            "wxid": s_Wxid,
            "wxfi": s_Wxfi,
            "level": s_Level,
            "entername": s_Entername,
            'date': df
        })
        clict.close()
        return HttpResponseRedirect('/wx')
    else:
        clict = pymongo.MongoClient(host=mghost, port=mgport)
        data = clict.kileng
        table = data.phone
        ssd = table.find().sort([(
            "company", pymongo.DESCENDING), ("classes", pymongo.DESCENDING)])
        clict.close()
    clict.close()
    return render(request, 'wx/wx.html', {"title": "手机号填报系统", 'ssd': ssd})
    # else:
    #     return HttpResponseRedirect('/')


def insert(request):
    if request.method == "POST":
        tata = request.FILES.get('tata')
        clict = pymongo.MongoClient(host=mghost, port=mgport)
        data = clict.kileng
        table = data.wx
        df = str((datetime.datetime.now() + datetime.timedelta(0)
                  ).strftime("%Y-%m-%d"))
        for ti in tata.readlines():
            uuk = re.split(",", ti.decode("gbk"))
            print(uuk)
            table.save({
                "_id": ''.join(str(uuk[1]).split()),
                "fans": ''.join(str(uuk[3]).split()),
                "wxname": ''.join(str(uuk[0]).split()),
                "city": ''.join(str(uuk[2]).split()),
                "name": ''.join(str(uuk[4]).split()),
                "phone": ''.join(str(uuk[5]).split()),
                "wxid": ''.join(str(uuk[1]).split()),
                "wxfi": int(''.join(str(uuk[6]).split())),
                "level": 1,
                "entername": ''.join(str(uuk[7]).split()),
                'date': df
            })
        print(tata.name, tata.size)
        return HttpResponseRedirect("/wx/")
    else:
        pass
    return render(request, "insert/insert.html", {"title": "hahahahaha"})


def movie(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'movie/movie_index.html', {"title": "hahahahaha"})


def vvs(request):
    clict = pymongo.MongoClient(host=mghost, port=mgport)
    data = clict.kileng
    table = data.res
    ip = request.META['REMOTE_ADDR']
    print(ip)
    if request.method == 'POST':

        pass
    else:
        if ip in ['172.19.0.1', '101.204.230.127']:
            da = table.find({"city": "cd"})
        elif ip in ["123.157.153.250"]:
            da = table.find({"city": "hz"})
        elif ip in ['220.249.102.70']:
            da = table.find({"city": "wh"})
        else:
            return HttpResponseRedirect("/")

        return render(request, "vvs/vvs.html", {"title": "58什么鬼", 'data': da})


def snow(request):
    if request.method == 'POST':

        pass
    else:
        return render(request, "snow.html", {"title": ""})

def aport(request):
    tt = pymongo.MongoClient(host=mghost, port=mgport)
    tw = tt.kileng
    tb = tw.wx
    ukt = []
    tk = request.GET.get("call")
    ut = tb.find()
    for yy in ut:
        # print(yy)
        ukt.append(yy)
    # tryy = json.dumps(ukt)
    # print(tryy)
    print(json.dumps(ukt))
    return HttpResponse(tk+"("+json.dumps(ukt)+")")