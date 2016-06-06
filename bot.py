from bs4 import BeautifulSoup
import urllib

def get_rows():
    r = urllib.urlopen('http://amirbahador.com/HTML/AEC%20DateOfExam2015.htm').read()
    soup = BeautifulSoup(r, 'lxml')
    rows = soup.find_all("tr", {"height" : "32"})
    return rows

def parse_rows(rows):
    dic = {}
    for row in rows:
        children = row.find_all('td', recursive=False)
        test_name = children[1].getText().strip()

        if(test_name != "TOEFL iBT"):
            continue

        d = children[2].getText().strip(' \t\n\r')
        d = d.replace('\r','')
        d = d.replace('\n','')
        d = d.replace('\t','')
        dic[d] = [False, False, False, False, False]
        
        for i in range(5):
            val = children[5+i].getText().strip()
            print val
            if val.isdigit():
                dic[d][i] = True


    return dic


rows = get_rows()
dic = parse_rows(rows)
