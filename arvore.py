class No:
    def __init__(self, valor):
        self.valor = valor
        self.direita = None
        self.esquerda = None

    def set_direta(self, no):
        self.direta = no

    def set_esquerda(self, no):
        self.esquerda = no

    def get_direita(self):
        return self.direita

    def get_esquerda(self):
        return self.esquerda


# Binary Search Tree
class BST:
    def __init__(self):
        self.raiz = None

    def insert_node(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.insert_node(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.insert_node(no.direita, valor)

    def insert(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.insert_node(self.raiz, valor)

    def search_node(self, no, valor):
        if no.valor == valor:
            return True
        if valor < no.valor:
            if no.esquerda is None:
                return False
            else:
                return self.search_node(no.esquerda, valor)
        else:
            if no.direita is None:
                return False
            else:
                return self.search_node(no.direita, valor)

    def search(self, valor):
        if self.raiz is None:
            return False
        return self.search_node(self.raiz, valor)
    
    def minimo(self, no = None):
        if no == self.raiz:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.valor
    
    def maximo(self, no = None):
        if no == self.raiz:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no.valor

    def delete(self, valor, no = None):
        if no is None:
            no = self.raiz

        if no is None:
            return no
           
        if valor < no.valor:
            no.esquerda = self.delete(valor, no.esquerda)
        elif valor > no.valor:
            no.direita = self.delete(valor, no.direita)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda  
            else:
                substituto = self.minimo(no.direita)
                no.valor = substituto
                no.direita = self.delete(substituto, no.direita)
        return no