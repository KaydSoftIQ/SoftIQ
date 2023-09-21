class DataTable:

    def __init__(self):
        self.data = {}
        

    def insert_data(self, name, **kwargs):
        self.data[name] = kwargs
        self.data[name]["Name"] = name

        

test = DataTable()
test.insert_data("Joao", Age=16, County="London")
print(test.data)