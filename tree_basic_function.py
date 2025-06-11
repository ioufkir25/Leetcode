def sommmevaleurs(T:TreeNode):
    if T == None:
        return 0
    return T.val + sommmevaleurs(T.left) +sommmevaleurs(T.right)


def min_valeur(T: TreeNode):
    if T is None:
        return float('+inf')  
    
    return min(T.val, min_valeur(T.left), min_valeur(T.right))

def max_valeur(T:TreeNode):
    if T is None:
        return float('-inf')  
    
    return max(T.val, max_valeur(T.left), max_valeur(T.right))

def search(T:TreeNode,n:int):
    
    if T is None :
        return False
    
    if T.val == n:
        return True 
    
    return search(T.left,n) or search(T.right,n)


print(search(T1,-10))