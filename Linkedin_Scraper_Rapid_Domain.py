import requests
import re

filename = "input.txt"
mynumbers = []
with open(filename) as f:
    for line in f:
        mynumbers.append([str(n) for n in line.strip().split("&")])
        #print(mynumbers)
for pair in mynumbers:  
    x,y,z = pair[0],pair[1],pair[2]
    print(x)
    #print(x)
    #print(Z)
    x = x.strip()
    y = y.strip()
    z = z.strip()

    url = "https://linkedin-company-data.p.rapidapi.com/linkedInCompanyDataByDomainJson"

    payload = {"domains": [x]}
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "d10d4b10a3mshec83724d6602eb0p13bc13jsnbe5f7f65011f",
    "X-RapidAPI-Host": "linkedin-company-data.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    #print(response.text)
    prodPgSrc = str(response.text)
    #input()
    reviewPgFl = open('CompanyInfo.html', 'w', encoding='utf-8')
    reviewPgFl.write(prodPgSrc)
    reviewPgFl.close() 
    curEleurl = re.search("CompanyLIUrl\"\:\s*\"([^>]*?)\"\,",prodPgSrc)
    if curEleurl != None:
       linkedin = curEleurl.group(1)
    curEle = re.search('(Employees[\w\W]*?Locations)',prodPgSrc)
    
    if curEle != None:
        curr = curEle.group(1)
        #print(curr)
        grouped=re.findall('\"(Name\"\:\s*\"[^>]*?\"\,\s*\"Title\"\:\s*\"[^>]*?\"\,\s*\"Link\"\:\s*\"[^>]*?\")',curr)
        for each_profile in grouped:
            profile_name=''
            designation=''
            linlid=''
            curEle=re.search("Name\"\:\s*\"([^>]*?)\"\,",each_profile)
            if curEle != None:
                profile_name = curEle.group(1)
            curEle=re.search("Title\"\:\s*\"([^>]*?)\"\,",each_profile)
            if curEle != None:
                designation = curEle.group(1)
            curEle=re.search("\"Link\"\:\s*\"([^>]*?)\"",each_profile)
            if curEle != None:
                linlid = curEle.group(1)
            print(profile_name)
            print(designation)
            print(linlid)
            print(linkedin)
            #input()
            filenamef = "Rapid.txt"
            output_contet=str(x)+ "\t" + str(y) + "\t" + str(z) + "\t" + str(profile_name)+ "\t" + str(designation)+ "\t" + str(linlid) + "\t" + str(linkedin)+"\n"
            do = open(filenamef, "a",encoding='utf-8')
            do.write(output_contet) 
            do.close()