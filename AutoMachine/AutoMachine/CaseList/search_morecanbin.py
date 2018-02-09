#encoding:utf-8
'''
Created on 2017年12月5日

@author: fy39919
'''
import requests,time,unittest,datetime,json

class Test(unittest.TestCase):

    def test_xcx_old(self):
         
        airlist = []
        #日志  
        now1 = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        log_file = "./log/扩展舱位"+now1+"log.txt"
        logf = open(log_file,"w")
         
        #航线
        now2 = (datetime.datetime.now() + datetime.timedelta(days = 2))
        flyofftime = now2.strftime("%Y-%m-%d")
        file = './Common/airline.txt'
        f = open(file,'r',encoding='utf-8')
        airline = f.readlines()
        logf.write("********"+now1+"扩展舱位接口测试日志**********\n")
        
        #从微信查询接口获取扩展舱位接口所需字段
        
            
        for line in airline:
            line1 = line.rstrip('\n')
            airlist = line1.split(",")
            url = 'http://cnzhxsrvweixin.17u.cn/FlightWeiXinQueryInfo.ashx?Departure='+str(airlist[0])+'&Arrival='+str(airlist[1])+'&DepartureDate='+flyofftime+'&userIp=1234567&flat=174&ProductType=1&gettype=0&Force=2'
            req1 = requests.get(url)
            #判断微信查询接口是否有返回
            if req1.status_code != 200 :
                logf.write("微信:"+url+"查询接口无法访问"+"\n")
                
            try:        
                #获取微信查询接口返回值   
                page1 = req1.text
                new_page1 = json.loads(page1) 
                #拆分FlightInfoSimpleList节点      
                for flight in new_page1["FlightInfoSimpleList"]:
                    flyOffTime = flight["flyOffTime"]
                    aircompanyCode = flight["airCompanyCode"]
                    flightNo = flight["flightNo"]
                    cabins = flight["cabins"]
                
                    #拆分cabins节点
                    for fz in cabins:
                        fzRuleID = fz["fzRuleID"]
                        productCode = fz["fProductCode"]
                        #加个room
                        realRoomCode = fz["realRoomCode"]
                        isMCE = fz["isMCE"]
                    
                    #判断isMCE字段是否为1,1为有扩展舱位，0为没有扩展舱位    
                        if str(isMCE) == str(1):
                        
                            url1 = 'http://wx.17u.cn/flightnew/json/getflightmorecabin.html?startPort='+airlist[0]+'&endPort='+airlist[1]+'&flyOffDate='+flyofftime+'&aircompanyCode='+aircompanyCode+'&flightNo='+flightNo+'&productCode='+str(productCode)+'&fzRuleId='+str(fzRuleID)+'&productType=1'
                            req3 = requests.get(url1)  

                            if req3.status_code != 200 :
                                logf.write("微信扩展舱位接口无法访问,链接："+url1+"\n\n")  
                                
                                #判断返回值是否有FlightInfoSimpleList
                            page3 = req3.text
                            new_page3 = page3.replace('\\', '')
                            
                            str1 ="\"isMCE\":1"
                            if new_page3.find(str1)== -1:
                                logf.write("Book1.5没有扩展舱位：\n")
                                logf.write("航线:"+airlist[0]+"-"+airlist[1]+" 起飞时间:"+flyOffTime+" 航司："+aircompanyCode+" 舱位："+realRoomCode+"\n"+page3+"\n\n\n")
                                logf.write(url1+"\n\n")
                            else:
                                logf.write("航线:"+airlist[0]+"-"+airlist[1]+" 起飞时间:"+flyOffTime+" 航司："+aircompanyCode+" 舱位："+realRoomCode+"Book1.5有扩展舱位：\n\n")

            finally:
                logf.write("********本次扩展舱位接口测试结束**********\n") 
        
        
                                 
        logf.close()
        f.close()
                
if __name__ == '__main__':

    unittest.main()               