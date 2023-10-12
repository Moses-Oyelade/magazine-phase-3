# from Author import Author




class Magazine:
    
    all = []
    
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
        cls.all.append(magazine)
        
    @classmethod
    def show_all_magazines(cls):
        print([{magazine.name: magazine.category}  for magazine in cls.all ])
        
    def contributors(self):
        return self.name 
    
    
magazine1 = Magazine("Mr. Bean", "Medical")
magazine2 = Magazine("Mr. Sean", "Banking")
magazine3 = Magazine("Mr. Hunter", "Research")



# magazine.name = "Colorado"
# magazine.category = "Medical"
# magazine1.name = "Kuda"
# magazine1.category = "Banking"
# magazine2.name = "Rice Technology"
# magazine2.category = "Research"

# print(magazine.get_name())
# print(magazine.get_category())
# print(magazine.magazine_all())
Magazine.show_all_magazines()
