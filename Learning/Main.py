import sys

def main():
    print("Hello World")
    cycle(10)

def cycle(counter):
    if counter == 0:
        return
    print(counter)
    cycle(counter-1)

if __name__ == '__main__':
    main()
