# _*_ coding : utf-8 _*_
# @Time : 025, Oct 25, 2022 17:12
# @Author : feng_land
# @File : cal_week_release
# @Project : test_project

import time,datetime,csv,re

now = datetime.datetime.today()
# 要拉取最近7天释放的币
last_n_days = 7
with open('f023152-2022-10-25.csv','r',encoding='utf-8') as db:
    reader = csv.reader(db)
    # for row in islice(reader,1,None)
    line_no = 0
    for row in reader:
        # last_xdays = now - datetime.datetime.strftime(row[3],'%Y-%m-%d')
        # print(last_xdays)
        if line_no != 0 :
            print(row)
            block_time = datetime.datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')
            last_xdays = now - block_time
            days = int(re.sub(r'(?P<days>^\d{1,3}).*',r'\g<days>',str(last_xdays)))
            print("出块日期距今{}天".format(days))
            if days == 0:
                release_fil = float(row[2]) * 0.25
                print(release_fil)
            elif days < 7:
                release_fil = float(row[2]) * 0.25 + float(row[2]) * 0.75 / 180 * last_n_days - int(row[4])
                print(release_fil)
            elif days < 180:
                release_fil = float(row[2]) * 0.75 / 180 * last_n_days
                print(release_fil)
            else:
                break

        elif line_no == 0:
            line_no = 1
            continue
        else:
            print("error")

