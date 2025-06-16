class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# Création des feuilles
node2 = TreeNode(2, None, None)
node7 = TreeNode(7, None, None)
node20 = TreeNode(20, None, None)

# Création des nœuds intermédiaires
node5 = TreeNode(5, node2, node7)
node15 = TreeNode(15, None, node20)

T = TreeNode(10, node5, node15)

def taille(T:TreeNode):
    if T is None:
        return 0
    return 1+ taille(T.right)+taille(T.left)

def isfeuille(T:TreeNode):
    if  T.right is None and T.left is None:
        return True
    return False

def hauteur(T:TreeNode):
    if T is None:
        return 0
    return 1+max(hauteur(T.right),hauteur(T.left))

def number_feuille(T:TreeNode):
    if T is None:
        return 0
    if T.right is None and T.left is None:
        return 1
    return number_feuille(T.right)+number_feuille(T.left)
    
def somme_valeur(T:TreeNode):
    if T is None:
        return 0
    return T.val+somme_valeur(T.right)+somme_valeur(T.left)

def min_valeur(T:TreeNode):
    if T is None:
        return float("inf")
    return min(T.val, min_valeur(T.left), min_valeur(T.right))

def max_valeur(T:TreeNode):
    if T is None:
        return float("-inf")
    return max(T.val, max_valeur(T.left), max_valeur(T.right))

def find_value(T:TreeNode,n:int):
    if T is None:
        return False
    if T.val==n:
        return True
    return find_value(T.left,n) or find_value(T.right,n)
       
print(find_value(T,58))