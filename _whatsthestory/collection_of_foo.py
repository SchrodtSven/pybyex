import functools

def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiouÄä')

vs = count_vowels('Ick bin ein Bärrliner!')

print(vs)

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

f = [fib(n) for n in range(16)]
print(f)