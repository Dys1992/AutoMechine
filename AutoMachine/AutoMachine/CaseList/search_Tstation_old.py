#encoding:utf-8
'''
Created on 2017年12月5日

@author: fy39919
'''
import requests,time,unittest,datetime

class Test(unittest.TestCase):

    def test_xcx_old(self):
         
        airlist = []
        #日志  
        now1 = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        log_file = "./log/T站"+now1+"log.txt"
        logf = open(log_file,"w+")
         
        #航线
        now2 = (datetime.datetime.now() + datetime.timedelta(days = 2))
        flyofftime = now2.strftime("%Y-%m-%d")
        file = './Common/airline.txt'
        f = open(file,'r',encoding='utf-8')
        airline = f.readlines()
        logf.write("********"+now1+"老T站查询接口测试**********\n")
        
        
        for line in airline:
            line1 = line.rstrip('\n')
            airlist = line1.split(",")
            url = "http://cnzhxsrvweixin.17u.cn/FlightWeiXinQueryInfo.ashx?" + "Departure=" + airlist[0] + "&Arrival=" + airlist[
            1] + "&DepartureDate=" + flyofftime + "&userIp=0123456" + "&flat=174" + "&ProductType=1&gettype=0&Force=2"
            req = requests.get(url)

            if req.status_code != 200 :
                logf.write("T站:"+url+"链接无法访问"+"\n\n")

            page = req.text 
           
            #判断返回值是否有FlightInfoSimpleList
            str1 ="FlightInfoSimpleList"
            if page.find(str1)== -1:
                logf.write("T站","FlightInfoSimpleList 未返回"+"\n\n")

            #判断政策
            try:        
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







