from Articles import Article
from Magazine import Magazine

class Author:
    def __init__(self, name=""):
        self.name=name
        self.Article = Article
        self.Magazine = Magazine
        Author.add_article(self)
        
        
    def get_name(self):
        # print("name inserted")
        return(self.name)
    def get_articles(self, author_name):
        author_name = self.name
        return[item for item in Article if author_name == item]

    def get_magazines(self, author_name):
        return [item for item in Magazine if author_name == item]

    @classmethod
    def add_article(self, magazine, title):
        print(f"This {Article} wit the title: {title} is inspired by {Author} in {magazine}")
        


author1 = Author("John Humphrey")
print(author1.get_name())