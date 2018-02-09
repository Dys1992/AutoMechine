#encoding:utf-8
'''
Created on 2017年12月5日

@author: fy39919
'''
import requests,time,unittest,datetime,json

class Test(unittest.TestCase):

    def test_xcx_old_today(self):
        airlist=[]
        timelist=[]
        now1 = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        log_file = "./log/老APP"+now1+"航班log.txt"
        logf = open(log_file,"w+")
        #航线
        now2 = datetime.datetime.now()
        flyofftime = now2.strftime("%Y-%m-%d")
        file = './Common/airline.txt'
        filef = open(file,'r',encoding='utf-8')
        airline = filef.readlines()
        now3 = now2.strftime("%H-%M")
        
        logf.write("********老APP查询接口测试**********\n\n")
        now3 = now2.strftime("%H-%M")


        for line in airline:
            line1 = line.rstrip('\n')
            airlist = line1.split(",")
            url = "http://cnzhxsrv1.t.17u.cn/FlightQueryInfo.ashx?flat=1&isgzip=1&gettype=0&UserIP=222.92.130.220&appquery={\"OrgAirportCode\":\""+airlist[0]+"\",\"ArrivalAirportCode\":\""+airlist[1]+"\",\"TakeoffBegDate\":\""+flyofftime+"T00:00:00\",\"TakeoffEndDate\":\""+flyofftime+"T00:00:00\",\"SubChannel\":10,\"QueryEngineRoomCodes\":[\"all\"],\"QueryAirCompanyCodes\":[\"all\"],\"SortCondition\":\"11\",\"UserIP\":\"222.92.130.220\",\"QueryChannelRefid\":5866741,\"FlatSubType\":3,\"ConKEY\":\"001010bafea78b6ef8\",\"GoflightTakeoffTime\":\"1900-01-01T00:00:00\",\"FzQuery\":1,\"NoFlightResult\":1,\"QuerySegmentType\":0,\"QueryType\":0,\"FProductID\":0,\"PolicyId\":\"\",\"GoflightGUId\":\"\",\"GoFlightNO\":\"\",\"GoFlightCabinCode\":\"\",\"ProductType\":1}" 
            req = requests.get(url)
            page = req.text 
            '''
                        获取每个航班的最早时间
              
            '''                    
            new_page = json.loads(page)
   
            for flight in new_page["FlightInfoSimpleList"]: 
   
                flyOffOnlyTime = flight["flyOffOnlyTime"]
                timelist.append(flyOffOnlyTime)
             
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







