class DataNotFoundException(Exception):
    def __init__(self, param: str, message: str = "Data not found"):
        self.param = param
        self.message = message
        super().__init__(self.message)
