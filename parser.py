# def parser(soup):
#   ###This first part is if the firmware name contains the file extension
#   index_html = soup.find_all('span', class_= "orange")
  
#   data = [tag.get_text() for tag in index_html]
#   #making sure data is a list
#   data = list(data)
  
#   for item in data:
#     if 'var' in item and 'emba' not in item:
#       data = item
  
#   #now "data" is a string.
#   data = str(data)
  
#   #Going to split based on "/"
#   data = data.split("/")
  
#   #data is now a list
#   #Now that we have those items in a list, we know we want the entry with the file extension and the one before it.
#   extension = [".zip", ".bin", ".hex", ".rar", ".udp", ".update", ".rom", ".iso", ".elf", ".dfu"]
#   answer = []
#   for entry in data:
#     for ext in extension:
#       if ext in entry:
#         answer = data[data.index(entry) -1], data[data.index(entry)]
#         dfResult.loc[len(dfResult)] = answer