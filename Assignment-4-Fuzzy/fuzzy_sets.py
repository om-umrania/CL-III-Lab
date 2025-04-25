# fuzzy_sets.py
def union(A: dict, B: dict) -> dict:
    return {x: max(A.get(x,0), B.get(x,0)) for x in set(A) | set(B)}

def intersection(A: dict, B: dict) -> dict:
    return {x: min(A.get(x,0), B.get(x,0)) for x in set(A) & set(B)}

def complement(A: dict) -> dict:
    return {x: 1 - mu for x, mu in A.items()}

def difference(A: dict, B: dict) -> dict:
    return {x: min(A.get(x,0), 1 - B.get(x,0)) for x in set(A) | set(B)}

if __name__ == "__main__":
    A = {"a":0.2,"b":0.3,"c":0.6,"d":0.6}
    B = {"a":0.9,"b":0.9,"c":0.4,"d":0.5}
    print("A:", A)
    print("B:", B)
    print("Union:", union(A,B))
    print("Intersection:", intersection(A,B))
    print("Complement of A:", complement(A))
    print("Difference A\\B:", difference(A,B))