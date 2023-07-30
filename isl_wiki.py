import os
import bs4
import time


class Article:
    def __init__(self, url=""):
        self.title, self.summary = self.read_file(url)
        self.url = url

    def read_file(self, file_path):
        title = ""
        summary = ""
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            soup = bs4.BeautifulSoup(text, "html.parser")
            title_tag = soup.find("h1")
            if title_tag:
                title = title_tag.text.strip()

            # first paragraph, usually the summary
            summary = soup.select("#bodyContent > p")
            if summary:
                summary = summary[0].text.strip()

        return title, summary


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
