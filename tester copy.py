
from bs4 import BeautifulSoup

#Note, change directory to match emba scan
with open('C:\Development\Research\CA1\Firm_grabber\index.html', 'r') as f:
    
    contents = f.read()
    
    index_html= BeautifulSoup(contents, 'lxml')
#Target: Tested firmware:</span><span class="orange"> /var/www/active/0427922f-f9b3-4baf-83d8-3548f2de25c1/DIS-200G-SERIES_REVA_FIRMWARE_v1.20.007.zip</span></span></pre>
def parser(soup):
  firmware = soup.find_all('span', class_= "orange")
  firmware = list(firmware)
  data = []
  for item in firmware:
    item = str(item)
    data.append(item)
  
  lists = ""
  for item in data:
    if 'var' in item and 'emba' not in item:
      lists = str(item)
  #now we have "<span class="orange"> /var/www/active/0427922f-f9b3-4baf-83d8-3548f2de25c1/DIS-200G-SERIES_REVA_FIRMWARE_v1.20.007.zip</span>"
  lists = lists.strip("""<span class="orange">""")
  lists = lists.split('/')
  #after this command, it is now a list
  #lets filter for what we want
  
  answer = []
  
  for item in lists:
    if '.zip' in item or '.bin' in item or '.hex' in item:
      answer.append(lists[lists.index(item) - 1])
      answer.append(item)
  
  print(answer)
      
  # answer = answer.replace("""<span class="orange">""", '')
  # answer = answer.split('/')
  # for item in answer:
  #   if ".zip" in item or ".bin" in item or ".hex" in item:
  #     print(item)
  

parser(index_html)
