# Library Management
class Member:
    def __init__(self, name):
        self.name = name
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    #method
    def register_member(self, name):
        self.members.append(name)

    def get_active_members(self):
        active_members = []
        for member in self.members:
            if member.is_active:
                active_members.append(member)

        return active_members

