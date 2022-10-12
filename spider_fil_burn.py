import requests,json
import time,datetime
import csv
import threading
from lxml import etree

headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Mobile Safari/537.36 Edg/102.0.1245.44'
}

check_url='https://filfox.info/api/v1/address/f023152/transfers?pageSize=20&page=37'

#base_url = 'https://filfox.info/zh/address/'

#page = 0


def get_one_page(url):
    html = requests.get(url,headers=headers).text
    html1 = json.loads(html)
    print(html1)
    time.sleep(5)
    try:
        for k,v in html1.items():
            # print(k,v)
            csv_list = []
            for transfer in html1['transfers']:
                if type(transfer['value']) == type('a') :
                    transfer['value'] =  float(transfer['value']) / (10 ** 18)
                    transfer['value'] = float('%.4f' % transfer['value'])
                #print(transfer['value'])
                # date_stamp = datetime.datetime.fromtimestamp(list1['timestamp'])
                # list1['timestamp'] = datetime.datetime.strftime(date_stamp, "%Y-%m-%d %H:%M:%S")
                try:
                    time_array = time.localtime(transfer['timestamp'])
                    transfer['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                except Exception as e:
                    pass
                if  transfer['type'] == 'burn':
                    #print(transfer)
                    csv_list.append('height')
                    csv_list.append(transfer['height'])
                    csv_list.append('timestamp')
                    csv_list.append(transfer['timestamp'])
                    csv_list.append('from')
                    csv_list.append(transfer['from'])
                    csv_list.append('to')
                    csv_list.append(transfer['to'])
                    csv_list.append('value')
                    csv_list.append(transfer['value'])
                    csv_list.append('type')
                    csv_list.append(transfer['type'])
                    #print(csv_list)
                    with open(miner_id + '_burn.csv','a',encoding='utf-8',newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(csv_list)
                    csv_list.clear()
    except Exception as e:
        print(e)
# items=etree.HTML(html,etree.HTMLParser())
# source_code = items.xpath('//*[@id="__layout"]/div/div[1]/div[1]/div/div[7]/div[2]/table/tbody/tr[1]/td[6]')

if __name__ == '__main__':
    #get_one_page(url)
    base_url = 'https://filfox.info/api/v1/address/'

    size = '/transfers?pageSize=20&page='
    miners = ['f023152', 'f0159883', 'f079426', 'f0159632', 'f0134006', 'f0111584', 'f01713152', 'f01735897', 'f0422266', 'f0418086', 'f0832131', 'f01211859', 'f01146045', ]

    # url = base_url + miner_id + size
    for miner_id in miners:
        print('spiding miner {}'.format(miner_id))
        for page in range(30):
            url = base_url + miner_id + size + str(page)
            print('第{}页'.format(page))
            print(url)

            #get_one_page(base_url + miner_id + str(page))

            get_one_page(url)





