from bs4 import BeautifulSoup
import requests
import json

def scrape(subred_url: str) -> dict:
    '''
    Scrape the subreddit and return the json data
    subred_url: str - the subreddit url
    '''
    r = requests.get(subred_url, headers={'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.text, 'html.parser')
    json_data = json.loads(soup.text)

    return json_data

def generate_md(json_data: dict, upvotes: str, downvotes: str, comments: str, subred_url: str) -> None:
    '''
    Generate the markdown file
    json_data: dict - the json data
    upvotes: str - include upvotes
    downvotes: str - include downvotes
    comments: str - include comments
    subred_url: str - the subreddit url
    '''
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