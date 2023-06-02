from .bloodoath import BloodOath
from datetime import date
class Cult:
    all = []
    def __init__(self, name, location, founding_year, slogan):
        self.name, self.location, self.founding_year, self.slogan = name, location, founding_year, slogan
        type(self).all.append(self)

    def recruit_follower(self, follower):
        today = date.today()
        BloodOath(today, follower, self)
          
    def cult_population(self):
        return len([oath for oath in BloodOath.all if oath.cult == self])
    
    def find_by_name(name=''):
        for cult in BloodOath.all: 
            if cult.name == name:
                return cult
    
    def find_by_location(location=''):
        return [oath.cult for oath in BloodOath.all if oath.cult.location == location]
    
    def find_by_founding_year(year=0):
        return [oath.cult for oath in BloodOath.all if oath.cult.founding_year == year]
    
    def average_age(self):
        return sum(oath.follower.age for oath in BloodOath.all if oath.cult == self)/type(self).cult_population(self)
    
    def my_followers_mottos(self):
        return [oath.follower.life_motto for oath in BloodOath.all if oath.cult == self]
    
    def least_popular():
        min_join = float('inf')
        min_cult = None
        for cult in Cult.all:
            member = cult.cult_population()
            if member < min_join:
                min_join = member
                min_cult = cult
        return min_cult
    
    def most_common_location():
        locations = [oath.cult.location for oath in BloodOath.all]
        return max(set(locations), key=locations.count)