# from Author import Author
# from Magazine import Magazine

article_inst = []

class Article:
    def __init__(self, Author, Magazine, title =""):
        self.author=Author
        self.magazine=Magazine
        self.title=title
        
    def get_author(self):
        return self.author
    
    def get_magazine(self):
        return self.magazine
    
    def get_title(self):
        return self.title
    
    def article_all(self):
        return(f"The magazine list are: {article_inst}")

# article1 = Article(Magazine, Author, title="The situation now!")


# print(Author)
# print(Magazine)
# print(article1.article_all())