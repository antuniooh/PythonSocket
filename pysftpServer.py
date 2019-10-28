import pysftp

myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print ("Connection succesfully stablished ... ")

    # Define the file that you want to download from the remote directory
    remoteFilePath = ('./TUTORIAL.txt')

    # Define the local path where the file will be saved
    # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
    localFilePath = ('./TUTORIAL.txt')

    sftp.get(remoteFilePath, localFilePath)
 
# connection closed automatically at the end of the with-block
