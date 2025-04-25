# fuzzy_relations.py
from fuzzy_sets import union, intersection, complement, difference

def cartesian_relation(A: dict, B: dict) -> dict:
    # returns a dict mapping (x,y)->min(μA(x),μB(y))
    return {(x,y): min(A[x], B[y]) for x in A for y in B}

def max_min_compose(R: dict, S: dict) -> dict:
    # R: X×Y, S: Y×Z -> returns T: X×Z
    X = set(x for x,_ in R)
    Y = set(y for _,y in R)
    Z = set(z for _,z in S)
    T = {}
    for x in X:
        for z in Z:
            # max over y of min(R(x,y), S(y,z))
            vals = [min(R[(x,y)], S[(y,z)]) for y in Y if (y in [yy for yy, _ in S])]
            T[(x,z)] = max(vals) if vals else 0
    return T

if __name__ == "__main__":
    A = {"a":0.2,"b":0.8}
    B = {"x":0.5,"y":0.9}
    C = {"x":0.7,"y":0.4}

    R = cartesian_relation(A,B)
    S = cartesian_relation(B,C)
    print("Relation R (A×B):", R)
    print("Relation S (B×C):", S)
    print("Max–Min Composition R∘S:", max_min_compose(R,S))