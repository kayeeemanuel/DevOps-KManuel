# hello.py
def hello_function(feature=None):
    if feature:
        return feature
    return "Hello, World!"

if __name__ == "__main__":
    print(hello_function())