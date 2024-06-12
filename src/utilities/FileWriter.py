class FileWriter:
    @staticmethod
    def write_links_to_file(filename, links):
        try:
            with open(filename, "w", encoding='utf-8') as file:
                for link in links:
                    file.write(link + '\n')
            return True
        except Exception as e:
            print("There was an error trying to write your links to file.")
            print(e)
            return False
