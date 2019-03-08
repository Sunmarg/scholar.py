from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
filename="prod.csv"
f=open(filename,"w")
headers="Name_of_paper,Citations \n"
f.write(headers)
f.close()
f=open(filename,"a")
num='0'
while True:
    req= Request('https://scholar.google.com/scholar?start='+num+'&q=emnlp+2018&hl=en&as_sdt=0,5',headers={'User-Agent': 'Mozilla/5.0'})
    
    page_html=urlopen(req).read()
    page_soup=soup(page_html,"html.parser")
    finders=page_soup.findAll("div",{"class" : "gs_ri"})
    #print(len(finders))
    #print(soup.prettify(finders[0]))
    print (num)
    try:
        finder=finders[0]
    except:
        continue
    citation=finder.find("div",{"class": "gs_fl"})
    #print(citation[0].text)
    #print(finder.a.text)
     

    for finder in finders:
        name_of_paper=finder.a.text
        try:
            no_of_citations=finder.findAll("div",{"class": "gs_fl"})
        except IndexError:
            citation=no_of_citations[0].text.strip()
            #print(citation.text)
        
        trim_cite= citation.text.split(' ')
        #print(trim_cite)
        final_cite=trim_cite[4]
        #print(final_cite)
        if(final_cite.isdigit()):
            print( name_of_paper+" ,"+ final_cite+"\n")
            f.write(name_of_paper+" ,"+ final_cite+"\n")
        else:
            final_cite='0'
            print( name_of_paper+" ,"+ final_cite+"\n")
            f.write(name_of_paper+" ,"+ final_cite+"\n")
    num=int(num)
    num=num+10
    num=str(num)
f.close()
