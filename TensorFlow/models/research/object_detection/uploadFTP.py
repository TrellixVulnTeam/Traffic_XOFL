from ftplib import FTP 
import os
import sys
import fileinput
import requests 


ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('files.000webhost.com', 21) 
ftp.login('sociodroid','Test1234!')
 
file_name=sys.argv[1]

file = open(file_name,'rb')                  # file to send
ftp.storbinary('STOR /public_html/detected_images/'+file_name, file)     # send the file
file.close()                                    # close file and FTP
ftp.quit()




with open('out.txt', 'r') as f:
            plate = f.readline()
link="https://sociodroid.000webhostapp.com/triggerSMS.php?license="+plate
print (link)
r = requests.get(link)

print (r.text)