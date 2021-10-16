from abc import ABC,abstractmethod

class Band(ABC):
    """
    Class Band made up of different kinds of musicians.

    type(name)=str
    type(members)=list

    """
    bands=[]
    def __init__(self,name="",members=[]):
        self.name=name 
        self.members=members
        Band.bands.append(self)

    
    def play_solos(self): 
        solo=[]
        if len(self.members) != 0:
            for i in self.members:
                solo.append(i.play_solo())
                return solo
            else: 
                return "There is no members in this Band" 
       

    def __str__ (self):
        return f"The Band Name is {self.name} , Members are : {self.members}" 
     
  
    def __repr__(self):
        return f"The Band Name is : {self.name} , Members are : {self.members}"  


    @classmethod
    def to_list(cls):
        """
        each time , a band is created will added here
        """ 
        return cls.bands         



class Musician(Band):
    """
    Base Class for each band member
    """
    def __init__(self,name="",instrument=""):
        self.name = name
        self.instrument = instrument
    @abstractmethod    
    def play_solo(self): 
        """
        method to make the band member play a solo on his instrument 
        """
        pass

     
    def __str__ (self): 
        return f"I am  : {self.name} , Plays : {self.instrument}"
  

    def __repr__(self):
        return f"I am  : {self.name} , Plays : {self.instrument}"

    @abstractmethod
    def get_instrument(self):
        """
        method returns what the band plays 
        """
        return self.instrument



class Guitarist(Musician):
    """
    inherit Class 
    """ 
    def get_instrument(self):  
        return "guitar"
    def play_solo(self):
        return "guit guit guit"
     
 
class Bassist(Musician):
    """
    inherit Class 
    """
    def get_instrument(self):  
        return "bass"
    def play_solo(self):
        return "bass bass bass"

class Drummer(Musician):
    """
    inherit Class 
    """
    def get_instrument(self):  
        return "drum"
    def play_solo(self):
        return "drum drum drum"

if __name__ == "__main__":
    x=Guitarist("dua")
    band=Band("DUA",[])
    print(band.play_solos())
