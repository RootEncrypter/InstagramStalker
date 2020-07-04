import requests,os,openpyxl
from datetime import date

def dataScraper(u_name):
    
    headers = {
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com',
        'Connection': 'keep-alive',
    }

    url ='https://www.instagram.com/'+u_name


    params = {
        '__a': '1'

    }

    r = requests.get(url=url, headers=headers,params= params )

    global p_id
    global username
    global fullname
    global bio
    global posts
    global followers
    global following
    global profpic
    global status
    global s_data
    global t_date

    data = r.json()
    p_id = data["graphql"]["user"]["id"]
    username= data["graphql"]["user"]["username"]
    fullname= data["graphql"]["user"]["full_name"]
    bio = data["graphql"]["user"]["biography"]
    posts = data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
    followers = data["graphql"]["user"][ "edge_followed_by"]["count"]
    following = data["graphql"]["user"]["edge_follow"]["count"]
    profpic = data["graphql"]["user"]["profile_pic_url_hd"]

    get_status = data["graphql"]["user"]["is_private"]
    if get_status == True:
        status='Private'
    else :
        status ='Public'

    t_day =date.today()

    s_data= [fullname,username,p_id,posts,followers,following,status,profpic,t_day]
    return s_data
    # print(fullname,username,p_id,posts,followers,following,status,profpic)

def extractData(s_data):
    global wb
    title_data=['Full Name','Username','ID','Posts','Followers','Following','Status','Profile Pic']
    os.chdir('C:\\Users\\Shaun\\Desktop\\python practrice') #change the directory to your folder
    wb = openpyxl.load_workbook('data.xlsx')   #devnote create a excel file in the directory you are using
    sheet = wb.active
    sheet.title = 'StalkerData'
    sheet['A1']. value = 'Full Name'
    sheet['B1']. value = 'Username'
    sheet['C1']. value = 'ID'
    sheet['D1']. value = 'Posts'
    sheet['E1']. value = 'Followers'
    sheet['F1']. value = 'Following'
    sheet['G1']. value = 'Status'
    sheet['H1']. value = 'Profile Pic'
    sheet['I1']. value = 'TimeStamp'
    sheet.append(s_data)
    wb.save('data.xlsx')
    wb.close()
    
    
        
        
    
        
            
  
        

    
        
    
ulist = ['_shaunnyboi_'] #add your friends username in this list

print("Data Extracted!...Saving Data Please Wait!...")
for u_name in ulist:
    dataScraper(u_name)
    
    # print(fullname,username,p_id,posts,followers,following,status,profpic)
    # print(s_data)
    extractData(s_data)
print("Data Saved...")
    
  