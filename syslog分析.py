import glob
import re
def log_chuli(line):
    def minglingchuli(line): #命令处理框
        match = re.search(r':Recorded command information. *',line) #匹配是否运行了命令，如果匹配到将继续匹配，用户名，IP地址，执行的命令
        if match:
            #print(line)
            datetime_match = re.search(r'(\w+\s+\d+\s+\d{4}\s+\d{2}:\d{2}:\d{2})', line)
            task_match = re.search(r'Task=(\w+)', line)
            user_match = re.search(r'User=([^,]+)', line)
            ip_match = re.search(r'Ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            ip = ip_match.group(1) if ip_match else None
            command_match = re.search(r'Command="([^"]+)"',line)
            print(datetime_match.group(1),task_match[1],user_match[1],ip,command_match[1])
    def login_chuli(line):
        match = re.search(r':The user succeeded in logging in to VTY0. *', line)
        if match:
            user_match = re.search(r'UserName=([^,]+)', line)
            UserType_match =  re.search(r'UserType=([^,]+)', line)
            ip_match = re.search(r'Ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            ip = ip_match.group(1) if ip_match else None
            print('用户',user_match.group(1),'使用IP',ip,'通过',UserType_match.group(1),'登录成功')
        match =  re.search(r':Failed to login. *', line)
        if match:
            user_match = re.search(r'UserName=([^,]+)', line)
            UserType_match =  re.search(r'UserType=([^,]+)', line)
            UserType = ip_match.group(1) if UserType_match else None
            ip_match = re.search(r'Ip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            ip = ip_match.group(1) if ip_match else None
            print('用户',user_match.group(1),'使用IP',ip,'通过',UserType,'登录失败')





    minglingchuli(line=line)
    login_chuli(line=line)
# 获取匹配的日志文件列表
log_files = glob.glob('*syslog.log')
for log_file in log_files :
    with open(log_file, 'r') as file:
        # 逐行读取日志内容
        for line in file:
            log_chuli(line=line)
