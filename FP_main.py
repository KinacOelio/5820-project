import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import gpt_2_simple as gpt2
import tensorflow
import requests

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')

replies = gpt2.generate(sess,
                        length=25,
                        temperature=1,
                        prefix="[TITLE]I am a turtle[TITLE]\n[start]",
                        include_prefix=False,
                        truncate='[end]',
                        nsamples=15,
                        batch_size=5,
                        return_as_list=True
                        )

for reply in replies:
    if ("[end]" and "[start]" and "[TITLE]") not in reply:
        print(reply + "\n")

print("complete.")