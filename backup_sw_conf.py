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

log_file = pathlib.Path('/root/netmiko.sw/sw_conf_back.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# 交换机名字不能出现"/",否则会无法创建日志文件
ip_list = [
    ['fw1','10.10.10.1'],
]

SW = {
    'device_type': 'hp_comware',
    'username': 'user1',
    'ip': '',
    'password': "password1"
}

for ip_item in ip_list:
    try:
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        file_time = time.strftime("%Y%m%d", time.localtime())
        SW['ip'] =ip_item[1]
        connect = ConnectHandler(**SW)
        #print(log_time + '	Successfully connected to ' + SW['ip'] + "	" + ip_item[0])
        logger.info('Successfully connected to ' + SW['ip'] + "	" + ip_item[0])
        safor = connect.send_command('save force')
        config = connect.send_command('dis cur')
        # fan = connect.send_command('dis fan')
        # 以下可以实现连续执行多条命令
        #commands = ['dis power','dis fan']
        #config = connect.send_config_set(commands)

        # 指定备份文件目录
        file_dir = pathlib.Path('conf_backup1')
        # 如果不存在，则创建
        if not file_dir.exists():
            file_dir.mkdir()
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
