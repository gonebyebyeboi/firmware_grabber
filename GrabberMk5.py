#Importing the libraries needed
import os
import pandas as pd
from bs4 import BeautifulSoup as bs



#Now getting into some global variables
masterFilepaths = []

# Common Firmware Image Extensions for the parser to look for
extension = [".bin", ".zip",  ".hex", ".rar", ".udp", ".update", ".rom", ".iso", ".elf", ".dfu", ".bin_extract", ".tar.gz", ".sys", ".exe", ".dav"]
#This is the path that stays the same for the index.html file
###You will need to modify bp for the parser to work!!!###

bp= "Insert File Path Here"

#this will contain all the file paths that align with the predefined path name
#Some scans will deviate from this path, but I will come up with a way to get those as well.

# three types in "other" scans
# Note that this was proprietary to our work
keenetic = []
china = []
ipcam = []

#Their respective path lists
keeneticPaths = []
chinaPaths = []
ipcamPaths = []

auxPaths = []

#troubleshooting lists
trouble = []
duplicate = []

#Master Result dataframe
dfResult = pd.DataFrame({
    "Hex_Guid": [],
    "Firmware Name/ID": []
})
#Now into functions

#this is the function that parses the HTML file for the HEX and the firmware name
def parser(soup):
  #Key characteristic is the file extension at the end of the firmware image name
  for ext in extension:
    if soup.find_all(string=lambda text: text and ext in text):
      index_html = soup.find_all(string=lambda text: text and ext in text)
  #Remove the start command and any other garbage
      data = []
      for item in index_html:
        if 'var' in item and 'emba' not in item:
          data = item
      #now "data" is a string.
      data = str(data)
      #Going to split based on "/"
      data = data.split("/")
      #data is now a list
      #Now that we have those items in a list, we know we want the entry with the file extension and the one before it.
      
      answer = []
      for entry in data:
        for ext in extension:
          if ext in entry:
            
            answer = data[data.index(entry) - 1], data[data.index(entry)]
            
            if answer:
              dfResult.loc[len(dfResult)] = answer
          

  
  #Now looking for the "utsa" string in the path
  #This will pull the keenetic and the associated hash
  if soup.find_all(string=lambda text: text and "utsa" in text):
    
    index_html = soup.find_all(string=lambda text: text and "utsa" in text)
    
    index_html = list(index_html)
    index_html = str(index_html)
    index_html = index_html.replace('[', '').replace(']','').replace("'", "")
    index_html = index_html.split("/")
    #since these dont have the file extension, I will place them into their respective lists to loop over the master filepath list and compare to get each filepath with respect to each device's category
    
    #This if statement puts each hash in their respective categories
    for i in range(len(index_html)):
      if index_html[i] == 'tplink_china_routers':
        china.append(index_html[i+1])
        
      elif index_html[i] == 'keenetic':
        keenetic.append(index_html[i+1])
        
      elif index_html[i] == 'hikvision_ipcameras':
        ipcam.append(index_html[i+1])

#Takes the three lists of hexes throws them into a singular list for ease of running
def fileGlob():
  globbedHexes = []
  
  globbedHexes.extend(china)
  globbedHexes.extend(ipcam)
  globbedHexes.extend(keenetic)
  
  
  
  
  # for hex in china:  
  #   if hex not in globbedHexes:
  #     globbedHexes.append(hex)
  
  
  # for hex in ipcam:
  #   if hex not in globbedHexes:
  #     globbedHexes.append(hex)
  
  
  # for hex in keenetic:
  #   if hex not in globbedHexes:
  #     globbedHexes.append(hex)
  
  
  
  
  
  return globbedHexes

def fileRelater():
  #Different paths dont matter now, just put them all into a list and iterate this function once
  hexes = fileGlob()
  
  for item in hexes:
    num = hexes.index(item)
    print(num, item)
  
  
  
  
  
  
  
  # for hex in china:
  #   for master in masterFilepaths:
  #     if hex in master:
  #       chinaPaths.append(master)
  # print("China List Done!")
  
  # #Ipcams, putting ipcam into ipcamPaths
  # #relating paths from masterPaths
  
  # for hex in ipcam:
  #   for master in masterFilepaths:
  #     if hex in master:
  #       ipcamPaths.append(master)
  # print("IPcam List done!")
        
  # #keenetic, putting keenetic into keeneticPaths
  # #relating paths from masterPaths
  
  # for hex in keenetic:
  #   for master in masterFilepaths:
  #     if hex in master:
  #       keeneticPaths.append(master)
  # print("Keenetic List Done!")
  

def p60FileCollector(hexes):
  #it needs to reference both main path collector and whichever hex it needs because the paths as of now only list the index.html files
  #lets try for china first
  workPaths = []
  
  
  
  nakedPaths = []
  for path in masterFilepaths:
    path = str(path)
    path = path.replace("/index.html",'')
    nakedPaths.append(path)
  
  
  wipPaths = []
  for path in nakedPaths:
    if os.path.isdir(path):
      if os.path.isdir(path):
        for file in os.listdir(path):
          if 'p60' in file:
            wipPaths.append(path)
            file_path = os.path.join(path, file)
            workPaths.append(file_path)
  
  
  for master in masterFilepaths:
    for path in wipPaths:
      if path in master:
        pass
      else:
        full = path + "/p60_deep_extractor.html"
        if os.path.isfile(full):
          trouble.append(full)
        
  

    
  

    
      
  #return updatedPaths
  
    
  #now to add their respective filenames


