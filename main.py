import requests
from send_email import send_email

api_key = "92396e6562b4436eb3f1184c726e084a"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-09-04&sortBy=publishedAt&apiKey=923" \
      "96e6562b4436eb3f1184c726e084a"

# Make a request
requests = requests.get(url)

# Get a dictionary with data
content = requests.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    title = article["title"]
    description = article["description"] or ""  # Ensures desciption is a string
    if title is not None:
        body += title + "\n" + description + 2 * "\n"
        # if article["title"] is not None:
        #   body = body + article["title"] + "n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)



