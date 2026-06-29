# WorldHello
This is a one year challenge I'm going to be embarking on where I will be completing one project every week. 

I hope you enjoy, some weeks will be alot easier than others but I want to push myself to create one new thing every week.  

#Week 4: 27th June
- Image Classifier:
  Wanted to actually train a model this week instead of just calling someone elses API. Used the Oxford-IIIT Pet dataset through fastai and started simple, cats vs dogs. The dataset filenames have a quirk where cats start with a capital letter and dogs are lowercase, so wrote a quick function off that, trained a ResNet34 for one epoch and somehow ended up at 0.8% error rate. Yeah that felt pretty good.

  Then levelled it up to full breed classification across 37 breeds. Used regex to pull the breed name out of the filenames, ran lr_find() to find a decent learning rate, fine tuned for 3 epochs and got it down to around 4.4% error rate. Also picked up that if valid_loss starts climbing while train_loss keeps falling you've gone too far and the model is just memorising at that point.

  Also tried scraping my own dataset for a forest vs bird classifier but gave up on that, the images were way too noisy and irrelevant to be useful so stuck with the ready made dataset.

  Ended the week by deploying the breed model to Hugging Face with a Gradio interface so its actually live and has an API too.

  Skills:
  - Python
  - fastai
  - Transfer learning
  - Regex
  - Gradio / Hugging Face

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
