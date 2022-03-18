# Setup Azure Sentinel Agent
## Note: 
1. test networking ability before starting the install
2. Install Ubuntu 18 (it comes preinstalled with a version of Python3 that will work). At the time of this writing the Sentinel Agent will only work with python versions before 3.8. In 3.8 they changed a function or its name for returning Linux distro information and Sentinel has not updated the Agent to reflect that. 

## DNS setup
1. list the interface information
```
nmcli connection show
nmcli connection modify <interface-uuid> ipv4.dns "8.8.8.8,8.8.4.4,1.1.1.1,1.1.0.0"
nmcli
nmcli conn show <interface-uuid> | grep dns:
```


## Update Ubuntu: 
1. sudo apt update && sudo apt upgrade -y && sudo apt install curl wget git net-tools gnutls-bin -y

## Create a symbolic link for /usr/bin/python:
1. cd /usr/bin
2. sudo ln -s python3.6 python

## Install Sentinel Agent: 
```
wget https://raw.githubusercontent.com/microsoft/OMS-Agent-for-Linux/master/installer/scripts/onboard_agent.sh

sudo sh onboard_agent.sh -w <Onboard-ID> -s <Onboard-key> -d <Top-Level-Domain>
```
this info can be found in Sentinel at: Connectors > syslog > open connector page > Install Agent on non-azure Linux Machine > Download & install agent for non-Azure Linux machines > Linux Servers

## Run Troubleshooter to verify that it installed correctly (Good Luck):
```
sudo /opt/microsoft/omsagent/bin/troubleshooter
```
Sometimes this is wrong. Check sentinel logs to verify:
```
Heartbeat | where Computer contains "<Computer-Name>"
Syslog | where Computer contains "<Computer-Name>"
Perf | where Computer contains "<Computer-Name>"
```

## Logfiles to check:
```
/var/opt/Microsoft/omsagent/<workspaceID>/log/omsagent.log
```

### if needed uninstall: 
```
sh onboard_agnet.sh –purge
```

# Setup rsyslogd:
## Server: 
1. sudo nano /etc/rsyslog.conf
unhash the lines:
```
Module(load=”imudp”)	                # tells rsyslog we will be receiving data by UDP
Input(type=”imudp” port=”514”)   	# tells rsyslog we will be receiving data on port 514
Module(load=”imtcp”)	                # tells rsyslog we will be receiving data by TCP
Input(type=”imtcp” port=”514”)   	# tells rsyslog we will be receiving data on port 514
```

2. Add these lines to the bottom of the config:

**NOTE: the quotes used on the $template line cause errors when copy and pasted into a terminal. make sure to retype out the quotes.**
```
*.* @127.0.0.1:514 	
$ActionQueueFileName queue
$ActionQueueMaxDiskSpace 1g
$ActionQueueSaveOnShutdown on
$ActionQueueType LinkedList
$ActionResumeRetryCount -1
$template remote-incoming-logs,”/var/log/%HOSTNAME%/%PROGRAMNAME%.log”
*.* ?remote-incoming-logs
&~
```
Exit nano (ctrl + x) and save the file

3. rsyslog -N1 		# will check the config file for errors. 
4. systemctl restart rsyslog

# Firewall Setup:
1. netstat -ano                    # to see all current tcp/ip connects
2. sudo apt install ufw -y  # install firewall
3. sudo ufw enable
4. sudo ufw status
5. sudo ufw allow 514        #for syslog data
6. sudo ufw allow 80          #for http
7. sudo ufw allow 443        #for https  
8. sudo ufw allow 53          #for dns
9. sudo ufw status

# Client: 
1. sudo nano /etc/rsyslog.conf8.* @192.168.164.7

Add these lines to the bottom of the config:
```
*.* @192.168.100.48:514 	# this is pointing it to our current SyslogRelay Server. Change IP as needed
$ActionQueueFileName queue
$ActionQueueMaxDiskSpace 1g
$ActionQueueSaveOnShutdown on
$ActionQueueType LinkedList
$ActionResumeRetryCount -1
```
Exit nano (ctrl + x) and save the file

2. systemctl restart rsyslog
3. sudo ufw allow out 514    # if needed

# Sentinel: 
Connectors > syslog > open connector page > Install Agent on non-azure Linux Machine > Download & install agent for non-Azure Linux machines > Linux Servers > go to logs

This should bring up a basic heartbeat search for Linux devices to make sure yours is connected. 

Connectors > syslog > open connector page > Open your workspace advanced settings configuration > Linux Performance Counters > Add Defaults > Apply below configuration to my machines

Connectors > syslog > open connector page > Open your workspace advanced settings configuration > Syslog > Apply below configuration to my machines

In the field enter: syslog and click the plus next to it. Add all auth, authpriv, local0, syslog as standard settings. Consider adding more like cron, daemon, etc depending on needs. 

For some reason I can no longer remember I also did:
Connectors > syslog > open connector page > Open your workspace advanced settings configuration > Data > Custom Fields 

Save the settings and make sure everything is correct after the save. 

# Sentinel Logs
## run: Syslog

## Log Searches: Syslog server named SyslogRelay
1.	Heartbeat | where OSType == 'Linux' | summarize arg_max(TimeGenerated, *) by SourceComputerId | sort by Computer | render table
2.	Heartbeat | where OSType == 'Linux' 
3.	Operation | where Computer contains "SyslogRelay"
4.	Alert | where Computer contains "Linux"
5.	Syslog | where HostName contains "LinuxSyslogRelay" | sort by TimeGenerated desc

## Log Searches:  Syslog server named LC01
1.	Heartbeat | where OSType == 'Linux' | summarize arg_max(TimeGenerated, *) by SourceComputerId | sort by Computer | render table
2.	Heartbeat | where OSType == 'Linux' 
3.	Operation | where Computer contains "LC01"
4.	Alert | where Computer contains "Linux"
5.	Syslog | where HostName contains " LC01" | sort by TimeGenerated desc

# Logrotate:
https://support.plesk.com/hc/en-us/articles/360006381154-Logrotate-cron-task-fails-skipping-because-parent-directory-has-insecure-permissions

## Set the correct permissions and ownerships on the parent directories:
```
chmod 755 /var/log/ && chown root:root /var/log/
chmod 755 /var && chown root:root /var
```
Note: if Ubuntu is used, make sure that su root syslog is included into /etc/logrotate.conf file:

```
head /etc/logrotate.conf

# see "man logrotate" for details
# rotate log files weekly
weekly

# use the syslog group by default, since this is the owning group
# of /var/log/syslog.
su root syslog
```



```
sudo nano /etc/logrotat.d/rsyslog
```

https://www.networkworld.com/article/3531969/manually-rotating-log-files-on-linux.html
```
/var/log/syslog
{
	rotate 5
	size 10M
	missingok
	notifempty
	create 0640 syslog adm	
	delaycompress	
	compress
	postrotate
		/usr/lib/rsyslog/rsyslog-rotate
	endscript
}

/var/log/mail.info
/var/log/mail.warn
/var/log/mail.err
/var/log/mail.log
/var/log/daemon.log
/var/log/kern.log
/var/log/auth.log
/var/log/user.log
/var/log/lpr.log
/var/log/cron.log
/var/log/debug
/var/log/message
{
	rotate 5
	size 10M
	missingok
	notifempty
	create 0640 syslog adm
	compress
	delaycompress
	sharedscripts
	postrptate
		/usr/lib/rsyslog/rsyslog-rotate
	endscript
}
```

# Manual log rotation:
```
sudo logrotate -f /etc/logrotate.d/rsyslog
```

