import argparse
import requests

from lxml import html


def parse(link: str) -> str:
    """Function for extracting path to element"""
    page = requests.get(link)
    root = html.fromstring(page.text)
    tree = root.getroottree()
    element_path = root.xpath("//div[@id='page-wrapper']//a[contains(@class,'btn-success') "
                              "or contains(@class, 'test-link-ok')]")
    for element in element_path:
        return tree.getpath(element)


def write_to_file(file_name: str, path: str) -> None:
    """Function for writing exctracted path to the file"""
    with open(f'{file_name}.txt', "w") as file:
        file.write(str(path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument("-l", "--link", help="Input link")
    parser.add_argument("-o", "--output", help="Output file")

    args = parser.parse_args()

    input_link = args.link
    output_file = args.output

    result = parse(str(input_link))
    write_to_file(output_file, result)
