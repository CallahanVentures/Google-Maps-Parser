class QueryLoader:
    @staticmethod
    def load_queries():
        try:
            return open("queries.txt", "r+", encoding='utf-8').read().split("\n")
        except:
            return [input("There was an issue reading queries.txt\nEnter A Query To Search By, For Example 'Realtors in 30303':\n")]
