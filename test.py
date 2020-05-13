
class Information:
    
    def __init__(self):
        self.name = "salman"
        self.__private_name = "Johnson"

    def get_private_name(self):
        return self.__private_name
        
    def set_private_name(self,new_Name):
        self.__private_name = new_Name
        self.__display()

    def __display(self):
        print("This method shouldn't be displayed by the instances")
 
info = Information()
info.set_private_name("Steve")



