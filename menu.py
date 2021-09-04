import os
import getpass as gp 
import pyttsx3 as txt
import subprocess

# JSON used to get specific value from JSON formate
import json

# in Time module sleep is used to wait for few seconds
import time

import speech_recognition as sr

os.system("tput setaf 120")
os.system("clear")
password = gp.getpass("\n\n\t\tEnter Password: ")

#can run in root account only to use in another account update to 'sudo'
#14  blue  - for neutral
#12  light blue - for what had done
#120 green - for output
#11  yellow - for ask and warn and continue
#9   red   - for wrong input
#7   white - for exit normal
#5   purple - for create note

while True:
	os.system("clear")
	

	if password=="menu":
		os.system("tput setaf 14")
		print("\t\t\t\t\t\t\t      Welcome to My Menu !")
		print("\t\t\t\t\t\t          ---------------------------")
		os.system("tput setaf 11")

		login=input("\n\t\tWhere you want to run this menu? (local(l)/remote(r)) (q to quit): ")
		print("")
		
		if login=="l":
			print('''
		press 1: To run date. 
		press 2: To run cal.
		press 3: To Configure webserver. 
		press 4: To Create New User.
		press 5: To Configure yum in RHEL8 .
		  [Note 5: will only work on -->rhel-8.0-x86_64-dvd.iso(iso file link provided while run.)]
		press 6: To Make Fullscreen RHEL8 in Oracle_Virtual_Box.
		  [Note 6: yum will also be configured and it will only work on -->rhel-8.0-x86_64-dvd.iso(iso file link provided while run.)]
		press 0: To exit.
			''')
			print('')
			ch=int(input("Enter your choice: "))
			print("")

			os.system("tput setaf 120")
			if ch==1:
				os.system("date")
			elif ch==2:
				os.system("cal")
			elif ch==3:
				os.system("yum install httpd")
				os.system("tput setaf 12")
				print('\nInstallation Done.')

				os.system("tput setaf 120")
				print("\nType content of webpage (after Done Enter key-->[Right [Ctrl]+C]):")
				os.system("cat > /var/www/html/autoweb.html")
				os.system("tput setaf 12")
				print('\nhtml page created.')

				#do service permenant uing :(search in book)
				os.system("tput setaf 120")
				os.system("systemctl start httpd")
				os.system("tput setaf 12")
				print('\nhttpd server activated.')

				os.system("tput setaf 120")
				os.system("systemctl stop firewalld")
				os.system("tput setaf 12")
				print('\nfirewall off.')

				os.system("tput setaf 120")
				ip1=input("Enter IP : ")
				os.system("tput setaf 12")
				print('\nGot IP\n')

				os.system("tput setaf 120")
				print(f"Now open URL -->[http://{ip1}/autoweb.html] in any web browser !")
				os.system("tput setaf 12")
				print('\nWebServer Configuration Done!')


			
			elif ch==4:

				os.system("tput setaf 120")
				user_name = input("\nEnter user name you wish to give : ")
				os.system(f"useradd {user_name}")

				os.system("tput setaf 120")
				user_password = input("\nEnter password: ")
				os.system(f"passwd {user_password}")

				os.system("tput setaf 11")
				print(f"\nNew user {user_name} is successfully Create ! ")

				#clear bug : if user want to hide pass

			elif ch==5:
				#bug : only run if autoyum.repo file is present in current os.
				os.system("tput setaf 5")
				print("\nDrive link for RHEL8 iso file:")
				os.system("tput setaf 7")	
				print(f"\n-->[https://drive.google.com/file/d/1nZVXCVOy41LjAyOAiHMcNgFIwUlJYw16/view]")
				os.system("tput setaf 5")
				print("\nCheck in VM : Devices > Optical Drives > rhel-8.0-x86_64-dvd.iso (should be tick).")
				print("\nThis yum Configuration will contain software which are present in RHEL8 iso image, docker, and epel-release-latest-8. ")
				os.system("tput setaf 9")
				print("\nNote: Docker is from online repository. So, site might be low sometime. \n")
				os.system("tput setaf 11")
				input("Press Enter to continue.")
				#clear bug if not to continue then go to login l or r page.
				print("\n")
				os.system("tput setaf 120")
				os.system("cd /run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/")
				os.system("cp /root/auto_yum_repo/autoyum.repo    /etc/yum.repos.d/")
				os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
				os.system("yum repolist")
				os.system("tput setaf 12")
				print("\nyum Configuration Done!")

			elif ch==6:
				#clear bug! : mount and unmount dvd of rhel8 and guest cd image and how to reboot os using cli.
				#bug : only run if autoyum.repo file is present in current os.
				os.system("tput setaf 5")
				print("First you have to set your video memory to 128 mb [settings > Display > video memory]")
				os.system("tput setaf 5")
				print("\nDrive link for RHEL8 iso file:")
				os.system("tput setaf 7")	
				print(f"\n-->[https://drive.google.com/file/d/1nZVXCVOy41LjAyOAiHMcNgFIwUlJYw16/view]")
				os.system("tput setaf 5")
				print("\nCheck in VM : Devices > Optical Drives > rhel-8.0-x86_64-dvd.iso (should be tick).")
				print("\nThis yum Configuration will contain software which are present in RHEL8 iso image and epel-release-latest-8. ")
				os.system("tput setaf 11")
				input("\nPress Enter to continue.")
				#clear bug if not to continue then go to login l or r page.
				print("\n")
				os.system("tput setaf 120")
				os.system("cd /run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/")
				os.system("cp /root/autoyum_dvd12.repo    /etc/yum.repos.d/")
				os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
				os.system("yum repolist")
				os.system("tput setaf 12")
				print("\nyum Configuration Done!\n\n")
				input("\nPress Enter to proceed for full screen configuration.")
				os.system("tput setaf 120")
				os.system("yum install make perl -y")
				os.system("tput setaf 12")
				print("\nInstalled make perl.\n")
				os.system("tput setaf 120")
				os.system("yum install kernel-devel -y")
				os.system("tput setaf 12")
				print("\nInstalled make perl.\n")
				os.system("tput setaf 120")
				os.system("yum install elfutils-libelf-devel -y")
				os.system("tput setaf 12")
				print("\nInstalled make perl.\n")
				os.system("tput setaf 12")
				print("\nTo Do Manually:\n")
				os.system("tput setaf 14")
				print("\nIn VM: Devices > Optical Drives > rhel-8.0-x86_64-dvd.iso (untick)")
				print("\nAfter doing that : Devices > Inster Guest Additions CD image (click) ")
				print("\nIt will pop-up on os screen -->[run] (click)")
				os.system("tput setaf 9")
				print("\nNote: Wait till everything is done. Don't do any other task (can cause error). It may take some time. \n")
				os.system("tput setaf 14")
				print("\nAfter Message [Press Return to close this windows....] comes on screen reboot the os. In VM(login) : View > Full-screen Mode.")
				os.system("tput setaf 12")
				input("\nGood to go ;)")

				
			elif ch==0:
				os.system("tput setaf 7")
				os.system("clear")
				exit()
			else :
				os.system("tput setaf 9")
				print("Wrong input!")

			os.system("tput setaf 11")	
			input("\n\nPress Enter to continue....")

		elif login=="r":
			ip1=input("Enter IP : ")
			# bug: if ip is not in network and wrong ip.
			# Write code.
			#cleare drawback of typing password in each step.
			os.system(f"ssh-copy-id root@{ip1}")
			#ip=os.system(f"echo '{ip1}'")
			print('''
		press 1: To run date 
		press 2: To run cal 
		press 3: To Configure webserver
		press 4: To Create New User 
		press 5: To Configure yum in RHEL8 
		   [Note 5: will only work on -->rhel-8.0-x86_64-dvd.iso(iso file link provided while run.)]
		press 6: To Make Fullscreen RHEL8 in Oracle_Virtual_Box
		   [Note 6: yum will also be configured and it will only work on -->rhel-8.0-x86_64-dvd.iso(iso file link provided while run.)]
		press 7: To Open Hadoop menu.
		press 8: To Open AWS (Cloud Computing.)
		press 9: To Open Docker menu.
		press 0: To exit
			''')
			#press 3: To Configure webserver 
			print('')
			ch=int(input("Enter your choice: "))
			print("")

			os.system("tput setaf 120")
			if ch==1:
				#os.system(f"ssh {ip1} date") ------> can use only {ip1} also but better to specify user name 
				#Work : modify user name also 
				os.system(f"ssh root@{ip1} date")
			elif ch==2:
				os.system(f"ssh root@{ip1} cal")
			elif ch==3:
				# cleared : drawback of enter password in each step. 
				os.system(f"ssh root@{ip1} yum install httpd")
				os.system("tput setaf 12")
				print('\nInstallation Done.')

				
				#how to create and edit html file in remote login?
				os.system(f"tput setaf 120")
				print("\nType content of webpage (after Done Enter key-->[Right [Ctrl]+C]):")
				#ssh not working with cat to directly create autoweb.html file in user os
				#os.system(f"ssh {ip1} cat > /var/www/html/autoweb.html")
				#to copy autoweb.html file from this os to user os
				os.system("cat > /var/www/html/autoweb1.html")
				os.system(f"scp /var/www/html/autoweb1.html root@{ip1}:/var/www/html/")
				os.system("tput setaf 12")
				print('\nhtml page created and saved.')
				

				os.system(f" tput setaf 120")
				os.system(f"ssh root@{ip1} systemctl start httpd")
				os.system("tput setaf 12")
				print('\nhttpd server activated.')

				os.system(f" tput setaf 120")
				os.system(f"ssh root@{ip1} systemctl stop firewalld")
				os.system("tput setaf 12")
				print('\nfirewall off.')

				os.system(f"tput setaf 12")
				print('\nGot IP\n')
				
				os.system(f"tput setaf 120")
				print(f"Now open URL -->[http://{ip1}/autoweb1.html] in any web browser !")
				os.system("tput setaf 12")
				print('\nWebServer Configuration Done!')




			elif ch==4:

				os.system("tput setaf 120")
				user_name = input("\nEnter user name you wish to give : ")
				os.system(f"ssh root@{ip1} useradd {user_name}")

				os.system("tput setaf 120")
				user_password = input("\nEnter password: ")
				os.system(f"ssh root@{ip1} passwd {user_password}")

				os.system("tput setaf 11")
				print(f"\nNew user {user_name} is successfully Create ! ")

				#clear bug here !
				


			elif ch==5:
				#bug : only run if autoyum.repo file is present in current os.
				os.system("tput setaf 5")
				print("\nDrive link for RHEL8 iso file:")
				os.system("tput setaf 7")	
				print(f"\n-->[https://drive.google.com/file/d/1nZVXCVOy41LjAyOAiHMcNgFIwUlJYw16/view]")
				os.system("tput setaf 5")
				print("\nCheck in VM : Devices > Optical Drives > rhel-8.0-x86_64-dvd.iso (should be tick).")
				print("\nThis yum Configuration will contain software which are present in RHEL8 iso image, docker, and epel-release-latest-8. ")
				os.system("tput setaf 9")
				print("\nNote: Docker is from online repository. So, site might be low sometime. \n")
				os.system("tput setaf 11")
				input("Press Enter to continue.")
				print("\n")
				#clear bug if not to continue then go to login l or r page.
				os.system("tput setaf 120")
				os.system(f"ssh root@{ip1} cd /run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/")
				os.system(f"scp /root/autoyum.repo    root@{ip1}:/etc/yum.repos.d/")
				os.system(f"ssh root@{ip1} dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
				os.system(f"ssh root@{ip1} yum repolist")
				os.system("tput setaf 12")
				print("\nyum Configuration Done!")


			elif ch==6:
				#clear bug! : mount and unmount dvd of rhel8 and guest cd image and how to reboot os using cli.
				#bug : only run if autoyum.repo file is present in current os.
				os.system("tput setaf 5")
				print("First you have to set your video memory to 128 mb [settings > Display > video memory]")
				os.system("tput setaf 5")
				print("\nDrive link for RHEL8 iso file:")
				os.system("tput setaf 7")	
				print(f"\n-->[https://drive.google.com/file/d/1nZVXCVOy41LjAyOAiHMcNgFIwUlJYw16/view]")
				os.system("tput setaf 5")
				print("\nCheck in VM : Devices > Optical Drives > rhel-8.0-x86_64-dvd.iso (should be tick).")
				print("\nThis yum Configuration will contain software which are present in RHEL8 iso image and epel-release-latest-8. ")
				os.system("tput setaf 11")
				input("\nPress Enter to continue.")
				print("\n")
				#clear bug if not to continue then go to login l or r page.
				os.system("tput setaf 120")
				os.system(f"ssh root@{ip1} cd /run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/")
				os.system(f"scp /root/autoyum_dvd12.repo    root@{ip1}:/etc/yum.repos.d/")
				os.system(f"ssh root@{ip1} dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
				os.system(f"ssh root@{ip1} yum repolist")
				os.system("tput setaf 12")
				print("\nyum Configuration Done!\n\n")
				input("\nPress Enter to proceed for full screen configuration.")
				os.system("tput setaf 120")
				os.system(f"ssh root@{ip1} yum install make perl -y")
				os.system("tput setaf 12")
				print("\nInstalled make perl.\n")
				os.system("tput setaf 120")
				os.system(f"ssh root@{ip1} yum install kernel-devel -y")
				os.system("tput setaf 12")
				print("\nInstalled make perl.\n")
				os.system("tput setaf 120")
				os.system(f"ssh root@{ip1} yum install elfutils-libelf-devel -y")
				os.system("tput setaf 12")
				print("\nInstalled make perl.\n")
				os.system("tput setaf 12")
				print("\nTo Do Manually:\n")
				os.system("tput setaf 14")
				print("\nIn VM: Devices > Optical Drives > rhel-8.0-x86_64-dvd.iso (untick)")
				print("\nAfter doing that : Devices > Inster Guest Additions CD image (click) ")
				print("\nIt will pop-up on os screen -->[run] (click)")
				os.system("tput setaf 9")
				print("\nNote: Wait till everything is done. Don't do any other task (can cause error). It may take some time. \n")
				os.system("tput setaf 14")
				print("\nAfter Message [Press Return to close this windows....] comes on screen reboot the os. In VM(login) : View > Full-screen Mode.")
				os.system("tput setaf 12")
				input("\nGood to go ;)")

			#Hadoop	

			elif ch==7:

				print("Download ,install Setup hadoop and connect to Data,Name and Client nodes")
				ch = input("Whether Your namenode Is local(l) or Remote(r) (l/r): ")
				#Taking Namenode IP and port numbers
				#namenode Setup
				IP = input("Enter a Name Node IP ") or "192.168.43.89" 

				PORT = input("Enter a any port number ") or "9090"
				if ch in "r" or ch in "R":
					name_file = open('NameNode.py','w')
					name_data = """import subprocess
				print(subprocess.getoutput("mkdir /namenode"))
				print(subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"))
				print(subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm "))


				text_file = open('/etc/hadoop/core-site.txt','w')
				hdfs_file = open('/etc/hadoop/hdfs-site.txt','w')

				hdfs_site = '''<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

				<!-- Put site-specific property overrides in this file. -->

				<configuration>
				<property>
				<name>dfs.name.dir</name>
				<value>/namenode</value>
				</property>
				</configuration>'''

				core_site = '''<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

				<!-- Put site-specific property overrides in this file. -->

				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://{}:{}</value>
				</property>
				</configuration>'''
				text_file.writelines(core_site)
				hdfs_file.writelines(hdfs_site)
				hdfs_file.close()
				text_file.close()
				print(subprocess.getoutput("cp  /etc/hadoop/hdfs-site.txt /etc/hadoop/hdfs-site.xml"))
				print(subprocess.getoutput("cp /etc/hadoop/core-site.txt /etc/hadoop/core-site.xml"))
				print(subprocess.getoutput("hadoop namenode -format"))
				print(subprocess.getoutput("hadoop-daemon.sh start namenode"))
				print(subprocess.getoutput("jps"))
				print(subprocess.getoutput("hadoop dfsadmin -report | less"))""".format(IP,PORT)
					name_file.writelines(name_data)
					name_file.close()
					print(subprocess.getoutput("scp  `NameNode.py root@{}:/root/;hadoop-1.2.1-1.x86_64.rpm root@{}:/root/ ; jdk-8u171-linux-x64.rpm root@{}:/root/;`;ssh root@{} python3 NameNode.py".format(IP,IP)))
				else:
					print(subprocess.getoutput("mkdir /namenode"))
					print(subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"))
					print(subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm "))


					text_file = open('/etc/hadoop/core-site.txt','w')
					hdfs_file = open('/etc/hadoop/hdfs-site.txt','w')

					hdfs_site = '''<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

					<!-- Put site-specific property overrides in this file. -->

					<configuration>
					<property>
					<name>dfs.name.dir</name>
					<value>/namenode</value>
					</property>
					</configuration>'''

					core_site = '''<?xml version="1.0"?>
					<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

					<!-- Put site-specific property overrides in this file. -->

					<configuration>
					<property>
					<name>fs.default.name</name>
					<value>hdfs://{}:{}</value>
					</property>
					</configuration>'''.format(IP,PORT)
					text_file.writelines(core_site)
					hdfs_file.writelines(hdfs_site)
					hdfs_file.close()
					text_file.close()
					print(subprocess.getoutput("cp  /etc/hadoop/hdfs-site.txt /etc/hadoop/hdfs-site.xml"))
					print(subprocess.getoutput("cp /etc/hadoop/core-site.txt /etc/hadoop/core-site.xml"))
					print(subprocess.getoutput("hadoop namenode -format"))
					print(subprocess.getoutput("hadoop-daemon.sh start namenode"))
					print(subprocess.getoutput("jps"))
					print(subprocess.getoutput("hadoop dfsadmin -report | less"))


				while True:
					choice = input("Do you wants to Create DataNode(d) or ClientNode(c) or exit(e) (d/c/e) : ") or "e"

					#Datanode Setup
					if choice == "D" or choice == "d":
						data_file = open('DataNode.py','w')
						data_data = """import subprocess
				print(subprocess.getoutput('mkdir /datanode'))
				print(subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"))
				print(subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm "))
				print(subprocess.getoutput("systemctl stop firewalld"))
				print(subprocess.getoutput("setenforce 0"))
				text_file = open('/etc/hadoop/core-site.txt','w')
				hdfs_file = open('/etc/hadoop/hdfs-site.txt','w')

				hdfs_site = '''<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

				<!-- Put site-specific property overrides in this file. -->

				<configuration>
				<property>
				<name>dfs.data.dir</name>
				<value>/datanode</value>
				</property>
				</configuration>'''

				core_site = '''<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

				<!-- Put site-specific property overrides in this file. -->

				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://{}:{}</value>
				</property>
				</configuration>'''
				text_file.writelines(core_site)
				hdfs_file.writelines(hdfs_site)
				hdfs_file.close()
				text_file.close()
				print(subprocess.getoutput("cp  /etc/hadoop/hdfs-site.txt /etc/hadoop/hdfs-site.xml"))
				print(subprocess.getoutput("cp /etc/hadoop/core-site.txt /etc/hadoop/core-site.xml"))
				print(subprocess.getoutput("hadoop-daemon.sh start datanode"))
				print(subprocess.getoutput("jps"))
				print(subprocess.getoutput("hadoop dfsadmin -report | less"))""".format(IP,PORT)
						data_file.writelines(data_data)
						data_file.close()
						dataIP = input("Enter a Data Node IP ")
						print(subprocess.getoutput("scp DataNode.py,hadoop-1.2.1-1.x86_64.rpm,jdk-8u171-linux-x64.rpm root@{}:/root/;ssh root@{} python3 DataNode.py".format(dataIP,dataIP)))

					#Client Node Setup
					if choice == "C" or choice == "c":
						client_file = open('ClientNode.py','w')
						client_data = """import subprocess
				print(subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"))
				print(subprocess.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm "))
				print(subprocess.getoutput("systemctl stop firewalld"))
				print(subprocess.getoutput("setenforce 0"))
				text_file = open('/etc/hadoop/core-site.txt','w')
				hdfs_file = open('/etc/hadoop/hdfs-site.txt','w')

				hdfs_site = '''<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

				<!-- Put site-specific property overrides in this file. -->

				<configuration>
				<property>
				<name></name>
				<value></value>
				</property>
				</configuration>'''

					core_site = '''<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

				<!-- Put site-specific property overrides in this file. -->

				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://{}:{}</value>
				</property>
				</configuration>'''
				text_file.writelines(core_site)
				hdfs_file.writelines(hdfs_site)
				hdfs_file.close()
				text_file.close()
				print(subprocess.getoutput("cp  /etc/hadoop/hdfs-site.txt /etc/hadoop/hdfs-site.xml"))
				print(subprocess.getoutput("cp /etc/hadoop/core-site.txt /etc/hadoop/core-site.xml"))
				print(subprocess.getoutput("hadoop-daemon.sh start datanode"))
				print(subprocess.getoutput("jps"))
				print(subprocess.getoutput("hadoop dfsadmin -report | less"))""".format(IP,PORT)
						client_file.writelines(client_data)
						client_file.close()
						clientIP = input("Enter a CLient Node IP ")
						print(subprocess.getoutput("scp  `ClientNode.py root@{}:/root/;hadoop-1.2.1-1.x86_64.rpm root@{}:/root/ ; jdk-8u171-linux-x64.rpm root@{}:/root/;`;ssh root@{} python3 ClientNode.py".format(clientIP,clientIP)))

					if choice == "E" or choice == "e":
						exit()

			#clear bugs in Hadoop , aws , docker.

			#aws.
			elif ch==8:

			i=0
			# Initialize the converter 
			converter = txt.init() 
			# Sets speed percent 
			# Can be more than 100 
			converter.setProperty('rate', 150) 
			# Set volume 0-1 
			converter.setProperty('volume', 1) 
			#To Change a Voice
			voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

			# Use female voice 
			converter.setProperty('voice', voice_id) 

			converter.say("Hey,,, Vinod, How can i help you")
			converter.runAndWait()

			r = sr.Recognizer()
			def speak():
			    with sr.Microphone() as source:
			            converter.say("start saying...")
			            converter.runAndWait()
			            audio = r.listen(source)
			            converter.say("Got it please wait....")
			            converter.runAndWait()
			    return audio

			def performTask(audio):
			    def aws(cmd):
			        # 1) Create new key pair 
			        if("create" in cmd or "launch" in cmd) and ("key" in cmd or "keypad" in cmd ):
			            converter.say("Enter Key pair name")
			            converter.runAndWait()
			            key = input("Key Name : ")
			            subprocess.getoutput("aws ec2 create-key-pair --key-name {}".format(key))
			            converter.say("Key pair {} Successfully created.".format(key))
			            converter.runAndWait()
			        # 2) Create new Security group
			        elif("create" in cmd or "launch" in cmd) and ("security" in cmd or "security-group" in cmd ):
			            converter.say("Enter group name and description")
			            converter.runAndWait()
			            grp = input("Group Name : ")
			            des = input("Description : ")
			            subprocess.getoutput("aws ec2 create-security-group --group-name {} --description {}".format(grp,des))
			            converter.say("Security Group with name {} iS successfully created".format(grp))
			            converter.runAndWait()
			        # 3) Create new instance
			        elif ("create" in cmd or "launch" in cmd) and ("instance" in cmd or "laptop" in cmd or "ins" in cmd):
			            converter.say("Enter image ID")
			            converter.runAndWait()
			            img = input("Image ID : ")
			            converter.say("Enter instance type")
			            converter.runAndWait()
			            typ = input("Instance Type:")
			            converter.say("Enter subnet ID")
			            converter.runAndWait()
			            subnet = input("Subnet ID : ")
			            converter.say("Enter Security group ID")
			            converter.runAndWait()
			            grp = input("Security group ID :")
			            converter.say("Enter key name ")
			            converter.runAndWait()
			            keyname = input("Key Name : ")
			            subprocess.getoutput("aws ec2 run-instances --image-id {} --instance-type {} --subnet-id {} --count 1 --security-group-ids {} --key-name {}".format(img,typ,subnet,grp,keyname))
			            converter.say("Instance successfully created.")
			            converter.runAndWait()
			        # 4) Termination of instance 
			        elif ("terminate" in cmd or "delete" in cmd or "destroy" in cmd) and ("instance" in cmd or "laptop" in cmd or "ins" in cmd):
			            converter.say("Enter Instance ID")
			            converter.runAndWait()
			            ids = input("Instance ID : ")
			            subprocess.getoutput("aws ec2 terminate-instances --instance-ids {}".format(ids))
			            converter.say("Instance successfully Terminated.")
			            print("Instance ID {} successfully Terminated.".format(ids))
			            converter.runAndWait()
			        # 5) Display list of instances
			        elif ("show" in cmd or "display" in cmd or "view" in cmd or "list" in cmd) and ("instance" in cmd or "laptop" in cmd or "ins" in cmd):
			            converter.say("Please, wait Displaying list")
			            converter.runAndWait()
			            print(subprocess.getoutput("aws ec2 describe-instances"))
			            converter.say("The following are the instances.")
			            converter.runAndWait()
			            time.sleep(4)
			        # 6) Creation a volume
			        elif ("create" in cmd or "launch" in cmd) and ("volume" in cmd or "EBS voluem" in cmd):
			            converter.say("Enter Size of EBS volume")
			            converter.runAndWait()
			            size = input("EBS size : ")
			            subprocess.getoutput("aws ec2 create-volume --volume-type gp2 --size  {} --availability-zone ap-south-1a".format(size))
			            converter.say("Volume Is created size of {}".format(size))
			            print("Volume Is created size of "+size)
			            converter.runAndWait()
			        # 7) Attach Volume to a instance
			        elif ("attach" in cmd or "join" in cmd) and ("volume" in cmd or "EBS voluem" in cmd or "backet" in cmd):
			            converter.say("Enter Volum id")
			            converter.runAndWait()
			            volId = input("Enter volum id : ")
			            converter.say("Enter Instance id")
			            converter.runAndWait()
			            insId = input("Enter Instance Id : ")
			            subprocess.getoutput("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volId,insId)) 
			            converter.say("Volume attached to a instance.")
			            print("Volume attached to a instance. \nInstance ID "+insId+"\n Volume ID "+volId)
			            converter.runAndWait()
			        # 8) Run/start instance
			        elif ("start" in cmd or "run" in cmd) and ("instance" in cmd or "laptop" in cmd or "ec2" in cmd or "ins" in cmd):
			            converter.say("Please enter instance id. ")
			            converter.runAndWait()
			            data = input("EC2 ID:")
			            subprocess.getoutput("aws ec2 start-instances --instance-ids "+data)
			            converter.say("Instance Started.")
			            print("Instance Started.\nInstance ID : "+data)
			            converter.runAndWait()
			        # 9) Stop instance
			        elif ("stop" in cmd or "exit" in cmd) and ("instance" in cmd or "laptop" in cmd or "ec2" in cmd or "ins" in cmd):
			            converter.say("Please enter instance id. ")
			            converter.runAndWait()
			            data = input("EC2 ID:")
			            subprocess.getoutput("aws ec2 stop-instances --instance-ids {}".format(data))
			            converter.say("Intance Stopped.")
			            print("Intance Stopped. \nInstance ID {}".format(data))
			            converter.runAndWait()
			        # 10) Create Cloud Front Distribution
			        elif ("create" in cmd or "launch" in cmd) and ("cloud front" in cmd or "cloudfront" in cmd):
			            converter.say("Please enter Origilnal domain name. ")
			            converter.runAndWait()
			            domainName = input("Enter Domain Name : ")
			            subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}".format(domainName))
			            print("New CloudFront distribution is created")
			            converter.say("New CloudFront distribution is created")
			            converter.runAndWait()
			            
			        # 11) Create New S3 Buckets
			        elif ("create" in cmd or "launch" in cmd) and ("S3 bucket" in cmd or "bucket" in cmd):
			            prt = ""
			            while(True):
			                # If Error occured goes to Except part
			                try:
			                    BucketName = input("Enter Bucket Name : ")
			                    converter.say("Please enter {} Bucket name. ".format(prt))
			                    converter.runAndWait()
			                    subprocess.getoutput("AWS s3api create-bucket --bucket {} --regoin ap-south-1".format(Bucketname))
			                    prt = "New Bucket is created"
			                    print(prt)
			                    converter.say(prt)
			                    converter.runAndWait()
			                    break;
			                # Display message if Exception Occured
			                except Exception as e:
			                    print("Oops!", e.__class__, "occurred.")
			                    prt = "Oops! Name Already exists!"
			                    print(prt)
			                    converter.say(prt)
			                    converter.runAndWait()
			                    prt = "Unique"
			        # 12) Uploading a file or folder to Bucket
			        elif ("upload" in cmd or "add" in cmd) and ("file" in cmd or "folder" in cmd or "image" in cmd or "picture" in cmd or "document" in cmd) and ("bucket" in cmd or "s3 bucket" in cmd):
			            prt = ""
			            while(True):
			                # If Error occured goes to Except part
			                try:
			                    print(subprocess.getoutput("DIR /W"))
			                    converter.say("Please enter {} Location,  orelse select File or folder name, from above list. ".format(prt) )
			                    converter.runAndWait()
			                    fileLoc = input("Enter {} Location orelse select  File or folder name from above list : ".format(prt))
			                    print(subprocess.getoutput("aws s3 ls"))
			                    converter.say("Please enter {} Bucket name, from above list. ".format(prt))
			                    converter.runAndWait()
			                    bucketName = input("Type Bucket name from above list : ")
			                    converter.say("Do you wants to allow public access, then type yes, orelse no")
			                    converter.runAndWait()
			                    publicAcess = input("Do you want to allow public acess (y,n) : ")
			                    desicion = "--acl public-read-write" if "y" in publicAcess else ""
			                    res = subprocess.getoutput("AWS s3 cp {} s3://{} {}".format(fileLoc,bucketName,desicion))
			                    if "Completed" in res or "complete" in res or "completed" in res or "Complete" in res: 
			                        prt = "Success!!, File, or folder uploaded to a bucket name {}".format(bucketName)
			                        print(prt)
			                        converter.say(prt)
			                        converter.runAndWait()
			                        break;
			                    else:
			                        prt = "Oops!, Something gone wrong!"
			                        print(prt)
			                        converter.say(prt)
			                        converter.runAndWait()
			                        print("===================================================")
			                        prt = "Valid"
			                # Display message if Exception Occured
			                except Exception as e:
			                    print("Oops!", e.__class__, "occurred.")
			                    prt = "Oops! Something gone wrong!"
			                    print(prt)
			                    converter.say(prt)
			                    converter.runAndWait()
			                    prt = "Valid"
			        # 13) Delete/Remove Cloud front Distribution
			        elif ("delete" in cmd or "remove" in cmd) and ("cloud front" in cmd or "cloudfront" in cmd):
			            prt = ""
			            while(True):
			                # If Error occured goes to Except part

			                converter.say("Please enter {} Cloudfront distribution id. ".format(prt))
			                converter.runAndWait()

			                cloudFrontID = input("Enter {} Cloudfront distribution id : ".format(prt))

			                # Taking complete JSON to find if-match ID
			                try:
			                    if_match_ID = json.loads(subprocess.getoutput("aws cloudfront get-distribution --id {}".format(cloudFrontID)))
			                    delRes = subprocess.getoutput("aws cloudfront delete-distribution --id {} --if-match {}".format(cloudFrontID,if_match_ID["ETag"]))
			                    if "DistributionNotDisabled" in delRes:
			                        converter.say("Sorry,  your Cloudfront is not disable,  Please go to AWS account,, and Disable Your Cloud front Distribution. ")
			                        converter.runAndWait()
			                        converter.say(",,I will be waiting for you.")
			                        converter.runAndWait()
			                        print("Your Coudfront id {} is not disabled,  Please go to AWS account and Disable Your Cloud front Distribution.\n".format(cloudFrontID))
			                        input("Press enter key to move further..")
			                    else:
			                        prt = "Success!!, Cloud Front ID {} is deleted".format(cloudFrontID)
			                        print(prt)
			                        converter.say(prt)
			                        converter.runAndWait()
			                        exit()
			                        print(if_match_ID["ETag"])
			                # Display message if Exception Occured
			                except Exception as e:
			                    print("Oops! ",e," occurred.")
			                    prt = "Oops! Something gone wrong!"
			                    print(prt)
			                    converter.say(prt,". Check Cloud front ID.")
			                    converter.runAndWait()
			                    if "e" in input("Press \"e\" to move orelse press any key to try once again."):
			                        converter.say("Hey!, Vinu!")
			                        break;
			                    print("=========================================")
			                    prt = "Valid"
			                    continue

			        # 14) Show a list of CloudFront Distribution
			        elif ("show" in cmd or "display" in cmd or "view" in cmd or "list" in cmd) and ("cloud front" in cmd or "cloudfront" in cmd):
			            ptr = "The following are list of CloudFront"
			            converter.say("Please, wait Displaying list")
			            converter.runAndWait()
			            print(ptr)
			            converter.say(ptr)
			            converter.runAndWait()
			            if_match = json.loads(subprocess.getoutput("aws cloudfront list-distributions"))
			            for i in range(len(if_match["DistributionList"]["Items"])):
			                print(str(i+1)+") Cloudfront Distribution ID : ",if_match["DistributionList"]["Items"][i]["Id"],"\n") 
			                print("  => Status : ",if_match["DistributionList"]["Items"][i]["Status"])
			                print("  => CloudFront Domain Name : ",if_match["DistributionList"]["Items"][i]["DomainName"])
			                print("  => CloudFront Origin Domain Name : ",if_match["DistributionList"]["Items"][i]["Origins"]["Items"][0]["DomainName"])
			                print("  => CloudFront is Enable : ",if_match["DistributionList"]["Items"][i]["Enabled"],"\n")
			            time.sleep(3)
			            
			            # a = [if_match_ID["DistributionList"]["Items"][i]["Id"] for i in range(len(if_match_ID["DistributionList"]["Items"]))] #Single line For loop
			            # print("\n".join(str(a).strip("[]").split(",")).replace("\'","").replace(" ",""))  # helps to remove all extras
			        
			        
			        # 15) Show list of Files/folder in a backet
			        elif ("show" in cmd or "display" in cmd or "view" in cmd or "list" in cmd) and ("file" in cmd or "folder" in cmd or "image" in cmd or "picture" in cmd or "document" in cmd) and ("bucket" in cmd or "s3 bucket" in cmd):
			            converter.say("Please, wait Displaying list")
			            converter.runAndWait()
			            print("\n\t\t\t--- Buckets ---\n")
			            if_match = json.loads(subprocess.getoutput("aws s3api list-buckets"))
			            for i in range(len(if_match["Buckets"])):
			                print("\t\t",i+1,") ",if_match["Buckets"][i]["Name"])
			            ptr = "Enter the Bucket Name from above list "
			            converter.say(ptr)
			            converter.runAndWait()
			            bucketName = input("\n\t\t{} : ".format(ptr))
			            ptr = "The following are list of files or folders available in "+bucketName+" bucket."
			            print("\n\t",ptr,"\n")
			            converter.say(ptr)
			            converter.runAndWait()
			            print("\t\t\t--- ",bucketName," ---\n")
			            print(subprocess.getoutput("aws s3 ls {}".format(bucketName)),"\n")
			        # 16) Show a list of S3 buckets
			        elif ("file" not in cmd or "folder" not in cmd or "image" not in cmd or "picture" not in cmd or "document" not in cmd) and("show" in cmd or "display" in cmd or "view" in cmd or "list" in cmd) and ("S3 bucket" in cmd or "bucket" in cmd):
			            ptr = "The following are list of Buckets available."
			            converter.say("Please, wait Displaying list")
			            converter.runAndWait()
			            print("\n\t",ptr,"\n")
			            converter.say(ptr)
			            converter.runAndWait()
			            print("\t\t\t--- Buckets ---\n")
			            if_match = json.loads(subprocess.getoutput("aws s3api list-buckets"))
			            for i in range(len(if_match["Buckets"])):
			                print("\t\t",i+1,") ",if_match["Buckets"][i]["Name"])

			        # 17) Remove files/folders from Buckets 
			        elif ("delete" in cmd or "remove" in cmd) and ("file" in cmd or "folder" in cmd or "image" in cmd or "picture" in cmd or "document" in cmd) and ("bucket" in cmd or "s3 bucket" in cmd):
			            while True:
			                try:
			                    ptr = "The following are list of Buckets available."
			                    converter.say(", Displaying a list.")
			                    converter.runAndWait()
			                    print("\n\t\t\t--- Buckets ---\n")
			                    if_match = json.loads(subprocess.getoutput("aws s3api list-buckets"))
			                    for i in range(len(if_match["Buckets"])):
			                        print("\t\t",str(i+1)+")",if_match["Buckets"][i]["Name"])
			                    ptr = "Please enter bucket name from above list"
			                    converter.say(ptr)
			                    converter.runAndWait()
			                    bucketName = input("\n{} : ".format(ptr))
			                    check = subprocess.getoutput("aws s3 ls {}".format(bucketName))
			                    if "error" in check:
			                        print(check)
			                        converter.say("Sorry Dear, Bucket Name is not exists.")
			                        convreter.say("Please Enter Valid")
			                        converter.runAndWait()
			                        continue
			                    print(check)
			                    print("\t\t\t--- ",bucketName," ---")
			                    ptr = "Type File Name to remove"
			                    converter.say(ptr)
			                    converter.runAndWait()
			                    fileName = input("\n{} : ".format(ptr))
			                    delFile = subprocess.getoutput("aws s3 rm s3://{}/{}".format(bucketName,fileName))
			                    if "del" in delFile:
			                        prt = "Success!!, File is removed."
			                        print(prt)
			                        converter.say(prt)
			                        converter.runAndWait()
			                    break
			                except Exception as e:
			                    print("Oops! ",e," occurred.")
			                    prt = "Oops! Something gone wrong!"
			                    print(prt)
			                    converter.say(prt,". Check Bucket or file name.")
			                    converter.runAndWait()
			        # Delete or Remove Buckets
			        if ("delete" in cmd or "remove" in cmd) and ("bucket" in cmd or "s3 bucket" in cmd):
			            while True:
			                try:
			                    ptr = "The following are list of Buckets available."
			                    converter.say(", Displaying a list.")
			                    converter.runAndWait()
			                    print("\n\t\t\t--- Buckets ---\n")
			                    if_match = json.loads(subprocess.getoutput("aws s3api list-buckets"))
			                    for i in range(len(if_match["Buckets"])):
			                        print("\t\t",str(i+1)+")",if_match["Buckets"][i]["Name"])
			                    ptr = "Please enter bucket name from above list, to remove a bucket"
			                    converter.say(ptr)
			                    converter.runAndWait()
			                    bucketName = input("\n{} : ".format(ptr)) or "."
			                    check = subprocess.getoutput("aws s3api delete-bucket --bucket {}".format(bucketName))
			                    if "BucketNotEmpty" in check:
			                        print("Sorry Dear, Bucket is not empty first empty Files.")
			                        converter.say("Sorry Dear, Bucket is not empty first empty Files.")
			                        converter.runAndWait()
			                        continue
			                    elif "Error" in check or "error" in check:
			                        print("Please enter Valid.")
			                        converter.say("Sorry Dear, Bucket Name is not exists.")
			                        converter.say("Please enter Valid.")
			                        converter.runAndWait()
			                        continue
			                    if "del" in check or "Del" in check:
			                        prt = "Success!!, Bucket is removed."
			                        print(prt)
			                        converter.say(prt)
			                        converter.runAndWait()
			                    break
			                except Exception as e:
			                    print("Oops! ",e," occurred.")
			                    prt = "Oops! Something gone wrong!"
			                    print(prt)
			                    converter.say(prt)
			                    converter.runAndWait()
			            # Task is not available
			            else:
			                converter.say("sorry, There is no such task..")
			                print("sorry, There is no such task..")
			                converter.runAndWait()
			            
			    if "how are you" in audio:
			        converter.say("I am doing great....")
			    elif "tell me about" in audio:
			        converter.say("I am Your voice assistant, very intelligent. I can control AWS public cloud for you.")
			    elif "help" in audio:
			        converter.say("I can help you from the following list.")
			        print("I can help you from the following list.")
			        print("1. List of ec2 instance")
			        print("2. Start a instance")
			        print("3. Launch a instance")        
			        print("4. Creating a key pair")
			        print("5. Creating a Security group")
			        print("6. Create an EBS volume  of 1GB")
			        print("7. Attach EBS to the instances.")
			        converter.say("Launchs a instance")
			        converter.say("Creating a key pair and Security group")
			        converter.say("Creating a EBS volume")
			        converter.say("Attach EBS to the instances.")
			    elif "hello" in audio or "hey" in audio or "hi" in audio:
			        converter.say("Hi dear, How can i help you..")
			    else:
			        aws(audio)
			    converter.runAndWait()

			        
			while 1:
			    spk = speak()
			    aud =  r.recognize_google(spk)
			    if "exit" in aud:
			        converter.say("AWS Account Logging out.")
			        print("AWS account is logged out.")
			        converter.runAndWait()
			        exit()
			    else:
			        print(aud)
			        performTask(aud)


			#docker.
			elif ch==9:

				# DOCKER
				# Docker Configure in yum
				print(subprocess.getoutput("touch yum.repo"))
				docker_repo = open('/etc/yum.repos.d/yum.repo','w')
				docker_conf = """[Docker]
				name=Yum form Docker
				baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
				gpgcheck=0"""

				docker_repo.writelines(docker_conf)
				docker_repo.close()
				# Installing Docker
				subprocess.getoutput("yum install docker-ce --nobest -y")
				# Docker Menu
				print("Welcome To a Docker Menu")
				print("Docker Successfully Configured and Installed...")
				while True:
					print("1. Start Docker")
					print("2. Stop Docker")
					print("3. Status of Docker")
					print("4. Remove Docker from this System")
					print("5. Exit")
					# Select Option
					choice = input("Enter your option (1/2/3/4/5) : ") or "5"
						
					print()
					# Start Docker 
					if choice in "1":
						print("Docker Started..")
						while True:
							# Menu Docker tasts
							print(subprocess.getoutput("systemctl start docker"))
							print("Docker Menu")
							print("1. Pull new Images.")
							print("2. Display all Images.")
							print("3. Launch New Container.")
							print("4. Display List of Containers")
							print("5. Start Container")
							print("6. Stop Container")
							print("7. Remove Image")
							print("8. Remove Container")
							print("9. Display Running Instances")
							print("10. Remove All Container")
							print("11. Exit")
							dchoice = input("Enter your choice : ")

							# 1) Pull New Images from docker hub
							if dchoice in "1":
								imageName = input("Enter Image Name : ") or "centos"
								imageV = ":"+input("Enter Version orelse takes default latest version : ") or ""
								print(subprocess.getoutput("docker pull {}{}".format(imageName,imageV)))

							# 2) Show  Images
							if dchoice in "2":
								print(subprocess.getoutput("docker images"))

							# 3) Launch new Container
							if dchoice in "3":
								try:
									ImageName = input("Enter Image Name orelse takes default takes centOS: ") or "centos"
									ConName = input("Enter Container Name(optional) : ") or ""
									print(subprocess.getoutput("docker run -it {} {} echo Success Container Started ".format(ConName,ImageName)))
									print("Container Launched...")

								except Exception as a:
									print("Error: "+e+" occured!")
							# 4) Display list of Containers
							if dchoice in "4":
								print(subprocess.getoutput("docker ps -a "))

							# 5) Start Container
							if dchoice in "5":
								try:
									print(subprocess.getoutput("firewall-cmd --zone=public --add-masquerade --permanent"))
									print(subprocess.getoutput("firewall-cmd --zone=public --add-port=80/tcp"))
									print(subprocess.getoutput("firewall-cmd --zone=public --add-port=443/tcp"))
									print(subprocess.getoutput("firewall-cmd --reload"))
									print(subprocess.getoutput("systemctl restart docker"))
									print(subprocess.getoutput("docker ps -a "))
									ConName = input("Enter Container Name or ID from above list : " ) or ""
									print(subprocess.getoutput("docker start {} ".format(ConName)))
									print(subprocess.getoutput("docker exec {} date".format(ConName)))
									print("Container Menu.")
									print("1. Install httpd")
									print("2. Start httpd ")
									print("3. Install python")
									print("4. Create Html file ")
									print("5. Exit from container ")
									ch = input("Enter your option (1/2/3/4/5) : ")
									if ch in "1":
										print(subprocess.getoutput("docker exec {} yum install httpd -y".format(ConName)))
									if ch in "2":
										print(subprocess.getoutput("docker exec {} /usr/sbin/httpd".format(ConName)))
									if ch in "3":
										print(subprocess.getoutput("docker exec {} yum install python3 -y".format(ConName)))
									if ch in "4":
										print(subprocess.getoutput("docker exec {} touch hello.html".format(ConName)))
										
									if ch in "5":
										break;
								except Exception as e:
									print("Error: "+e+" occured!")

							# 6) Stop Contaner
							if dchoice in "6":
								print(subprocess.getoutput("docker ps"))
								ConName = input("Enter Container Name or ID to stop from above list : " ) or ""
								print(subprocess.getoutput("docker stop {}".format(ConName)))

							# 7) Remove Image
							if dchoice in "7":
								print(subprocess.getoutput("docker images"))
								ImageName = input("Enter Image Name to remove : ") or ""
								print(subprocess.getoutput("docker rmi {} -f".format(ImageName)))

							# 8) Remove Container
							if dchoice in "8":
								print(subprocess.getoutput("docker ps -a "))
								ConName = input("Enter Container Name or ID from above list : " ) or ""
								print(subprocess.getoutput("docker rm {} -f".format(ConName)))

							# 9) Display all Running Instances
							if dchoice in "9":
								print(subprocess.getoutput("docker ps"))

							# 10) Remove All Containers
							if dchoice in "10":
								print(subprocess.getoutput("docker ps -a "))
								rm = input("Are you sure wants to remove all CONTAINERS (y/n) : ") or "n"
								if rm in "y":
									print(subprocess.getoutput("docker container rm  -f `docker container ls -a -q`"))
							if dchoice in "11":
								break
					if choice in "2":
						print("Docker is stopping...")
						print(subprocess.getoutput("systemctl stop docker"))
						print()
					if choice in "3":
						print(subprocess.getoutput("systemctl status docker"))
						print()
					if choice in "4":
						rm = input("Are you sure wants to remove Docker (y/n) : ") or "n"
						if rm in "y":
							print(subprocess.getoutput("yum remove docker-ce"))
							print("Docker removed from your system")
					if choice in "5":
						print("You choose 5 to quite")
						print("Exiting from menu..Thank you have nice day..")
						exit()


			elif ch==0:
				os.system("tput setaf 7")
				os.system("clear")
				exit()
			else :
				os.system("tput setaf 9")
				print("Wrong input!")

			os.system("tput setaf 11")
			input("\nPress Enter to continue....")	

		elif login=='q':
			os.system("tput setaf 7")
			os.system("clear")
			exit()

		else :
			os.system("tput setaf 9")
			print("\t\tNot Supported ! ")
			os.system("tput setaf 10")
			print("\n\t\tPlease Enter 'l' for local login or 'r' for remote login ")
			input("\t\tPress Enter to continue....")



	elif password!="menu":
		os.system("tput setaf 9")
		print("\n\t\tIncorrect password !")
		os.system("tput setaf 10")
		print("\t\tPress Enter to continue....")
		input("\t\t")
		os.system("tput setaf 120")
		os.system("clear")
		password = gp.getpass("\n\n\t\tEnter Password (q to quit): ")
		
		if password=='q':
			os.system("tput setaf 7")
			os.system("clear")
			exit()
