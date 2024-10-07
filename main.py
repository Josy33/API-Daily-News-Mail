import requests
from send_email import send_email

topic = "tesla"

api_key = "92396e6562b4436eb3f1184c726e084a"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=92396e6562b4436eb3f1184c726e084a" \
      "&language=en"


# Make a request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

# Access the article titles and description
body = "Subject: Today's news\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
               + (article["description"] or "") + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)



