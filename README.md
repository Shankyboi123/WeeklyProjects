# WorldHello
This is a one year challenge I'm going to be embarking on where I will be completing one project every week. 

I hope you enjoy, some weeks will be alot easier than others but I want to push myself to create one new thing every week.  

#Week 4: 27th June
- Image Classifier:
  This week I started playing around with actual image classification instead of just using a ready-made API. The main notebook is a cat vs dog classifier using the Oxford-IIIT Pet dataset through fastai. I used the file names to label the images, built an `ImageDataLoaders` object, trained a ResNet34 vision learner, and tested predictions on sample images.

  Then I levelled it up with a cat and dog breed classifier. Instead of only checking whether the first letter of the filename was uppercase or lowercase, I used regex to pull the full breed name out of filenames like `Egyptian_Mau_167.jpg`. I built the dataloader with `ImageDataLoaders.from_name_re`, kept 20% of the data for validation, resized the images, used `lr_find()` to choose a learning rate, and fine-tuned a ResNet34 model for 3 epochs.

  I also started a second notebook for a forest vs bird classifier. That one is more of a data collection experiment right now: I first tried DuckDuckGo image search, then pivoted to using `icrawler` with Google Image Crawler to download bird and forest images into separate folders.

  Files:
  - `Image_Classifier/catvsdog.ipynb` - fastai cat vs dog classifier
  - `Image_Classifier/CatDogBreeds.ipynb` - fastai cat/dog breed classifier using regex labels
  - `Image_Classifier/forestvsbird.ipynb` - image scraping/data collection for bird vs forest classifier

  I gave up on the scrapping and data collection as it would produce to many irrelevant images so worked with the ready made cat and dog dataset. 

  Skills:
  - Python
  - fastai
  - Transfer learning
  - Image classification
  - Dataset loading and labelling
  - Regex
  - Learning rate tuning
  - Model validation
  - Web image scraping

#Week 3: June 22nd
- Stock Visualizer:
  Wanted to get into data after a couple of weeks of pure logic-building. Pulled real
  stock data and plotted price against trading volume on a dual-axis chart, then
  pushed further and compared % price change across multiple tickers (AAPL, TSLA, NVDA).

  Skills:
  - Python
  - pandas
  - matplotlib
  - Working with real-world data (yfinance)

#Week 2: June 15th 
- Bank Branch System:
  Exam prep got alittle piled up this week and ran short on time so felt like keeping it basic and hitting up the fundamentals again so did a little objet orientated programming :)

  Very Basic I had to build 4 classes:
  - BankAccount — the base account with deposit, withdraw, and balance
  - SavingsAccount — inherits from BankAccount, adds an apply_interest method
  - Customer — has a name and a list of accounts, can open new ones
  - Bank — manages all customers, can add/find customers and report total funds held

  Skills:
  - OOP
  - Python
  - HTML + CSS + JS

  EDIT:
  It felt alittle too basic so working on making it a web app 


#Week 1: June 8th  
- NSFW Detector - LMAO was tryna make a hotdog detector but no image classfication models were deployed on Hugging Face and this was the first avaliable one, I'm not a weirdo.

  Skills:
  - APIs
  - Python
  - HTML + CSS
  - JavaScript 
