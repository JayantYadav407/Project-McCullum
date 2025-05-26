import instaloader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests





def load(url): 
    loader = instaloader.Instaloader()
    post_url = url
    shortcode = post_url.split("/")[-2]

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        if post.is_video:
            loader.download_post(post, target="video_downloads")
            print("Video download completed.")
        else:
            print("The post does not contain a video.")
    except Exception as e:
        print("An error occurred:", e)



with open('link.txt','r',encoding='UTF-8') as f:
   text =  f.read()
list = text.split(',')
 
    
response = requests.post("https://www.savethevideo.com/home","/p/CpXvzPQrqcc/")
 
driver = webdriver.Chrome()
count = 0
for i in list:
    if count >0 and count<len(list)-2:
        try:
            modified_string = i[2:-1]
            url =f"https://www.instagram.com{modified_string}"
            load(url)
        except Exception as e:
    
            print("An error occurred:", e)
    count = count +1
    time.sleep(5)







