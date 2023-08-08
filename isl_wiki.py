import os
import bs4
import time
import random


class Article:
    def __init__(self, url="", max_length=512):
        self.url = url
        self.max_length = max_length
        self.read_file(url)
        self.links = self.extract_all_links()

    def read_file(self, file_path):
        self.title = ""
        self.summary = ""
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            self.soup = bs4.BeautifulSoup(text, "html.parser")
            title_tag = self.soup.find("h1")
            if title_tag:
                self.title = title_tag.text.strip()

            # first paragraph, usually the summary
            summary = self.soup.select("#bodyContent p")
            if summary:
                self.summary = "".join([p.text for p in summary])
                self.summary = self.summary.strip()

                if len(self.summary) > self.max_length:
                    self.summary = self.summary[: self.max_length]

    def extract_all_links(self):
        all_links = self.soup.find_all("a")
        links = []
        for link in all_links:
            if link.has_attr("href"):
                links.append(link["href"])
        return links


def filter_files(file_path):
    # Ignore special files
    if "~" in file_path:
        return False

    if file_path.endswith(".html"):
        return True
    else:
        return False


def list_files_and_folders_recursively(directory_path, max_files=10):
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    file_paths = []
    # Walk through the directory tree and list all files and folders
    print(f"Files and folders in '{directory_path}':")
    for root, dirs, files in os.walk(directory_path):
        if len(file_paths) == max_files:
            print(f"Found {max_files} files, stopping")
            break

        for file in files:
            file_path = os.path.join(root, file)
            if filter_files(file_path):
                print(f"Extracting File: {file_path}")

                article = Article(url=file_path)
                file_paths.append(article)

        for folder in dirs:
            folder_path = os.path.join(root, folder)
            # print(f"Folder: {folder_path}")

    return file_paths


def get_wikipedia_articles(max_articles=10, directory_path="./is/articles/"):
    articles = list_files_and_folders_recursively(
        directory_path, max_files=max_articles
    )
    # remove empty files, articles without summary (e.g. redirects)
    articles = [article for article in articles if article.summary]

    return articles


if __name__ == "__main__":
    directory_path = "./is/articles/"
    start = time.time()
    articles = list_files_and_folders_recursively(directory_path, max_files=100)
    end = time.time()
    # remove empty files, articles without summary (e.g. redirects)
    articles = [article for article in articles if article.summary]

    print("\n")
    print("-" * 20)
    print(f"Extracted {len(articles)} articles")
    print(f"Time elapsed: {int(end - start)}s")
    print("-" * 20)

    print("random article:", random.randrange(0, len(articles)))
    random_article = articles[random.randint(0, len(articles))]
    print(random_article.title)
    print(random_article.summary)
    print(random_article.url)

    # one hot encode the links
    all_links = []
    for article in articles:
        all_links.extend(article.links)

    all_links = list(set(all_links))
    print(f"Found {len(all_links)} unique links")
