__author__ = 'Archangel'
import os
import shutil
import datetime

dt = datetime.datetime.now()
currentdate = dt.strftime('backup %Y_%m_%d-{%H;%M}')
print(currentdate)
os.makedirs('g:/_backups/_Remastersys/'+currentdate)
#os.mkdir('/media/backup/Backups/_Remastersys/'+currentdate)
dir = 'g:\_backups\\'
names = os.listdir(dir)
print(names)