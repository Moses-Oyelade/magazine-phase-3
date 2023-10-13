# from Author import Author




class Magazine:
    
    ALL = []
    
    def __init__(self, name="", category=""):
        self.name=name
        self.category=category
        Magazine.magazine_all(self)
        
        
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    
    def get_category(self):
        return self.category
    def set_category(self, category):
        self.category = category
    
    @classmethod
    def magazine_all(cls, magazine):
        cls.ALL.append(magazine)
        
    @classmethod
    def show_all_magazines(cls):
        print([{magazine.name: magazine.category}  for magazine in cls.ALL])
        
    def contributors(self):
        return self.name 
    
    @classmethod
    def find_by_name(cls, name):
        for name in cls.ALL:
            if cls.ALL.__contains__(name):
                return name.__dict__
            else:
                return"Not yet pulished"
    

    
    
    
    
    
magazine1 = Magazine("Mr. Bean", "Medical")
magazine2 = Magazine("Mr. Sean", "Banking")
magazine3 = Magazine("Mr. Hunter", "Research")
magazineA = Magazine("John Bosko", "Technology")

# magazine.name = "Colorado"
# magazine.category = "Medical"
# magazine1.name = "Kuda"
# magazine1.category = "Banking"
# magazine2.name = "Rice Technology"
# magazine2.category = "Research"

# print(magazine.get_name())

# print(magazine.magazine_all())
print(Magazine.show_all_magazines())

print(Magazine.find_by_name("Mr. Sean"))
