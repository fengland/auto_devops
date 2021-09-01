import time,os,logging
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

file_handler = logging.FileHandler('sw_conf_back.log')
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


ip_list = [
    ['E1-19-S12508G','172.21.10.1'],
    ['E4-E5-45-6520X-jieru','172.21.10.2'],
]

SW = {
    'device_type': 'hp_comware',
    'username': 'wangxufeng',
    'ip': '',
    'password': "123456"
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
        file_name = ip_item[0] + file_time + '-.conf'
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
