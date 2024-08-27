""" https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true """

if __name__ == '__main__':
    s = input()
    
    #We check for any Character in S, if its alpha, a digit,etc
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))   
    print(any(char.isdigit() for char in s))   
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
