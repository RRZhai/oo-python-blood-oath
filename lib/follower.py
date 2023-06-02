from .bloodoath import BloodOath
from datetime import date
class Follower:
    all = []
    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        type(self).all.append(self)

    def cults(self):
        return [oath.cult for oath in BloodOath.all if oath.follower == self]
    
    def join_cult(self, cult):
        today = date.today()
        BloodOath(today, self, cult)

    def of_a_certain_age(self, age):
        return [follower for follower in type(self).all if follower.age >= age]
    
    def my_cults_slogans(self):
        return [oath.cult.slogan for oath in BloodOath.all if oath.follower == self]
    
    def most_active():
        all_oath = [oath.follower.name for oath in BloodOath.all]
        return max(set(all_oath), key = all_oath.count)
    
    def top_ten():
        all_oath = [oath.follower.name for oath in BloodOath.all]
        def sortBy(elem):
            return all_oath.count(elem)
        sorted = Follower.all.sort(key=sortBy)
        return sorted[:10]