#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined in hidden_4 module"""
    import hidden_4

    data = sorted(dir(hidden_4))
    for n in data:
        if n[:2] != "__":
            print(n)
