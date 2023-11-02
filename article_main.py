import metadata_parser as parser
import markdown

###
# {'2023년 10월 1일': ['http://bit.ly/45aU7oc',
#                   'https://www.youtube.com/watch?v=zp6nybNYjBQ&list=PLSCuU2a9seuO4xpzlC7dRjrVMhV6idD42',
#                   'https://youtu.be/zp6nybNYjBQ',
#                   'https://youtu.be/p_q4ECN33Yc',
#                   'https://youtu.be/uXS0kiJQMtw',
#                   'https://youtu.be/xf4kI_emeFo',
#                   'https://youtu.be/XsbKfvznouA',
#                   'https://youtu.be/nj2rVsu5n8w',
#                   'https://youtu.be/A2yOLycDuI4'],
#  '2023년 10월 4일': ['https://medium.com/@s4.ali/flutter-code-review-dos-and-don-ts-and-best-practices-1-5d003035953e'],
#  '2023년 10월 5일': ['https://www.youtube.com/playlist?list=PLSCuU2a9seuO4xpzlC7dRjrVMhV6idD42',
#                   'https://festa.io/events/4014',
#                   'https://janggiraffe.tistory.com/m/405',
#                   'https://n.news.naver.com/mnews/article/028/0002658981']}

###


def convert_to_markdown(json: dict):
    for key, value in json.items():
        if key == "title":
            result = markdown.markdown("#" + key)
            print(result)
        elif key == "url":
            result = markdown.markdown("##" + key)
            print(result)
        else:
            print(key,value)


url = "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"
mp = parser.MetadataParser()
print("start")
print(mp.get_metadatas(url))
print(convert_to_markdown(mp.get_metadatas(url)))

    # {'title': 'Flutter & Dart - The Complete Guide [2023 Edition]'
    # , 'url': 'https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/'
    # , 'description': 'A Complete Guide to the Flutter SDK & Flutter Framework for building native iOS and Android apps'
    # , 'image': 'https://img-c.udemycdn.com/course/480x270/1708340_7108_5.jpg'
    # , 'type': 'udemy_com:course'
    # , 'site_name': 'Udemy'
    # , 'locale': 'en_US'}



