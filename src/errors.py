class Missing(exception):
    def __init__(self, msg: str):
        self.msg = msg

class Duplicate(exception):
    def __init__(self, msg: str):
        self.msg = msg