#Tweet Scraper

Using the twitterscraper tool to scrape the latest 500 tweets of U.S. Senators and other prominent politicans. Their tweets will serve as labelled partisan speech to train a supervised NLP classification model, which will eventually be able to classify the tweets of any twitter user (or any text block) given their handle as input.

Requires the twitterscraper and fasttext plugins. Run `pip install -r requirements.txt` to download them.

Run `python scraper.py` to generate the commands necessary to scrape twitter. Unfortunately, we can't run each command automatically, you will have to scrape each user's twitter individually by running the commands one at a time from `dCommands.txt` and `rCommands.txt`. Data will be saved within `data/d/` and `data/r/` - the full dataset will be posted in a .zip file once I have finished scraping myself.

