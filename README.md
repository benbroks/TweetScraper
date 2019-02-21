# Tweet Scraper

Using the twitterscraper tool to scrape the latest 500 tweets of U.S. Senators and other prominent politicans. Their tweets will serve as labelled partisan speech to train a supervised NLP classification model, which will eventually be able to classify the tweets of any twitter user (or any text block) given their handle as input.

Requires the twitterscraper and fasttext plugins. Run `pip install -r requirements.txt` to download them.

Run `python scraper.py` to generate the commands necessary to scrape twitter. Unfortunately, we can't run each command automatically, you will have to scrape each user's twitter individually by running the commands one at a time from `dCommands.txt` and `rCommands.txt`. Data will be saved within `data/d/` and `data/r/` - the full dataset will be posted in a .zip file once I have finished scraping myself.

How I trained the model -> this entails downloading [fasttext](https://github.com/facebookresearch/fastText/tree/master/python)'s github repo within the `data/` folder. Follow the instructions in their readme to install the necessary packages. Run `textClean.py` to create our supervised learning training and validation sets. Then, go to `data/fasttext/` and run `./fasttext supervised -input ../fullEdited/supervised.train -output ../../model/model -epoch 60`. You can fiddle around with the epoch number but pretty much anything above 50 will get us reasonably high accuracy. To get test accuracy, run `./fasttext test ../../model/model.bin ../fullyEdited/supervised.valid`. You should get a number just north of 99%.

Run `python predict.py TWITTERHANDLE` in the main directory to predict the political leaning of any public user on twitter.
