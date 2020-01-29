from urllib.request import urlopen 

id="Q5SLP9"
url="http://www.uniprot.org/uniprot/"+id+".txt"

data = urlopen(url).read().decode('utf-8')
with open('answer1.txt', 'a') as file:            
    file.write(data)
