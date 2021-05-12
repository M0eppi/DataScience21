class ListKeeper:
    global d
    d = {"example": [1,2,3,4,5]}

    # Functions
    # returns all list names (keys)
    def show():
        print(d.keys())
    
    # adding a new list into the dictionary
    def add(name,list):
        d_add = {name: list}
        d.update(d_add)
    
    # delets the list 'name'
    def delete(name):
        d.pop(name)
    
    # sorting the list 'name'
    def sort(name):
        k = d[name]
        k.sort()
        print(name + ':', k)
    
    # adds the new list to an existing list 'name'
    def append(name, list):
        v = d[name] + list
        # adds the new list into the dictionary
        ListKeeper.add(name,v)