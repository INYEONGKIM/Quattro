class get_method_name_decorator:
    def __init__(self, fn):
        self.fn = fn

    def __set_name__(self, owner, name):
        owner.method_names.add(self.fn)
        setattr(owner, name, self.fn)
