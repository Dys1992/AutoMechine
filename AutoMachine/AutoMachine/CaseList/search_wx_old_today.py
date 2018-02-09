#encoding:utf-8
'''
Created on 2017年12月5日

@author: fy39919
'''
#coding=utf-8
import requests,time,unittest,datetime,json

class Test(unittest.TestCase):

    def test_xcx_old_today(self):
        airlist=[]
        timelist=[]
        now1 = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        log_file = "./log/微信"+now1+"航班log.txt"
        logf = open(log_file,"w+")
        
        #航线
        now2 = datetime.datetime.now()
        flyofftime = now2.strftime("%Y-%m-%d")
        file = './Common/airline.txt'
        filef = open(file,'r',encoding='utf-8')
        airline = filef.readlines()
        
        logf.write("********老微信查询接口测试**********\n\n")
        now3 = now2.strftime("%Y-%m-%d %H-%M")

        for line in airline:
            line1 = line.rstrip('\n')
            airlist = line1.split(",")
            url = 'http://cnzhxsrvweixin4.t.17u.cn/FlightWeiXinQueryInfo.ashx?Departure='+str(airlist[0])+'&Arrival='+str(airlist[1])+'&DepartureDate='+flyofftime+'&userIp=1234567&flat=174&ProductType=1&gettype=0&Force=2'
            req = requests.get(url)
            if req.status_code != 200 :
                logf.write("微信:"+url+"链接无法访问"+"\n\n")

            page = req.text 
            '''
                        获取每个航班的最早时间
             
            '''                    
            new_page = json.loads(page)
  
            for flight in new_page["FlightInfoSimpleList"]:        
                flyofftime = flight["flyOffTime"]
                timelist.append(flyofftime)
         
         
            timelist.sort()
            if timelist[0] < now3:
                logf.write(airlist[0]+airlist[1]+"航班时间早于当前时间\n")
            else:
                logf.write("起飞时间正确：\n")
                logf.write("起飞机场："+airlist[0]+"  降落机场："+airlist[1]+"  当前最早起飞时间："+timelist[0]+"\n")
                
        filef.close()          
        logf.close()       
if __name__ == '__main__':

    unittest.main()







