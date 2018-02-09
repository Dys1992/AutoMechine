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
        log_file = "./log/老APP"+now1+"log.txt"
        logf = open(log_file,"w")
         
        #航线
        now2 = (datetime.datetime.now() + datetime.timedelta(days = 2))
        flyofftime = now2.strftime("%Y-%m-%d")
        file = './Common/airline.txt'
        f = open(file,'r',encoding='utf-8')
        airline = f.readlines()
        logf.write("********"+now1+"老APP查询接口测试**********\n")
        
        
        for line in airline:
            line1 = line.rstrip('\n')
            airlist = line1.split(",")
            url = "http://cnzhxsrv1.t.17u.cn/FlightQueryInfo.ashx?flat=1&isgzip=1&gettype=0&UserIP=222.92.130.220&appquery={\"OrgAirportCode\":\""+airlist[0]+"\",\"ArrivalAirportCode\":\""+airlist[1]+"\",\"TakeoffBegDate\":\"2017-12-31T00:00:00\",\"TakeoffEndDate\":\""+flyofftime+"T00:00:00\",\"SubChannel\":10,\"QueryEngineRoomCodes\":[\"all\"],\"QueryAirCompanyCodes\":[\"all\"],\"SortCondition\":\"11\",\"UserIP\":\"222.92.130.220\",\"QueryChannelRefid\":5866741,\"FlatSubType\":3,\"ConKEY\":\"001010bafea78b6ef8\",\"GoflightTakeoffTime\":\"1900-01-01T00:00:00\",\"FzQuery\":1,\"NoFlightResult\":1,\"QuerySegmentType\":0,\"QueryType\":0,\"FProductID\":0,\"PolicyId\":\"\",\"GoflightGUId\":\"\",\"GoFlightNO\":\"\",\"GoFlightCabinCode\":\"\",\"ProductType\":1}"               
            req = requests.get(url)

            if req.status_code != 200 :
                logf.write("APP:"+url+"链接无法访问"+"\n\n")

            page = req.text 
        
       #判断返回值是否有FlightInfoSimpleList
            str1 ="FlightInfoSimpleList"
            if page.find(str1)== -1:
                logf.write("APP","FlightInfoSimpleList 未返回"+"\n\n")
            try:
            #判断政策
                
                str1 ="\"pt\":1"
                str2 = "\"pt\":21"
                str3 = "\"pt\":40"
                str4 = "\"pt\":41"
                str5 = "\"pt\":45"
                str6 = "\"pt\":60"
                if page.find(str1)== -1:
                    logf.write(airlist[0]+airlist[1]+"1政策未返回\n\n")
                else:
                    logf.write(airlist[0]+airlist[1]+"1政策正确返回\n\n")
                if page.find(str2)== -1:
                    logf.write(airlist[0]+airlist[1]+"21政策未返回\n\n")
                else:
                    logf.write(airlist[0]+airlist[1]+"21政策正确返回\n\n")
                if page.find(str3)== -1:
                    logf.write(airlist[0]+airlist[1]+"40政策未返回\n\n")
                else:
                    logf.write(airlist[0]+airlist[1]+"40政策正确返回\n\n")
                if page.find(str4)== -1:
                    logf.write(airlist[0]+airlist[1]+"41政策未返回\n\n")
                else:
                    logf.write(airlist[0]+airlist[1]+"41政策正确返回\n\n")
                if page.find(str5)== -1:
                    logf.write(airlist[0]+airlist[1]+"45政策未返回\n\n")
                else:
                    logf.write(airlist[0]+airlist[1]+"45政策正确返回\n\n")
                if page.find(str6)== -1:
                    logf.write(airlist[0]+airlist[1]+"60政策未返回\n\n")
                else:
                    logf.write(airlist[0]+airlist[1]+"60政策正确返回\n\n")
                    
                logf.write(page+"\n\n")
            finally:
                return 1
            
        f.close()          
        logf.close()

     
if __name__ == '__main__':

    unittest.main()







