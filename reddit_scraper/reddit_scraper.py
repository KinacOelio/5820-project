# This is an example of how praw can be used to scrape data from a subreddit. In this case, r/SubSimulatorGPT2.
# keywords are used to denote the beginning and and of a title and of a comment to help it generate comments better.
# this may or may not be a good way to do it.
# output is also included.

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
SubSimulatorGPT2_comments = open('SubSimulatorGPT2_comments.txt', 'w', encoding='utf-8')

# iterates through maximum allowable posts in the subreddit
for submission in reddit.subreddit("SubSimulatorGPT2").hot():
    print(submission.title)
    # writes the title
    SubSimulatorGPT2_comments.write("[TITLE] " + submission.title + " [TITLE]\n")
    top_level_comments = list(submission.comments)
    # then iterates through and writes all top level comments
    for comment in top_level_comments:
        SubSimulatorGPT2_comments.write(("[start] " + comment.body + " [end]").replace("\n", " ") + "\n")
