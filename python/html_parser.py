import http
from pathlib import Path
from urllib.parse import urljoin, urlunparse
from urllib.request import urlopen, urlretrieve
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        if not hasattr(self, "result"):
            self.result = []
        for name, value in attrs:
            if name == "src":
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    data_set = set(x for x in parser.result)
    return data_set


def download_image(url, data):
    download_dir = Path("DOWNLOAD")
    download_dir.mkdir(exist_ok=True)

    parser = ImageParser()
    parser.feed(data)
    data_set = set(x for x in parser.result)
    for x in sorted(data_set):
        image_url = urljoin(url, x)
        basename = Path(image_url).name
        target_file = download_dir / basename
        print(target_file)
        print("Downloading...", image_url)
        urlretrieve(image_url, target_file)


def main1():
    url = "https://google.co.kr"
    with urlopen(url) as f:
        charset = f.headers.get_params("charset")[1][1]
        data = f.read().decode(charset)

    data_set = parse_image(data)
    print("\n>>>>>> Fatch Images from", url)
    print("\n".join(sorted(data_set)))


def main2():
    host = "www.google.co.kr"
    connection = http.client.HTTPConnection(host)

    connection.request("GET", "")
    response = connection.getresponse()

    charset = response.msg.get_param("charset")
    print("charset :", charset)
    data = response.read().decode(charset)
    connection.close()

    print("\n>>>>> Downloading...", host)
    url = urlunparse(("http", host, "", "", "", ""))
    download_image(url, data)


if __name__ == "__main__":
    main2()
