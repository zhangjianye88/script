
import requests
import sys

WEB_URL = 'http://www.csdn.com/'


def run():
    try:
        page = requests.get(WEB_URL)
        if page.status_code == 200 and page.content.decode("utf-8").find('<title>CSDN-专业IT技术社区</title>') >= 0:
            print("CSDN is working great :)")
        else:
            print("It looks like CSDN is having trouble, some one please take a look at it")
            sys.exit(-1)
    except:
        print("It looks like CSDN is having trouble, some one please take a look at it")
        sys.exit(-1)


if __name__ == '__main__':
    run()