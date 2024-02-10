import requests
import datetime as dt

# Company's data
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API Keys
news_api_key = '8dba7e4727ff4852b3f1f716dccf83ed'
stock_api_key = 'AZFKY1Q438T7ISRY'

# Relevant dates
yesterday = (dt.datetime.now() - dt.timedelta(1)).strftime('%Y-%m-%d')
before_yesterday = (dt.datetime.now() - dt.timedelta(2)).strftime('%Y-%m-%d')

# Parameters
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': stock_api_key
}

news_params = {
    'q': COMPANY_NAME,
    'from': yesterday,
    'apiKey': news_api_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]
yesterday_close_price = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])

# Get the day before yesterday's closing stock price
before_yesterday_close_price = float(stock_data['Time Series (Daily)'][before_yesterday]['4. close'])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
diff_stock_price = round(abs(yesterday_close_price - before_yesterday_close_price), 2)

# Work out the percentage difference in price between closing price yesterday and closing price the
# day before yesterday.
perc_diff_stock_price = diff_stock_price / before_yesterday_close_price

# If TODO4 percentage is greater than 5 then print("Get News").
if perc_diff_stock_price > 5:
    print('Get news')

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_response = requests.get(NEWS_ENDPOINT, params= news_params)
news_data = news_response.json()
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
top3_news = news_data['articles'][:2]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

