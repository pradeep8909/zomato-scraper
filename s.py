from bs4 import BeautifulSoup
import requests,pprint
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.zomato.com/ncr')

page = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

#############------------------------ task-1
soup = BeautifulSoup(page,"html.parser")
# print(soup)
div_1 = soup.find("div",class_="ui segment row")
# print(div_1)
a_tag =  div_1.find_all("a")

list_for_links = []
restaurants_links=[]
for i in a_tag:
    link=(i['href'])
    list_for_links.append(link)
# print(list_for_links)



##################------- geting the no. of the resturant in the particular locality
all_data=[]
num=0
for i in a_tag:
    num+=1
    s=i.find("span").get_text()
    sli=s[1:-1]
    # print(sli)

    link=(i.get_text().strip())
    a=""
    for k in link:
        # print(k)
        if  k == "(":
            break
        else:
            a+=k
    # print(str(num)+"."+" ", a)
    # print("      total restaurants ==  " ,sli)
    restaurant = {}
    s_no=str(num)

    name=(a).strip()
    restaurant[s_no]=name
    restaurant["Total resturants"]=sli
    restaurant["link"]=list_for_links[num-1]
    all_data.append(restaurant)
pprint.pprint(all_data)   


########----------task2 details of all the resturants
print("+++++++++++")
print("@@@@@@@@@@@@@@@@@@@")
user_input=int(input("Give the place number in which you wnat to ENTER?"))
print("@###############")
i=0
for i in range(len(all_data)):
    if i== user_input:
        soup1=(all_data[i-1]["link"])
        driver = webdriver.Chrome()
        driver.get(soup1)
        page1 = driver.execute_script("return document.documentElement.outerHTML")
        driver.quit()
        
        driver = BeautifulSoup(page1,"html.parser")
        # print(driver)
        divs = driver.find("div",class_="subzone-content")
        # print(divs)
        divs1 = divs.find_all("div")
        # print(divs1)
        li=[]
        s=1
        for i in divs1:
            name_1={}
            type=i.find("div",class_="fontsize1 semi-bold mt2")
            
            try:
                see_all=i.find("div",class_="cat-subzone-res ptop0 ml15 mr20")
                see_more_link=see_all.find("div",class_="pb5 bt ptop0 ta-right")
                a_link=see_more_link.find("a")["href"]
                res_name=(type.get_text()).strip()
                name_1["Num"]=s
                s+=1
                name_1[res_name]=a_link
                li.append(name_1)

                # print(name_1)
                
            except :
                continue   
        pprint.pprint(li)  


# #############--------------------- finding an resturant..

print("&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("*********************")
user_input1=int(input("Write the number for ENTERING in the particular type of the resturant?"))
print("^^^^^^^^^^^^^^^^^^^^^")
print("->->->->->->->->")
values=li[user_input1-1]
a=[]
for i in values:
    a.append(i)
a=a[1]
link2=values[a]
driver = webdriver.Chrome()
driver.get(link2)
page2 = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
a=[]
driver = BeautifulSoup(page2,"html.parser")
res_data=driver.find_all("article")
final_dictor={}
id=0

for i in res_data:
    #___________________finding all the name of the resturant
    names=i.find_all("a",class_="result-title hover_feedback zred bold ln24 fontsize0 ")
    for j in names:
        r_name=j.get_text().strip()
        # print(r_name)
        final_dictor["Name"]=r_name


        #___________________finding all the location of the resturant
    location=i.find_all("a",class_="ln24 search-page-text mr10 zblack search_result_subzone left")
    for x in location:
        r_location=x.get_text().strip()
        # print(r_location)
        final_dictor["Adrres"]=r_location

        #___________________finding all the rating of the resturant
    rating=i.find("div",class_="ta-right floating search_result_rating col-s-4 clearfix") 
    final_rating=rating.find("div").get_text().strip()  
    # print(final_rating)
    final_dictor["Rating"]=final_rating


    #___________________finding all the review of the resturant
    review=i.find("span").get_text()
    # print(review)
    final_dictor["Number of reviews"]=review

    #___________________Updating the id of the resturant
    final_dictor["Id"]=id+1
    id+=1


    #___________________finding price of the resturant
    cost=i.find("span",class_="col-s-11 col-m-12 pl0")
    final_cost=cost.get_text()
    final_dictor["Price"]=final_cost
    # print(final_cost)
    print(final_dictor)







