#Mk3 is a much cleaner stripper, and will throw the data into a pandas dataframe for multiple index.html files
from bs4 import BeautifulSoup
import pandas as pd
###Note, you will need to modify directory where index.html is located
with open('C:\Development\Research\CA1\Firm_grabber\Test Files\index.html', 'r') as f:
    
    contents = f.read()
    
    index_html= BeautifulSoup(contents, 'lxml')
    


#Target: /var/www/active/0427922f-f9b3-4baf-83d8-3548f2de25c1/DIS-200G-SERIES_REVA_FIRMWARE_v1.20.007.zip

#try to add more arguments, like the firmware file extension types
def parser(soup):
  index_html = soup.find_all('span', class_= "orange")
  
  data = [tag.get_text() for tag in index_html]
  #making sure data is a list
  data = list(data)
  
  for item in data:
    if 'var' in item and 'emba' not in item:
      data = item
  
  #now "data" is a string.
  data = str(data)
  
  #Going to split based on "/"
  data = data.split("/")
  
  #data is now a list
  #Now that we have those items in a list, we know we want the entry with the file extension and the one before it.
  extension = [".zip", ".bin", ".hex"]
  answer = []
  for entry in data:
    for ext in extension:
      if ext in entry:
        answer = data[data.index(entry) -1], data[data.index(entry)]
        
 
  #Now, I'm going to put that list into a data frame, and append any additional matches found
  data = pd.DataFrame({
    "Hex_Guid": [],
    "Firmware": []
  })
  data.loc[len(data)] = answer
  print(data)
  
  
parser(index_html)