
def IsWebPageOnServer(webSite):    
    import requests
    webSite = 'https://the-radio.ru/playlist/maximum-r962'
    try:
        requests.get(webSite)
    except:
        print('Нет доступа к веб-сайту из интернета')
        return False
    else:
        print('Можно посылать запросы на сайт')
        return True
    
def VerifySSL(webSite):
    import requests
    try:
        requests.get(webSite, verify=True)
    except:
        print('Нет сертификата')
        return False
    else:
        print('Есть сертификат')
        return True

def Ex3():
    import requests
    webSite = 'https://python.org'
    if(IsWebPageOnServer(webSite) and VerifySSL(webSite)):
        response = requests.get(webSite)

        print("Status Code: ", response.status_code)
        print("Headers: ", response.headers)
        print("Url: ", response.url)
        print("History: ", response.history)
        print("Encoding: ", response.encoding)
        print("Reason: ", response.reason)
        print("Cookies: ", response.cookies)
        print("Elapsed: ", response.elapsed)
        print ("Request: ", response.request)
        print("Content: ", response._content)

def Ex4():
    import requests

    response = requests.get("https://en.wikipedia.org/robots.txt")
    text = response.content

    print("robots.txt from http://www.wikipedia.org/")
    print("============================== =====================")
    print(text)

def Ex5():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen('http://www.example.com/')
    bsh = BeautifulSoup(html.read(), 'html.parser')
    print(bsh.h1.text)

def Ex6():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
    bsh = BeautifulSoup(html.read(), 'html.parser')
    titles = bsh.find_all(['h1', 'h2','h3','h4','h5','h6'])
    for element in titles:
        print(element.text)

def Ex7():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("https://en.wikipedia.org/wiki/Python")
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])

def Ex8():
    import pandas
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv"
    data = pandas.read_csv(url, sep=',', encoding='utf-8', )
    print(len(data))

#def Ex9():
    #403 ошибка выходит((
    
def Ex10_1():
    import requests
    # SOAP URL
    url = "http://www.dneonline.com/calculator.asmx"
    # structured XML
    payload = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <Subtract xmlns="http://tempuri.org/">
        <intA>5</intA>
        <intB>5</intB>
        </Subtract>
    </soap:Body>
    </soap:Envelope>"""
    # headers
    headers = {
    'Content-Type: text/xml; charset=utf-8'
    }
    # POST запрос
    response = requests.request("POST", url, headers=headers, data=payload)
    # ответ
    print(response.text)
    print(response)


def Ex10_1():
    import requests
    # SOAP URL
    url = "http://www.dneonline.com/calculator.asmx"
    # structured XML
    payload = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <Subtract xmlns="http://tempuri.org/">
        <intA>5</intA>
        <intB>5</intB>
        </Subtract>
    </soap:Body>
    </soap:Envelope>"""
    # headers
    headers = {
    'Content-Type: text/xml; charset=utf-8'
    }
    # POST запрос
    response = requests.request("POST", url, headers=headers, data=payload)
    # ответ
    print(response.text)
    print(response)