from bs4 import BeautifulSoup

with open('C:\Development\Research\CA1\Firm_grabber\index.html', 'r') as f:
    
    contents = f.read()
    
    soup = BeautifulSoup(contents, 'lxml')

print(soup)