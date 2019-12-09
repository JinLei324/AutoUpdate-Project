import requests
import io
import os
from zipfile import ZipFile,ZipInfo
import requests	 
from clint.textui import progress
import shutil
def main():
    #url = input("zip url: ") 
    url = 'http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf'
    
    #zipfilename = url.split('/')[-1]
    zipfilename = "1.zip"    
    #print(zipfilename)   

    #you can set workdirectory 
    currentDirectory = input("Input the Replace Directory Path(Nothing Input is CurrentDirectory):")
    
    
    

    if(currentDirectory==''):
        currentDirectory = os.getcwd()    

    '''
    for file in os.listdir(currentDirectory): 
        print(file)
        file_path = os.path.join(currentDirectory, file)
        if os.path.isfile(file_path):
            if(file=='update.py'):
                pass
            else:
                os.remove(file_path)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
    
    
    r = requests.get(url, stream=True)	 
    
    with open(zipfilename, "wb") as updatefile:	 
        total_length = int(r.headers.get('content-length'))		
        for ch in progress.bar(r.iter_content(chunk_size = 1024),expected_size=(total_length/1024) + 1,label="Downloading Zip Data: ",):
            if ch:						
                updatefile.write(ch)
                updatefile.flush()
    
    '''
    with ZipFile(zipfilename) as myzip:        
        for fileInfo in progress.bar(myzip.infolist(), expected_size=len(myzip.infolist()) + 1,label="Updating Zip Data: ",):
           
            filename = fileInfo.filename
            

            filenames=filename.split("/")
            currentFileName = currentDirectory
            for i in range(1,len(filenames)):
                currentFileName = currentFileName+"/"+filenames[i]
            #print(currentFileName)
            
            
            if(fileInfo.is_dir()==False):    #targetfilename=currentDirectory+"/"+filename
                if(os.path.exists(currentFileName)):                
                    if(os.path.isfile(currentFileName)):
                        os.remove(currentFileName)   
           
            
                with myzip.open(filename) as myfile:
                    #print(myfile)
                    try:
                        with open(currentFileName,"xb") as writefile:
                            #print(string(myfile.read())
                            newFileByteArray = bytearray(myfile.read())
                            writefile.write(newFileByteArray)
                            #writefile.write(myfile.read().decode('ascii'))
                    except:
                        pass
            else:
                if(os.path.exists(currentFileName)==False):
                    os.makedirs(currentFileName)    
    
    os.remove("./"+zipfilename)               
               
            
    
        


if __name__ == "__main__":
    main()
