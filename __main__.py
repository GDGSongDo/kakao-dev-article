import re
from urllib.parse import urlparse
from message_reader import MessageReader
from article_writer import ArticleWriter

def main():
    # read
    reader = MessageReader(".", "android_en.txt")
    messages = reader.get_messages()

    # write
    for msg in messages:
        text = msg['text']
        urls = re.findall(r'(https?://\S+)', text)
        print(urls)
        # todo
        # 1. validation
        #   1. urls empty check
        # 2. make directories by date
        # 3. get open graph data using MetadataParser
        # 4. write files in each directories using ArticleWriter

    # upload (git add, commit, push)


if __name__ == "__main__":
    main()

