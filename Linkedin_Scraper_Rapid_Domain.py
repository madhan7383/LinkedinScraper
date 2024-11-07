import requests
import re
import json

filename = "input"+str(sys.argv[1])+".txt"
mynumbers = []
with open(filename) as f:
    for line in f:
        mynumbers.append([str(n) for n in line.strip().split("&")])
        #print(mynumbers)
Header_List = ["Industries","Industries","CompanySize","Headquarters","Type","Founded","CompanyLIUrl","Description","OriginalLIUrl","EmployeeCountOnLI","CompanyName","Logo","FundingInfo","Employees","Domain"]
Address_Header_List = ["type","streetAddress","addressLocality","addressRegion","postalCode","addressCountry"]
header_info = Header_List+Address_Header_List
File_Header = open("Rapid"+str(sys.argv[1])+".txt", 'w', encoding='utf-8') 
File_Header.write("\t".join(str(v) for v in header_info)+'\n')
File_Header.close()
for pair in mynumbers:  
    x,y,z = pair[0],pair[1],pair[2]
    print(x)
    #print(x)
    #print(Z)
    x = x.strip()
    y = y.strip()
    z = z.strip()

    url = "https://linkedin-company-data.p.rapidapi.com/linkedInCompanyDataByDomain"

    payload = {"domains": [x]}
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "d10d4b10a3mshec83724d6602eb0p13bc13jsnbe5f7f65011f",
    "X-RapidAPI-Host": "linkedin-company-data.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    #print(response.text)
    response_txt = str(response.text)
    # response_txt = str(open('CompanyInfo.txt', 'r').read())

    
    reviewPgFl = open("Updated_CompanyInfo"+str(sys.argv[1])+".txt", 'w', encoding='utf-8') 
    reviewPgFl.write(response_txt)
    reviewPgFl.close()
    Company_Data = json.loads(response_txt)

    #input()
    
    for Company_Info in Company_Data:
        # reviewPgFl = open('CompanyInfo__1.json', 'w', encoding='utf-8') 
        # reviewPgFl.write(json.dumps(Company_Info, indent=4))
        # reviewPgFl.close()
        
        # Company_Info_json = json.loads(Company_Info)
        Detail_List = []
        for header in Header_List:
            Str_data = str(Company_Info.get(header))
            Str_data = Str_data.replace("\\/", "/").encode().decode('unicode_escape')
            Str_data = ''.join(Str_data.splitlines())
            Detail_List.append(Str_data)
            
        Address_list = Company_Info.get("Primary_Loc_Parsed")
        if(type(Address_list)==dict):
            for Address_header in Address_Header_List:
                Str_data = str(Address_list.get(Address_header))
                Str_data = Str_data.replace("\\/", "/").encode().decode('unicode_escape')
                Str_data = ''.join(Str_data.splitlines())
                Detail_List.append(Str_data)
                
        File_Detail = open("Rapid"+str(sys.argv[1])+".txt", 'a', encoding='utf-8') 
        File_Detail.write("\t".join(str(v) for v in Detail_List)+'\n')
        File_Detail.close()