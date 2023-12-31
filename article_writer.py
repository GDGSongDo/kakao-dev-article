import os

class ArticleWriter:
    __article_format = """## [{title}]({url})<br>
![Course Image]({image})<br>
**Description:** {description}<br>
**Type:** {course_type}<br>
**Site Name:** {site_name}<br>
**Locale:** {locale}"""

    def __init__(self, directory: str, filename: str):
        self.__directory = directory
        self.__filename = filename
    
    def write(self, data: dict):
        try:
            if not os.path.exists(self.__directory):
                os.makedirs(self.__directory)
        except OSError:
            print("Error: Failed to create the directory during writing articles.")
        
        with open(os.path.join(self.__directory, self.__filename), 'w', encoding='utf-8') as file:
            article_text = self.__article_format.format(
                title=data['title'], 
                url=data['url'], 
                image=data['image'], 
                description=data['description'], 
                course_type=data['type'], 
                site_name=data['site_name'], 
                locale=data['locale'])
            file.write(article_text)

if __name__ == "__main__":
    sample_data = {'title': 'Test Title', 'url': 'https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/', 'description': 'This is test description', 'image': 'https://img-c.udemycdn.com/course/480x270/1708340_7108_5.jpg', 'type': 'udemy_com:course', 'site_name': 'Udemy', 'locale': 'en_US'}
    writer = ArticleWriter("./test", "test_output.md")
    writer.write(sample_data)
