from modules import scraper

def checker(str_var, default = 'n') -> str:
    '''
    Check if the user entered y or n and return the input in lowercase
    str_var: str - the user input
    default: str - the default value 
    '''
    while str_var.lower() != "y" and str_var.lower() != "n" and str_var != "":
        str_var = input(f"Please enter y or n : (y/n)[default: {default}] ")
        if str_var.lower() == "y" or str_var.lower() == "n" or str_var == "":
           break

    return str_var.lower()

def checker_int(int_value, text_print: str, default = 10) -> int:
    '''
    Check if the user entered an integer and return the input
    int_value: str - the user input
    text_print: str - the text to print
    default: int - the default value
    '''
    while int_value <= 0:
        try:
            int_value = int(input(text_print))
            print("You entered : " + str(int_value))
            break

        except ValueError as e:
            if int_value == "":
                int_value = 10
                print("You entered: " + str(int_value))
                break

    return int(int_value)

subreddit = input("Enter a subreddit url: /r/") 
print("You entered: reddit.com/r/" + subreddit)

upvotes = str(input("Do you want to include the number of upvotes : (y/n)[default: n] "))
upvotes = checker(upvotes, 'n')

downvotes = str(input("Do you want to include the number of downvotes : (y/n)[default: n] "))
downvotes = checker(downvotes, 'n')

num_posts = checker_int(0, "Enter the number of posts to scrape : (for 10 posts press enter) ", 10)

comments = input("comments :=> (click enter) ")
comments = checker(comments, '0')

if comments == "y":
    num_comments = checker_int(0, "Enter the number of comments to scrape : (for 10 comments press enter) ", 10)

elif comments == "n" or comments == "":
    num_comments = 0

print("converting .....")

subred_url = "https://www.reddit.com/r/" + subreddit + "/top.json?t=all&limit=" + str(num_posts) 

print(subred_url)

# scrape the subreddit and generate the markdown file
data = scraper.scrape(subred_url)
scraper.generate_md(data, upvotes, downvotes, comments, subred_url)