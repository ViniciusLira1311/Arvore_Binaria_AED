import sys

sys.path.append("..")

#importing
from arvore import BST


def test_vazio():
    lst = BST()
    assert lst.search(10) == False
    lst.insert(10)
    assert lst.search(10) == True
    assert lst.search(11) == False
    lst.insert(5)
    assert lst.search(5) == True
    assert lst.search(10) == True
    assert lst.search(11) == False
    lst.insert(15)
    assert lst.search(15) == True
    assert lst.search(11) == False


def test_remove_simple():
    lst = BST()
    lst.insert(10)
    lst.insert(5)
    lst.insert(15)
    lst.insert(3)
    lst.delete(15)
    assert lst.search(15) == False
    lst.delete(5)
    assert lst.search(5) == False
    assert lst.search(3) == True


def test_remove_completo():
    lst = BST()
    lst.insert(10)
    lst.insert(5)
    lst.insert(15)
    lst.insert(3)
    lst.delete(10)
    assert lst.search(10) == False
    assert lst.search(3) == True
    assert lst.search(5) == True
    assert lst.search(15) == True
