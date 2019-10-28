import pysftp

myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished ... "

    # Define the file that you want to upload from your local directorty
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL2.txt"
    localFilePath = './TUTORIAL2.txt'

    # Define the remote path where the file will be uploaded
    remoteFilePath = '/var/integraweb-db-backups/TUTORIAL2.txt'

    sftp.put(localFilePath, remoteFilePath)
 
# connection closed automatically at the end of the with-block
