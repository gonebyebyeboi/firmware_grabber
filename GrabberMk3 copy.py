#Mk3 is a much cleaner stripper, and will throw the data into a pandas dataframe for multiple index.html files
import pandas as pd
from bs4 import BeautifulSoup
import os


bp= "/home/daclocaladmin/Documents/Data_Analytics_I/Whole_Emba_Collection"

#this will contain all the file paths that align with the predefined path name
#Some scans will deviate from this path, but I will come up with a way to get those as well.
results1 = []

#Self.logger function may be important here





def __main__():
  ###Note, you will need to modify directory where index.html is located
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
                    print(file_path)
  except:
    print("Something up with the path")

  print(len(results1))
  # counter = 0
  # for var1, var2, file, path in results:
  #   print(f'Variable 1: {var1}, \nVariable 2: {var2}, \n File: {file}, \nPath: {path}\n')
  #   counter += 1

  # print(f'This is the total entries: {counter}')



  #This is a different little function
  # # paths = []
  # for file_path in results:
  #   paths.append(file_path)

  # for i in range(len(paths)):
  #   print(paths[i])




  for i in range(len(results1)):
    print(results1)
    
  
  with open("/home/daclocaladmin/Documents/Data_Analytics_I/firm_name_grabber/firm_grabber-main/Test Files/index.html", 'r') as f:
      
      contents = f.read()
      
      index_html= BeautifulSoup(contents, 'lxml')
      


  #The target is the tested firmware or the emba start command, which contains the file path that has the associated hex and firmware names

  
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
    extension = [".zip", ".bin", ".hex", ".rar", ".udp", ".update", ".rom", ".iso", ".elf", ".dfu"]
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

  if __name__=="__main__":
    main()
