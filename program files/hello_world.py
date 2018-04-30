import string

greeting = "hello world"
greeting = string.capwords(greeting)
greeting += "!"

if __name__ == "__main__":
    print(greeting)
