from lxml import html
import requests

def main():

    page = requests.get('http://deshevshe.net.ua/laptop/')
    t = html.fromstring(page.content)

    prices = t.xpath('//div[@class="price important"]/text()')

    print (prices)

if __name__ == '__main__':
    main()