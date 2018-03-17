# Podcast-Recommendation-System
Python libraries used:
- pandas,
- numpy,
- nltk


input and output files are located at ./private/

We have following input data:
1. episode_data.json: episodes with key and name
2. user_history.json: user with watching history 
3. social_network.json: users with their social network 

Scripts are,
1. collect_words.py:

input file(s) - episode_data.json

output file(s) - words.txt


2. word_keys.py

input file(s) - episode_data.json,words.txt

output file(s) - words_keys.txt


3. history.py

input file(s) - user_history.json

output file(s) - user_episodes.txt


4. user_social_recommendation.py

input file(s) - social_network.json,user_episodes.txt

output file(s) - user_social_recommendation.txt


5. generate_recommendation.py

input file(s) - user_social_recommendation.txt,words_keys.txt

input strings - user, watching_episode

user: user_id

watching_episode: watching episode

output= a set of recommendation based on given user and his/her watching episode

