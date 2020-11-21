# -- coding: utf-8 --
import unittest

"""
Rotating primes
Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.
"""


# Implement the below function and run the program
def is_prime(n):   
    t=0;
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                t=1;
    if(t==0):
        return True;
    else:
        return False;


def is_rotating_prime(num):
    d=[int(x) for x in str(num)];
    c=[0];
    f=[];
    l=d[:];
    a=[];
    for i in  range(len(d)):
        c[0]=l.pop(len(d)-1);
        fin=c+l;
        l=fin[:];
        f.append(fin);
    for i in f:
        strings = [str(integer) for integer in i];
        a_string = "".join(strings);
        an_integer = int(a_string);
        a.append(an_integer);
    k=0;
    for i in a:
        if(is_prime(i)):
            k+=1;
    if(k==len(a)):
        return True;
    else:
        return False;


class TestIsRotatingPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(2), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(19), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(791), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(919), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
