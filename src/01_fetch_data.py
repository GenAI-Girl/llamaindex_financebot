import os
import urllib.request as request

data_url = "https://github.com/GenAI-Girl/llamaindex_stocksbot/raw/main/articles.zip"

def download_file():

    filename, headers = request.urlretrieve(
        url = data_url,
        filename = "articles.zip"
    )
    

download_file()
os.system("unzip articles.zip")
os.system("rm -rf articles.zip")