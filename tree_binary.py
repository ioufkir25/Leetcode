# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

T1 = TreeNode(1,
              TreeNode(3, TreeNode(4), TreeNode(5)),
              TreeNode(6, TreeNode(7), TreeNode(8)))

def isFeuille(T:TreeNode):
    if T.left == None and T.right == None :
        return True 
    return False


def taille(T:TreeNode):
    if  T == None :
        return 0
    
    return 1  + taille(T.left) + taille(T.right)

def hauteur(T:TreeNode):
    if  T == None :
        return 0
    return 1 + max( hauteur(T.left) , hauteur(T.right))


def compteurfeuille(T:TreeNode):
    if  T == None :
        return 0
    return compteurfeuille(T.left) +compteurfeuille(T.right)


print(compteurfeuille(T1))