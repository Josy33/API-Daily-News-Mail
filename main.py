import requests

api_key = "92396e6562b4436eb3f1184c726e084a"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-09-04&sortBy=publishedAt&apiKey=923" \
      "96e6562b4436eb3f1184c726e084a"

# Make a request
requests = requests.get(url)

# Get a dictionary with data
content = requests.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["tittle"])
    print(article["description"])




