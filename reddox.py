
subreddit = input("Enter a subreddit url: /r/")
print("You entered: reddit.com/r/" + subreddit)

upvotes = input("Do you want to include the number of upvotes : (y/n)[default: n] ")
while upvotes != "y" and upvotes != "n" and upvotes != "":
    upvotes = input("Please enter y or n : (y/n)[default: n] ")
    if upvotes == "y" or upvotes == "n" or upvotes == "":
        break

downvotes = input("Do you want to include the number of downvotes : (y/n)[default: n] ")
while downvotes != "y" and downvotes != "n" and downvotes != "":
    downvotes = input("Please enter y or n : (y/n)[default: n] ")
    if downvotes == "y" or downvotes == "n" or downvotes == "":
        break


num_posts = input("Enter the number of posts to scrape : (for 10 posts press enter) ")

while num_posts.isdigit() == False or int(num_posts) <= 0:
    if num_posts == "":
        num_posts = 10
        print("You entered: " + str(num_posts))
        break
    num_posts = input("Atleast 1 post is required to scrape. Enter the number of posts to scrape : (for 10 posts press enter) ")
    print("You entered: " + str(num_posts))

comments = input("comments :=> (click enter) ")
while comments != "y" or comments != "n" or comments != "":
    comments = input("Please enter y or n : (y/n)[default: 0 comments] ")
    if comments == "y":
        num_comments = input("Enter the number of comments to scrape : (for 10 comments press enter) ")
        while num_comments.isdigit() == False or int(num_comments) <= 0:
            if num_comments == "":
                num_comments = 10
                break
                print("You entered: " + str(num_comments))
            num_comments = input("Atleast 1 comment is required to scrape. Enter the number of comments to scrape : (for 10 comments press enter) ")
            print("You entered: " + str(num_comments))
        break
    elif comments == "n" or comments == "":
        num_comments = 0
        break
    else:
        comments = input("Please enter y or n : (y/n)[default: 0 comments] ")

print("converting .....")

def isdigit(num_posts):
    if type(num_posts) == True:
        return True
    else:
        return False
subred_url = "https://www.reddit.com/r/" + subreddit + "/top.json?t=all&limit=" + str(num_posts) 

print(subred_url)
# fetch json data from url with beautiful soup 
import requests
from bs4 import BeautifulSoup
import json


r = requests.get(subred_url, headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(r.text, 'html.parser') 
#print(soup)
json_data = json.loads(soup.text)
#                 data  | children | data index | title
# print(json_data['data']['children'][0]['data']['title'])
md_data = ""
md_data += "All this posts are from: " + subred_url + "\n"
for i in json_data['data']['children']:
    md_data += '# ' + i['data']['title'] + "\n"
    md_data += "- " + i['data']['selftext'] + "\n"
    if upvotes == "y":
        md_data += "### upvotes: " + str(i['data']['ups']) + "\n"
    if downvotes == "y":
        md_data += "### downvotes: " + str(i['data']['downs']) + "\n"
    if comments == "y":
        md_data += "## comments: " + str(i['data']['num_comments']) + "\n"
# write md_data to a file
with open("reddit.md", "w", encoding="utf-8") as f:
    f.write(md_data)