#Working on the 3 other parser functions that will rely on the hash provided via one of the hash lists, and the master file path list for sync
#Returns the firmware file name 
def p60Parser(soup):
  
  p60 = soup.find_all(string=lambda text: text and "Start processing file" in text)
  
  p60 = list(p60)
  
  for item in p60:
    for ext in extension:
      if ext in item:
        #By doing this, it just chooses the last one that it found the file extension on, so it should work fine
        p60 = item
  p60 = str(p60)
  
  p60 = p60.split("/")
  #There is a space in the firmware name and the pid is still attached
  
  p60 = str(p60)
  p60 = p60.replace("'", "").replace(",", "")
  p60 = p60.split(" ")
  #Have it by itself, now to grab it
  
  answer = ""
  for ext in extension:
    for item in p60:
      if ext in item:
        answer = item
  return answer

#works!
def mainPathCollector():
  try:
      for var1 in os.listdir(bp):
        var1path = os.path.join(bp, var1)
        if os.path.isdir(var1path):
          for var2 in os.listdir(var1path):
            var2path=os.path.join(var1path, var2)
            if os.path.isdir(var2path):
              html_report_path = os.path.join(var2path, "html-report")
              if os.path.isdir(html_report_path):
                for file in os.listdir(html_report_path):
                  if file == "index.html":
                    file_path=os.path.join(html_report_path, file)
                    if os.path.isfile(file_path):
                      masterFilepaths.append((file_path))
                  
                      
  except:
    print("Issue reading file path!!!")


def masterReader():
  for i in range(len(masterFilepaths)):
    filepath = masterFilepaths[i]
    try:
      with open(filepath, 'r') as f:
        contents = f.read()
        index_html = bs(contents, 'lxml')
        parser(index_html)
        
    except:
      print("Didn't read correctly!")

  #Manual Block(parser)
  # with open("/home/daclocaladmin/Documents/Data_Analytics_I/firm_name_grabber/firm_grabber-main/Test Files/index.html", 'r') as f:
  #   contents = f.read()
  #   index_html = bs(contents, 'lxml')
  #   parser(index_html)

#reads and calls the p60parser, returns the associated firmware name and hex value
#Then appends the results to dfResult, should it exists, it can also throw the pairs into the duplicate list
def p60Reader(paths):
  #Reading in paths
  
  #Automated block
  updatedPaths = paths
  for i in range(len(updatedPaths)):
    path = updatedPaths[i]
    
    try:
      with open(path, 'r', encoding='utf-8', errors='replace') as f:
        contents = f.read()
        p60 = bs(contents, 'lxml')
        firmware = p60Parser(p60)
        #Now to associate it with the hex after getting the firmware name
        path = str(path)
        path = path.split("/")
        for i in range(len((path))):
          thing = path[i]
          if thing == "Whole_Emba_Collection":
            pair = path[i+1], firmware
        pair = list(pair)
        
        #Checking to see if the hex already exists 
        #This may need review
        # for index,_ in dfResult.iterrows():
        #   if index == thing:
        #     duplicate.append(thing)
        if firmware:
          dfResult.loc[len(dfResult)] = pair
        else:
          trouble.append(pair)
        
    except Exception as e:
      error = type(e).__name__
      print("This error occured:", error, "\nWith filepath: ", path)


  #Manual Block
  test = 'Insert individual file scan directory path here'
  with open(test, 'r', encoding='UTF-8', errors='replace') as f:
    contents = f.read()
    p60 = bs(contents, 'lxml')
    firmware = p60Parser(p60)
    
    #Now to associate it with the hex
    
    test = test.split("/")
    for i in range(len((test))):
      thing = test[i]
      if thing == "Whole_Emba_Collection":
        pair = test[i+1], firmware
    
    pair = list(pair)
    
    if pair:
      dfResult.loc[len(dfResult)] = pair
    



#Now onto the main function
def main():
  #Run pathCollector function to get filepaths
  mainPathCollector()
  #Reads the ones it can get, otherwise its thrown into the other lists
  masterReader()
  
  #lists the hex values after globbing them into a master list
  hexes = fileGlob()
  
  #Now to get the paths for the hexes relating to the master
  p60FileCollector(hexes)
  
  
    
  
  
  #We have the paths, now to run it to the reader to get the files, then it throws the resulting soup into the parser for data extraction
  # p60Reader(paths)
  
  # print(dfResult)
  
  # for item in duplicate:
  #   print("Duplicated file: ", item)
  
  num = 0
  # for item in trouble:
  #   num += 1
  #   print(f'Number {num} had trouble', item)
  
  
  #dfResult.to_csv("/home/daclocaladmin/Documents/Data_Analytics_I/firm_name_grabber/firm_grabber-main/output/smallResult.csv", index=False)
if __name__ == "__main__":
  main()
  
