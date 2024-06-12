class LinkLoader:
    @staticmethod
    def load_links(file_name):
        unique_urls = set()
        try:
            with open(file_name, "r+", encoding='utf-8') as file:
                url_list = file.read().split('\n')
                for url in url_list:
                    unique_urls.add(url)
            return list(unique_urls)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return []
        except UnicodeDecodeError:
            print(f"Error: Unable to decode contents of '{file_name}'.")
            return []
