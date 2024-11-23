
#Importing the libraries needed
import pandas as pd
from bs4 import BeautifulSoup
import os


#Now getting into some global variables


#This is the path that stays the same for the index.html file
###You will need to modify this for the code to work outside the DAC###

bp= "/home/daclocaladmin/Documents/Data_Analytics_I/Whole_Emba_Collection"

#this will contain all the file paths that align with the predefined path name
#Some scans will deviate from this path, but I will come up with a way to get those as well.
results1 = []


#Resulting dataframe

dfResult = pd.DataFrame({
    "Hex_Guid": [],
    "Firmware": []
  })
#Now into functions

#this is the function that parses the HTML file for the HEX and the firmware name
def parser(soup):
  ###This first part is if the firmware name contains the file extension
  # index_html = soup.find_all('span', class_= "orange")
  
  # index_html = list(index_html)
  
  # for item in index_html:
  #   item = str(item)
  #   if 'var' in item and 'emba' not in item:
  #     string = item
    
  # print(string)

  #Key characteristic "keenetic"
  index_html = soup.find_all('span', class_= "orange")
  index_html = list(index_html)
  for item in index_html:
    item = str(item)
    if "scan" not in item:
      if "keenetic" in item:
        string = item
    
  print(string)
  
  
  
  
  
  
  
  #Little extension dictionary
  extension = [".zip", ".bin", ".hex", ".rar", ".udp", ".update", ".rom", ".iso", ".elf", ".dfu"]
  
  index_html = list(index_html)
  
  #loops over each entry and gets the text
  index_html = [tag.get_text() for tag in index_html]
  #Remove the start command and any other garbage
  
  data = []
  for item in index_html:
    for ext in extension:
      if ext in item:
        data.append(item)
  
  
  
  #Now I have it as the simple path, now will put it as a list and compare against the extensions dictionary 
  
  
  
  
  # print(data)
  # #making sure data is a list
  
  # for item in data:
  #   if 'var' in item and 'emba' not in item:
  #     data = item
  
  # #now "data" is a string.
  # data = str(data)
  
  # #Going to split based on "/"
  # data = data.split("/")
  
  # #data is now a list
  # #Now that we have those items in a list, we know we want the entry with the file extension and the one before it.
  # extension = [".zip", ".bin", ".hex", ".rar", ".udp", ".update", ".rom", ".iso", ".elf", ".dfu"]
  # answer = []
  # for entry in data:
  #   for ext in extension:
  #     if ext in entry:
  #       answer = data[data.index(entry) -1], data[data.index(entry)]
  #       dfResult.loc[len(dfResult)] = answer

  #Now, I'm going to put that list into a data frame, and append any additional matches found
  #checking for the different characteristic
  
  
  
  #dfResult.loc[len(dfResult)] = answer
  


#Now onto the main function
def main():

  #This grabs the file paths and throws it into the "results" list
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
                      results1.append((file_path))
                      
  except:
    print("Something up with the path")
  
  
  #this function opens the files(Still need to edit it to do it.)
  #Lets try a for loop
  #                                                                               HEX                           Number      folder                        
  #Path: /home/daclocaladmin/Documents/Data_Analytics_I/Whole_Emba_Collection/000ddfaf591c2853d7a46acb8af69c33/1726336310/html-report
  # trouble = []
  # for file in range(len(results1)):
  #   try:
  #     filename = results1[file]
  #     with open(filename, 'r') as f:
  #       contents = f.read()
  #       index_html= BeautifulSoup(contents, 'lxml')
        
  #       parser(index_html)
  #   except:
      
  #     trouble.append(filename)
  
  ###index without extension
  #/home/daclocaladmin/Documents/Data_Analytics_I/Whole_Emba_Collection/e9ea6138ef11c95211d304a8ea6e3a3a/1726186758/html-report/index.html
  
  ###index with extension
  #/home/daclocaladmin/Documents/Data_Analytics_I/firm_name_grabber/firm_grabber-main/Test Files/index.html
  with open("/home/daclocaladmin/Documents/Data_Analytics_I/Whole_Emba_Collection/e9ea6138ef11c95211d304a8ea6e3a3a/1726186758/html-report/index.html", 'r') as f:
        contents = f.read()
        index_html= BeautifulSoup(contents, 'lxml')
  parser(index_html)
  
  
  
  
  
if __name__ == "__main__":
  main()