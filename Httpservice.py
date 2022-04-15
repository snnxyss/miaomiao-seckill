import hashlib

import requests
import Config
import regionCode


class Seckill:
    Config=Config
    MemberId=""
    cookie={

    }
    baseUrl="https://miaomiao.scmttec.com"
    def __init__(self):
        while True:
            print("""
showList    查看疫苗
                        """)
            shell = input()

            if "showList" == shell:
                regionCode.showcity()
                Config.regionCode = input("请输入地区吗：")
                self.GET_list()

    def skill(self ,seckillid,vaccineIndex,linkmanID,idCard,st):
        """
        :param seckillid:
        :param vaccineIndex:
        :param linkmanID:
        :param idCard:
        :param st:
        :return:
        """
        path=Seckill.baseUrl +"/seckill/seckill/subscribe.do"
        urlparams={
            'seckillid':seckillid,
            'vaccineIndex':vaccineIndex,
            'linkmanID':linkmanID,
            'idCard':idCard,

        }
        exHeader={
            'ecc-hs': Seckill.EccHs(seckillid,st)
        }

        json=requests.get(url=path,params=urlparams,headers=exHeader).json()
        return  json

    # @Config.check
    def GET_list(self):
        """
        获取疫苗列表
        :return:
        """
        header={
        'UserAgent':"Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/1042 MicroMessenger/7.0.15.1680(0x27000F34) Process/appbrand0 WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32",
        'Referer':'https://servicewechat.com/wxff8cad2e9bf18719/2/page-frame.html',
        'request.Accept':"application/json, text/plain, */*",
        "request.Host":"miaomiao.scmttec.com",
        'ContinueTimeout':'2500',
        'Timeout':'2500',
        }
        if Config.regionCode=='':
            print("请先设定区域码")
            return
        else:
            print("getlist: "+Config.regionCode)
        regionCodes=Config.regionCode
        path=Seckill.baseUrl + "/seckill/seckill/list.do"
        urlparam={
            'offset': "0",
            'limit':"100",
            'regionCode': regionCodes
        }
        liste=requests.get(url=path, params=urlparam, headers=header).json()
        print(liste)
        return liste



    def EccHs(self,secKillId,st):
        """

        :param secKillId:
        :param st: 秒杀时间
        :return: 加密方法
        """
        salt="ux$ad70*b"
        memberId=Seckill.MemberId
        md5str=Seckill.Md5hex(secKillId + memberId + st)
        return  Seckill.Md5hex(md5str + salt)




    def Md5hex(self,str):
        """

        :param str:
        :return: 加密方法
        """
        result=""
        self.str=str
        md5=hashlib.md5(str.encode('utf-8')).hexdigest()
        for re in md5:
            result += hex(ord(re))
        return result
