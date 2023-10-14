class Round:
    def __init__(self, name):
        self.matchs = []
        self.name = name
        self.date_time_start = None
        self.date_time_end = None

    def __str__(self):
        output = ""
        for match in self.matchs:
            output += f"{match}\n"
        return output
    
    def __repr__(self):
        return str(self)
    
    def store_match(self, match):
        self.matchs.append(match)
