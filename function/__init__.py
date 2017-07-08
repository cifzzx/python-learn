import math



def is_sqr(x):
    print(math.sqrt(x))
    return math.sqrt(x).isdigit()

if __name__ == "__main__":

    print(filter(is_sqr,range(1,100)))