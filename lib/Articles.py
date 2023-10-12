# from Author import Author
# from Magazine import Magazine



class Article:
    
    all_articles = []
    
    def __init__(self, Author, Magazine, title =""):
        self.author=Author
        self.magazine=Magazine
        self.title=title
        Article.article_all(self)
        
    def get_author(self):
        return self.author
    
    def get_magazine(self):
        return self.magazine
    
    # def get_title(self):
    #     return self.title
    
    @classmethod
    def article_all(cls, article):
        cls.all_articles.append(article)
        
    @classmethod
    def show_all_articles(cls):
        print([article.title for article in cls.all_articles])
        

# article1 = Article(Magazine, Author, title="The situation now!")


# print(Author)
# print(Magazine)
# print(article1.article_all())