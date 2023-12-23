import requests
from bs4 import BeautifulSoup

from util.github_push import GithubPush


class MetadataParser:
    __opengraph_props = {'og:title', 'og:url', 'og:description', 'og:image', 'og:type', 'og:site_name', 'og:locale'}

    def get_metadatas(self, url: str) -> dict:
        soup = self.__create_soup(url)
        if soup is None:
            return {}
        return self.__convert_to_metadata(soup)

    def __create_soup(self, url: str) -> BeautifulSoup:
        try:
            r = requests.get(url=url)
            return BeautifulSoup(r.text, 'html.parser')
        except:
            # should change below print logic to logging logic
            print("failed to get response from url({}). so return empty metadata.".format(url))
            return None

    def __convert_to_metadata(self, soup: BeautifulSoup) -> dict:
        metadatas = {}
        for metadata in soup.find_all("meta"):
            property = metadata.get("property", None)
            if property is None:
                continue
            if property not in self.__opengraph_props:
                continue
            content = metadata.get("content", None)
            if content is None:
                continue
            props_name = property.split(":")[-1]
            metadatas[props_name] = content
        return metadatas

if __name__ == "__main__":
    url = "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"
    mp = MetadataParser()
    print(mp.get_metadatas(url))
