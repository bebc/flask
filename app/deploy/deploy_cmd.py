from app import app
import subprocess
import threading
import paramiko

def cmd(web_project,host,deploy_version):

    def run_command(host,cmd):
        stdin,stdout,stderr = ssh.exec_command(cmd)
        error = stderr.read().decode('utf-8')
        if error !='':
            app.logger.info(error)
            return (host+':'+error)
        else:
            return (host+':'+stdout.read().decode('utf-8'))

    tomcat_path = '/opt/tomcat7'+web_project
    cmd_mkdir = 'mkdir -p /webapps/upload/'+deploy_version
    cmd_scp = 'scp /data/files/'+web_project+'-web.war '+host+':/webapps/upload/'+deploy_version
    cmd_rm = 'rm -rf /data/files/'+web_project+'-web.war'
    cmd_cp = 'cp -rf /webapps/run/'+web_project+' /webapps/runBak/'+web_project+'-web-'+deploy_version
    cmd_zip = 'unzip -od /webapps/run/'+web_project+' /webapps/upload/'+deploy_version+'/'+web_project+'-web.war'
    cmd_kill = "ps -ef|grep "+web_project+"|grep -v grep |awk '{print $2}'|xargs kill -9"
    cmd_start = 'source /etc/profile;bash '+tomcat_path+'/bin/startup.sh'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,timeout=10)
    run_command(host,cmd_mkdir)
    app.logger.info(host + ":开始传包...")
    try:
        child = subprocess.check_output(cmd_scp, shell='true')
    except Exception as e:
            return e
    app.logger.info(host+":开始部署...")
    cp_info = run_command(host,cmd_cp)
    zip_info = run_command(host,cmd_zip)
    kill_info = run_command(host,cmd_kill)
    start_info = run_command(host,cmd_start)
    app.logger.info(start_info)
    ssh.close()
    subprocess.check_output(cmd_rm, shell='true')

def run_thread(hosts):

    for host in hosts:
        try:
            sthread = threading.Thread(target=cmd, args=('polaris', host, 'test123',))
            sthread.start()
        except Exception as e:
            return e