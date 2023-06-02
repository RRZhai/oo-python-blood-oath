class BloodOath:
    all = []
    def __init__(self, date, follower, cult):
        self.date = date
        self.follower = follower
        self.cult = cult
        type(self).all.append(self)
