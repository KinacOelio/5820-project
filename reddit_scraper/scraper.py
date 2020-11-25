# This is an example of how praw can be used to scrape data from a subreddit. 
# keywords are used to denote the beginning and and of a title and of a comment to help it generate comments better.
# this may or may not be a good way to do it.


import praw

reddit = praw.Reddit(
    client_id="SMoB8JGhtjXOPA",
    client_secret="QK7QAlrOrOl2SsnK7eQIH3vBKFs",
    # password="Craven0",
    user_agent="fugmatoad",
    # validate_on_submit=True,
    # username="fugmatoad"
)

# creates the file to write to
askreddit_comments = open('askreddit.txt', 'a', encoding='utf-8')
# iterates through maximum allowable posts in the subreddit
for submission in reddit.subreddit("askreddit").hot():
    print(submission.title)
    # writes the title
    askreddit_comments.write("[TITLE] " + submission.title + " [TITLE]\n")
    submission.comments.replace_more(limit=0)
    top_level_comments = list(submission.comments)
    # then iterates through and writes all top level comments
    for comment in top_level_comments:
        askreddit_comments.write(("[start] " + comment.body + " [end]").replace("\n", " ") + "\n")


# creates the file to write to
politics_comments = open('politics.txt', 'a', encoding='utf-8')
# iterates through maximum allowable posts in the subreddit
for submission in reddit.subreddit("politics").hot():
    print(submission.title)
    # writes the title
    politics_comments.write("[TITLE] " + submission.title + " [TITLE]\n")
    submission.comments.replace_more(limit=0)
    top_level_comments = list(submission.comments)
    # then iterates through and writes all top level comments
    for comment in top_level_comments:
        politics_comments.write(("[start] " + comment.body + " [end]").replace("\n", " ") + "\n")


# creates the file to write to
self_comments = open('self.txt', 'a', encoding='utf-8')
# iterates through maximum allowable posts in the subreddit
for submission in reddit.subreddit("self").hot():
    print(submission.title)
    # writes the title
    self_comments.write("[TITLE] " + submission.title + " [TITLE]\n")
    submission.comments.replace_more(limit=0)
    top_level_comments = list(submission.comments)
    # then iterates through and writes all top level comments
    for comment in top_level_comments:
        self_comments.write(("[start] " + comment.body + " [end]").replace("\n", " ") + "\n")


# creates the file to write to
ProgrammerHumor_comments = open('ProgrammerHumor.txt', 'a', encoding='utf-8')
# iterates through maximum allowable posts in the subreddit
for submission in reddit.subreddit("ProgrammerHumor").hot():
    print(submission.title)
    # writes the title
    ProgrammerHumor_comments.write("[TITLE] " + submission.title + " [TITLE]\n")
    submission.comments.replace_more(limit=0)
    top_level_comments = list(submission.comments)
    # then iterates through and writes all top level comments
    for comment in top_level_comments:
        ProgrammerHumor_comments.write(("[start] " + comment.body + " [end]").replace("\n", " ") + "\n")
