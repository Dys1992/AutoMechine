#encoding:utf-8
'''
Created on 2017年12月5日

@author: fy39919
'''
import requests,time,unittest,datetime,json,re

class Test(unittest.TestCase):

    def test_xcx_old_today(self):
        airlist=[]
        now1 = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        log_file = "../log/NEW_QQ"+now1+"航班log.txt"
        logf = open(log_file,"w+")
        
        #航线
        now2 = datetime.datetime.now()
        flyofftime = now2.strftime("%Y-%m-%d")
        file = '../Common/airline.txt'
        filef = open(file,'r',encoding='utf-8')
        airline = filef.readlines()
        
        logf.write("********新APP查询接口测试**********\n\n")
        now3 = now2.strftime("%Y-%m-%d %H-%M")

        for line in airline:
            line1 = line.rstrip('\n')
            airlist = line1.split(",")
            url = "http://wx.17u.cn/qqflightnew/json/getflightlist.html?"+"SearchDate="+flyofftime+"&ArriveAirportCode="+airlist[0]+"&OriginAirportCode="+airlist[1]+"&GetType=0&Plat=519&OpenId=&IsNewQuery=1"
            req = requests.get(url)
            if req.status_code != 200 :
                logf.write("NEW_QQ:"+url+"链接无法访问"+"\n\n")

            page = req.text 
            
            '''
                        获取每个航班的最早时间
             
            '''                    
            str1 = page.replace('\\', '')            
            timelist = re.findall('{\"flyOffTime\":\"(.+?)\",\"flyOffOnlyTime\":',str1)
                 
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







