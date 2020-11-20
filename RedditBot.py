# imports
import gpt_2_simple as gpt2
from datetime import datetime
import praw
import time


# List of subreddits
subreddits = ["askreddit", "politics", "ProgrammerHumor", "self"]

#  Train models for each subreddit
gpt2.download_gpt2()
for subreddit in subreddits:
  gpt2.download_gpt2(model_name=subreddit)
  sess = gpt2.start_tf_sess()
  gpt2.finetune(sess,
                dataset=(subreddit + ".txt"),
                run_name=subreddit,
                steps=1000
                )
  gpt2.reset_session(sess)

gpt2.reset_session(sess)


reddit = praw.Reddit(
    client_id="SMoB8JGhtjXOPA",
    client_secret="QK7QAlrOrOl2SsnK7eQIH3vBKFs",
    password="Craven0",
    user_agent="fugmatoad",
    # validate_on_submit=True,
    username="fugmatoad"
)

# get rising posts for each subreddit
count = 0
askredditrising = reddit.subreddit("askreddit").rising()
politicsrising = reddit.subreddit("politics").rising()
ProgrammerHumorrising = reddit.subreddit("ProgrammerHumor").rising()
selfrising = reddit.subreddit("self").rising()

# loop to post every hour to each subreddit
while True:
  
  for subreddit in subreddits:
    index = 0
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,run_name=subreddit)
    if(subreddit == "askreddit"):
      print("on askreddit\n")
      for submission in askredditrising:
        if(index == count):
          index = 0
          break
        index = index + 1

    elif(subreddit == "politics"):
      print("on politics")
      for submission in politicsrising:
        if(index == count):
          index = 0
          break
        index = index + 1

    elif(subreddit == "ProgrammerHumor"):
      print("on programmerHumor")
      for submission in ProgrammerHumorrising:
        if(index == count):
          index = 0
          break
        index = index + 1

    elif(subreddit == "self"):
      print("on self")
      for submission in selfrising:
        if(index == count):
          index = 0
          break
        index = index + 1

    replyTo = "[TITLE]" + submission.title + "[TITLE]\n[start]" 
    print(replyTo)
    replies = gpt2.generate(sess,
                            length=(len(replyTo)+25),
                            temperature=1,
                            prefix=replyTo,
                            include_prefix=False,
                            truncate='[end]',
                            nsamples=5,
                            batch_size=5,
                            return_as_list=True,
                            run_name=subreddit
                            )

    for reply in replies:
        if ("[end]" and "[start]" and "[TITLE]") not in reply:
            submission.reply(reply)
            print("reply: " + reply + "\n")
            break

    gpt2.reset_session(sess)

  time.sleep(3600)
  count = count + 1

  print("iteration: " + count)
