class dictionary_parser:
    
    def __init__(self, a):
        self.a = a
        
    def key_provider(self):
        if self.notdict():
            return list(self.a.keys())
        
    def value_provider(self):
        if self.notdict():
            return list(self.a.values())
        
    def notdict(self):
        if type(self.a) != dict:
            raise Exception(self.a, " is not a dictionary")
        return 1
    
    def userinput(self):
        self.a = eval(input())
        print(self.a, " is of type",type(self.a))
        print(self.key_provider())
        print(self.value_provider())
      
    def insertion(self, key , value):
        self.a[key] = value
        return self.a