episode_data_file=./private/"episode_data.json"
words_file=./private/"words.txt"
python ./src/collect_words.py collect_words episode_data_file,words_file

word_episode_file=./private/"words_keys.txt"
dictionary_file=./private/"words.txt"
python ./src/word_keys.py word_keys word_episode_file,dictionary_file

user_history_file=./private/"user_history.json"
user_episodes_file=./private/"user_episodes.txt"
python ./src/history.py user_history user_history_file,user_episodes_file



user_file=./private/"social_network.json"
user_watched_file=./private/"user_episodes.txt"
user_social_recommendation_file=./private/"user_social_recommendation.txt"
python ./src/user_social_recommendation.py user_social_recommendation user_fil$




