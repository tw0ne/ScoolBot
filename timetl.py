from datetime import datetime, date, time
import datetime
import time 
import os 

while True:
      infile = open('file2.txt', 'r')
      data = infile.read()
      if data == ('-'):
            b = datetime.time(9,15,0,0)
            texter = ('🕒 Время до школы (Нет 1го урока !) :' + '\n')
      if data == ('--'):
            b = datetime.time(10,0,0,0)
            texter = ('🕒 Время до школы (Нет 2го урока !) :' + '\n')
      else:
            b = datetime.time(8,20,0,0)
            texter = ('🕒 Время до школы :' + '\n')
      
      a = datetime.datetime.now().time()
      d1 = datetime.timedelta(hours=a.hour, minutes=a.minute, seconds=a.second)
      d2 = datetime.timedelta(hours=b.hour, minutes=b.minute, seconds=b.second)
      result = str(d2-d1)
      result = result.replace("-1 day,", "")
      print(result)
      print(data)
      print(b)
      time.sleep(3)
      wp = datetime.datetime.now()
      wp2 = datetime.datetime(2016, 5, 25, 0, 0)
      wpf = wp2 - wp
      wpf = str(wpf)
      spliter = ('\n')
      texterwp = ('🔥 Время до выпускного:')
      wpf = wpf.replace('days', 'дней')
      f = open('time.txt', 'w')
      f.write(texter)
      f.write(result)
      f.write(spliter)
      f.write(texterwp)
      f.write(spliter)
      f.write(wpf)
      f.close()
      time.sleep(3)




