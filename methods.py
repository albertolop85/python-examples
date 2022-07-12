def sum(x, y) :
    return x + y

def subs(x, y) :
    return x - y

def write(fpath, data) :
    with open(fpath, "w") as new_file :
        new_file.write(data)


class calculator :

    def sum(x, y) :
        return sum(x, y)