#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for nom in dir(hidden_4):
        if nom[0] != '_' and nom[1] != '_':
            print(nom)
