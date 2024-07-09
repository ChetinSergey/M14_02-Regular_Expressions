import re


def extract_image_links(html_text):
    pattern = r'<img[^>]+?src\s*=\s*["\'](?P<url>(?:https?:\/\/)?' \
              r'(?:www\.)?example\.com\/(?:image\d+\.){1}[a-z]{3,4})["\']'
    links = re.findall(pattern, html_text)
    return links


sample_html = ("<img src='https://example.com/image1.jpeg'> "
               "<img src='http://example.com/image2.jpg'> "
               "<img src='http://example.com/image3.png'> "
               "<img src='https://example.com/image4.gif'>")


def print_result(img_links):
    if img_links:
        for url in img_links:
            print(url)
    else:
        print('Нет ссылок с картинками в HTML тексте.')


image_links = extract_image_links(sample_html)
print_result(image_links)
