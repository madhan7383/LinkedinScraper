import requests
import re

filename = "input_linkid.txt"
mynumbers = []

filenamef = "Rapid_Emp.txt"
output_contet= "Id\tUnique Number\tTotal Count\tuniversal_name\ttitle\tfirst_name\tlast_name\timage_url\n"
do = open(filenamef, "w",encoding='utf-8')
do.write(output_contet) 
do.close()

def scrape_data(prodPgSrc):
    reviewPgFl = open('LINKEDINPAGE2.html', 'w', encoding='utf-8')
    reviewPgFl.write(prodPgSrc)
    reviewPgFl.close()  

    curEle = re.search('(employees[\w\W]*?start_at)',prodPgSrc)
    if curEle != None:
        curr = curEle.group(1)
        print(curr)
        grouped=re.findall('(universal_name\"\:\s*\"[^>]*?\"\,\s*\"title\"\:\s*\"[^>]*?\"\,\s*\"first_name\"\:\s*\"[^>]*?\"\,\s*\"last_name\"\:\s*\"[^>]*?\"\,\s*\"image_url\"\:\s*\"[^>]*?\")',curr)
        for each_profile in grouped:
            universal_name=''
            title=''
            first_name=''
            last_name=''
            image_url=''
            curEle=re.search("universal_name\"\:\s*\"([^>]*?)\"\,",each_profile)
            if curEle != None:
                universal_name = curEle.group(1)
            curEle=re.search("title\"\:\s*\"([^>]*?)\"\,",each_profile)
            if curEle != None:
                title = curEle.group(1)
            curEle=re.search("\"first_name\"\:\s*\"([^>]*?)\"",each_profile)
            if curEle != None:
                first_name = curEle.group(1)
            curEle=re.search("\"last_name\"\:\s*\"([^>]*?)\"",each_profile)
            if curEle != None:
                last_name = curEle.group(1)
            curEle=re.search("\"image_url\"\:\s*\"([^>]*?)\"",each_profile)
            if curEle != None:
                image_url = curEle.group(1)
            # print(universal_name)
            # print(title)
            # print(first_name)
            # print(last_name)
            # print(image_url)
            filenamef = "Rapid_Emp.txt"
            output_contet=str(x)+ "\t" + str(y) + "\t" + str(z) + "\t" + str('https://www.linkedin.com/in/')+str(universal_name)+ "\t" + str(title)+ "\t" + str(first_name)+ "\t" + str(last_name)+ "\t" + str(image_url) +"\n"
            do = open(filenamef, "a",encoding='utf-8')
            do.write(output_contet) 
            do.close()
        # curPager = curPager+1
        # print(curPager)
with open(filename) as f:
    for line in f:
        mynumbers.append([str(n) for n in line.strip().split("&")])
        #print(mynumbers)
for pair in mynumbers:  
    x,y,z = pair[0],pair[1],pair[2]
    print(y)
    #print(x)
    #print(Z)
    x = x.strip()
    y = y.strip()
    z = z.strip()

    url = "https://linkedin-company-data.p.rapidapi.com/companyEmployees"

    payload = {
        "company_id": x,
        "per_page": 50,
        "offset": 0
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "d10d4b10a3mshec83724d6602eb0p13bc13jsnbe5f7f65011f",
        "X-RapidAPI-Host": "linkedin-company-data.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    
    # print(response.text)
    prodPgSrc = str(response.text)
    # prodPgSrc=''
    reviewPgFl = open('LINKEDINPAGE1.html', 'w', encoding='utf-8')
    reviewPgFl.write(prodPgSrc)
    reviewPgFl.close()  
    scrape_data(prodPgSrc)
    #"total": 1683,
    total_reviews=''
    curEle = re.search('\"total\"\:\s*(\d+)\,',prodPgSrc)
    if curEle != None:
        total_reviews = curEle.group(1)
     
    # total_reviews=161
    try:
        total_reviews = int(total_reviews)
    except:
        print("Total Reviews Exception: "+ str(total_reviews))
    # if total_reviews!= 0:   
         
    print("Total Executives" + str(total_reviews))
    
    # input()
    totalPgsCnt = 1
    if total_reviews > 51:
        totalPgsCnt = 0
        totalPgsCnt = int(total_reviews)/50
        tmpRevPgsCnt = str(totalPgsCnt).split(".")
        totalPgsCnt = tmpRevPgsCnt[0]
        if(len(tmpRevPgsCnt)>0):
            totalPgsCnt = int(totalPgsCnt) + 1
        print("Total Pages Found: " + str(totalPgsCnt)) 
        # input("Wait")
    print(totalPgsCnt)   
    if totalPgsCnt>=1:
        curPager = 1
        while(curPager<totalPgsCnt):
            print(curPager)
            #print(totalPgsCnt)
            print("Im in")
            # input()
            
            url = "https://linkedin-company-data.p.rapidapi.com/companyEmployees"

            payload = {
                "company_id": x,
                "per_page": 50,
                "offset": curPager
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "d10d4b10a3mshec83724d6602eb0p13bc13jsnbe5f7f65011f",
                "X-RapidAPI-Host": "linkedin-company-data.p.rapidapi.com"
            }
            response = requests.request("POST", url, json=payload, headers=headers)
            
            #print(response.text)
            prodPgSrc = str(response.text)
            scrape_data(prodPgSrc)
            curPager = curPager+1
            