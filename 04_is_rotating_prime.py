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
    c=0;
    r=0;
    for j in range(1,n):
        if n%j==0:
            c+=1;
    if c<2:
        r+=1;
    return r;


def is_rotating_prime(num):
    s=str(num);
    l=list(s);
    r=0;
    for i in range(len(l)):
        s=str();
        t=0;
        for j in range(1,len(l)+1):
            if j!=len(l):
                s=s+str(l[j]);
            else:
                s=s+str(l[0]);
        l=list(s);
        t=int(s);
        is_prime(t);
    if r==len(s):
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
