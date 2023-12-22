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


url = "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"
data = parser.MetadataParser().get_metadatas(url)

markdown_text = f"## [{data['title']}]({data['url']})\n\n"
markdown_text += f"![Course Image]({data['image']})\n\n"
markdown_text += f"**Description:** {data['description']}\n\n"
markdown_text += f"**Type:** {data['type']}\n\n"
markdown_text += f"**Site Name:** {data['site_name']}\n\n"
markdown_text += f"**Locale:** {data['locale']}"

print(markdown_text)

output = 'test_output.html'

try:
    with open(output, 'w', encoding='utf-8') as file:
        file.write(markdown_text)
except Exception as e:
    print(f"Error: {e}")

