import sys
import gmpy2
import argparse

def xgcd(a, b):
    if b == 0:
        return 0,1,0

    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Update a,b
        a = b
        b = r
        #Update for next iteration
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    return  a, u0, v0

def rsa(c1, c2, n, a, b, gcd):
    if(a < 0):
    	# invert(c1, n) -> c1_invert: c1 * c1_invert = 1 mod n
    	c1_inv = gmpy2.invert(c1, n)
    	c1 = pow(c1_inv, -a , n)
    else:
    	# tercer numero es el mod
    	c1 = pow(c1, a, n)


    if(b < 0):
        # invert(c1, n) -> c1_invert: c1 * c1_invert = 1 mod n
        c2_inv = gmpy2.invert(c2, n)
        c2 = pow(c2_inv, -b , n)

    else:
        c2 = pow(c2, b, n)


    cp = c2*c1 % n
    # True si la raiz es exacta
    m = gmpy2.iroot(cp, gcd)
    h=hex(m[0])

    return h[2:].decode('hex')

def main():
    print("RSA CTF - From n, e1, e2, c1 and c2 to m\n")
    parser = argparse.ArgumentParser()
    parser.add_argument("e1", metavar='e1', type=int, nargs='+', help='e1 value')
    parser.add_argument("e2", metavar='e2', type=int, nargs='+', help='e1 value')
    parser.add_argument("n", metavar='n', type=int, nargs='+', help='e1 value')
    parser.add_argument("c1", metavar='c1', type=int, nargs='+', help='e1 value')
    parser.add_argument("c2", metavar='c2', type=int, nargs='+', help='e1 value')
    args = parser.parse_args()


    e1, e2, n, c1, c2 = args.e1[0], args.e2[0], args.n[0], args.c1[0], args.c2[0]
    gcd, a, b = xgcd(e1, e2)
    resultado = rsa(c1, c2, n, a, b, gcd)

    print("---------------------------------------------")
    print("RSA message:")
    print(resultado)
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
