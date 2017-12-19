import urllib.request
def crawl():
    for i in range(1,10):#10 is just for exemple chose the number you want
        
        urllib.request.urlretrieve("https://www.example.com/fileNumber"+str(i)+".mp3", "filename"+str(i)+".mp3") #you can paste an url and chose the number of files to download 
        
        #for exemple if you want to download 10 files , first file url is https://www.example.com/file1 then you just copy this url into the code and type 10 in the loop
        
        print(i)

crawl()
