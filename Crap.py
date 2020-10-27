import praw
import os
import transformers # transformers library
import torch # PyTorch, we are using PyTorch as our library

# We are going to load in GPT-2 using the transformers library
gpt_tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2-large')
# Loading in model now...
gpt_model = transformers.GPT2LMHeadModel.from_pretrained('gpt2-large')
# Takes a while to run...



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    def gen_text(prompt_text, tokenizer, model, n_seqs=1, max_length=25):
        # n_seqs is the number of sentences to generate
        # max_length is the maximum length of the sentence
        encoded_prompt = tokenizer.encode(prompt_text, add_special_tokens=False, return_tensors="pt")
        # We are encoding the text using the gpt tokenizer. The return tensors are of type "pt"
        # since we are using PyTorch, not tensorflow
        output_sequences = model.generate(
            input_ids=encoded_prompt,
            max_length=max_length + len(encoded_prompt),  # The model has to generate something,
            # so we add the length of the original sequence to max_length
            temperature=1.0,
            top_k=0,
            top_p=0.9,
            repetition_penalty=1.2,  # To ensure that we dont get repeated phrases
            do_sample=True,
            num_return_sequences=n_seqs
        )  # We feed the encoded input into the model.
        ## Getting the output ##
        if len(output_sequences.shape) > 2:
            output_sequences.squeeze_()  # the _ indicates that the operation will be done in-place
        generated_sequences = []
        for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
            generated_sequence = generated_sequence.tolist()
            text = tokenizer.decode(generated_sequence)
            total_sequence = (
                    prompt_text + text[len(tokenizer.decode(encoded_prompt[0], clean_up_tokenization_spaces=True, )):]
            )
            generated_sequences.append(total_sequence)
        return generated_sequences


    # Create the Reddit instance and log in
    reddit = praw.Reddit('RedditBot')

    # reddit.login(REDDIT_USERNAME, REDDIT_PASS)

    # Create a list
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    # Or load the list of posts we have replied to
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    # Pull the hottest 10 entries from a subreddit of your choosing
    subreddit = reddit.subreddit('books')
    for submission in subreddit.hot(limit=10):
        # print(submission.title)

        # Make sure you didn't already reply to this post
        if submission.id not in posts_replied_to:
            print("Bot replying to : ", submission.title)
            print("Post text : ", submission.selftext)
            print("Post Reply: ",gen_text(submission.selftext,gpt_tokenizer,gpt_model,max_length=len(submission.selftext) + 100))

            # Store id in list
            # posts_replied_to.append(submission.id)

    # Write updated list to file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

    # a = gen_text("Legolas and Gimli advanced on the orcs, raising their weapons with a harrowing war cry",gpt_tokenizer,gpt_model)
    #
    # # Sequence length was too small, lets increase it
    # b = gen_text("Legolas and Gimli advanced on the orcs, raising their weapons with a harrowing war cry",
    #      gpt_tokenizer,
    #      gpt_model,
    #      max_length=100)
    # # Will take some time......
    #
    # c = gen_text("Legolas and Gimli advanced on the orcs, raising their weapons with a harrowing war cry",
    #      gpt_tokenizer,
    #      gpt_model,
    #      max_length=40,
    #      n_seqs=3) # Will take even longer....
    d = gen_text("Legolas and Gimli advanced on the orcs, raising their weapons with a harrowing war cry",
                 gpt_tokenizer,
                 gpt_model,
                 max_length=40,
                 n_seqs=3)  # Will take even longer....
    # print(a)
    # print(b)
    print(d)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
