from ftplib import FTP

# We need to first connect to a server
host = "127.0.0.1"
user = "admin"
password = "password"
path = './storage'


with FTP(host) as ftp:
    ftp.login(user, password)
    print(ftp.getwelcome())

    # We can now list the contents of the server
    ftp.dir()

    option = input("ENTER AN OPTION:\n[1] Upload\n[2] Download\n[3] Exit\n")

    # Create match statements
    if option == "1":                                       # Upload
        with open("upload.txt", "rb") as f:
            ftp.storbinary("STOR upload.txt", f, 1024)
            print("Upload Successful")
    elif option == "2":                                     # Download
        with open("download.txt", "wb") as f:
            ftp.retrbinary("RETR download.txt", f.write, 1024)
            print("Download Successful")
    else:
        print("Exiting...")
        ftp.quit()
