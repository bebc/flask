import subprocess
import threading
import paramiko

def cmd(web_project,host,deploy_version):

    def run_command(host,cmd):
        stdin,stdout,stderr = ssh.exec_command(cmd)
        error = stderr.read().decode('utf-8')
        if error !='':
            return (host+':'+error)
        else:
            return (host+':'+stdout.read().decode('utf-8'))

    tomcat_path = '/opt/tomcat7'+web_project
    cmd = 'scp /data/'+web_project+'-web.war '+host+':/webapps/run'
    cmd_mv = 'cp -rf /webapps/run/'+web_project+'-web /webapps/runBak/'+web_project+'-web-'+deploy_version
    cmd_zip = 'unzip -od /webapps/run/'+web_project+'-web /webapps/run/'+web_project+'-web.war'
    cmd_kill = "ps -ef|grep "+web_project+"|grep -v grep |awk '{print $2}'|xargs kill -9"
    cmd_start = 'source /etc/profile;bash '+tomcat_path+'/bin/startup.sh'
    child = subprocess.check_output(cmd,shell='true')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,timeout=10)
    run_command(host,cmd_mv)
    run_command(host,cmd_zip)
    run_command(host,cmd_kill)
    run_command(host,cmd_start)
    ssh.close()

def run_thread(hosts):

    for host in hosts:
        try:
            sthread = threading.Thread(target=cmd, args=('polaris', host, 'test123',))
            sthread.start()
        except Exception as e:
            return e