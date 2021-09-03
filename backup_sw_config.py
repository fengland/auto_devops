import time,os,logging,pathlib
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import NetmikoAuthenticationException



logger = logging.getLogger('test')
logger.setLevel(level=logging.DEBUG)
#logging.basicConfig(formatter='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    #level = logging.DEBUG,
                    #filename='sw_conf_back.log',
                    #filemode='a')
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

log_file = pathlib.Path('sw_conf_back.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


ip_list = [
    ['E1-19-S12508G','172.21.10.1'],
    ['E4-E5-45-6520X-jieru','172.21.10.2'],
    ['E8-E9-45-6520X-jieru','172.21.10.3'],
    ['ZJ-JH-YX-2#401_E12_E13U45-SA6520X-BEISHOU','172.21.10.4'],
    ['F02-F03-45-6520X-jieru','172.21.10.5'],
    ['F6-F7-45-6520X-jieru','172.21.10.6'],
    ['F10-F11-45-6520X-jieru','172.21.10.7'],
    ['F14-F15-45-6520X-jieru','172.21.10.8'],
    ['E16-45-5130-jieru','172.21.10.9'],
    ['D16-45-5130-jieru','172.21.10.10'],
    ['ZJ-JH-YX-2#401_G03U45-SA6520X-CASH','172.21.10.11'],
    ['ZJ-JH-YX-2#401_G06_G07U45-SA6520X-CASH','172.21.10.12'],
    ['ZJ-JH-YX-2#401_J11_J12U45-SA6520X-KOREA','172.21.10.33'],
    ['ZJ-JH-YX-2#401_J15U45-S6520X-PADENG','172.21.10.34'],
    ['ZJ-JH-YX-2#401_D09U45-SA6520X-TZ','172.21.10.35'],
    ['ZJ-JH-YX-2#401_G10_G11U45-SA6520X-TZ','172.21.10.36'],
    ['ZJ-JH-YX-2#401_G13_G14U45-SA6520X-YUANQUAN','172.21.10.51'],
    ['ZJ-JH-YX-2#401_H12U45-SA6520X-YUANQUAN','172.21.10.52'],
    ['ZJ-JH-YX-2#401_I16U45-SA6520X-ZAB','172.21.10.53'],
]

SW = {
    'device_type': 'hp_comware',
    'username': 'wangxufeng',
    'ip': '',
    'password': "WXF2017.cn"
}

for ip_item in ip_list:
    try:
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file_time = time.strftime("%Y%m%d", time.localtime())
        SW['ip'] =ip_item[1]
        connect = ConnectHandler(**SW)
        #print(log_time + '	Successfully connected to ' + SW['ip'] + "	" + ip_item[0])
        logger.info('Successfully connected to ' + SW['ip'] + "	" + ip_item[0])
        config = connect.send_command('dis cur')
        fan = connect.send_command('dis fan')
        file_dir = pathlib.Path() / "conf_backup"
        file_base_name = ip_item[0] + '-' + file_time + '.conf'
        file_name = file_dir / file_base_name
        with open(file_name,'a') as f:
            f.write(config)
    except (EOFError,NetmikoTimeoutException):
        #print(log_time + "	Can not connect to Device  " + SW['ip'] + "	" + ip_item[0])
        logger.error("Can not connect to Device  " + SW['ip'] + "	" + ip_item[0])
    except (EOFError,NetmikoAuthenticationException):
        #print( SW['ip'] + 'username/password wrong!')
        logger.error(SW['ip'] + 'username/password wrong!')
    except (ValueError,NetmikoAuthenticationException):
        #print(SW['ip'] + '  enable password wrong!')
        logger.error(SW['ip'] + 'enable password wrong!')
    except (KeyboardInterrupt):
        logger.info("process exit by ctrl + c")
        exit()
