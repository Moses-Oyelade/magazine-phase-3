# from Author import Author




class Magazine:
    
    ALL = []
    
    def __init__(self, name: str, category: str):
        self.name=name
        self.category=category
        # Magazine.magazine_all(self)
        Magazine.ALL.append(self)
        
        
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    
    def get_category(self):
        return self.category
    def set_category(self, category):
        self.category = category
    
    # @classmethod
    # def magazine_all(cls, magazine):
    #     cls.ALL.append(magazine)
        
    def __repr__(self):
        return f"('{self.name}': '{self.category})"
    
    # @classmethod
    # def show_all_magazines(cls):
    #     print([{magazine.name: magazine.category}  for magazine in cls.ALL])
        
    # def contributors(self):
    #     return self.name 
    
    @classmethod
    def find_by_name(cls, name):
        for dict in cls.ALL:
            for name in dict:
                print({name}) 
                
            print("")
        
        # print ((
        #     (name for name in cls.ALL if name == cls.ALL.__contains__(name))
                
        # ))
    @classmethod
    def article_titles(cls):
        # return []
        pass
    
    # def contributing__authors():
        

    
    
    
    
    
magazine1 = Magazine("The Bean", "Medical")
magazine2 = Magazine("The Sean", "Banking")
magazine3 = Magazine("The Hunter", "Research")
magazineA = Magazine("Python", "Technology")

# magazine.name = "Colorado"
# magazine.category = "Medical"
# magazine1.name = "Kuda"
# magazine1.category = "Banking"
# magazine2.name = "Rice Technology"
# magazine2.category = "Research"

print(magazine1.get_name())
print(magazine2.get_category())
print(Magazine.ALL)
# print(Magazine.show_all_magazines())

# print(Magazine.find_by_name("Mr. Hunter"))
