class Nodo:
    def __init__(self, id, nodosAdyacentes, distanciaNodosAdyacentes,tipoCable_NodosAdyacentes):
        self.id = id
        self.nodosAdyacentes = nodosAdyacentes
        self.distanciaNodosAdyacentes = distanciaNodosAdyacentes
        self.tipoCable_NodosAdyacentes = tipoCable_NodosAdyacentes
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, id, nodosAdyacentes, distanciaNodosAdyacentes,tipoCable_NodosAdyacentes):
        nuevo_nodo = Nodo(id, nodosAdyacentes, distanciaNodosAdyacentes,tipoCable_NodosAdyacentes)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.id,actual.distanciaNodosAdyacentes,actual.distanciaNodosAdyacentes,actual.tipoCable_NodosAdyacentes, end=" -> ")
            actual = actual.siguiente
        print("None")

# Crear una lista enlazada y agregar algunos elementos
lista = ListaEnlazada()
lista.agregar(1, [2, 3], [1500, 20000],["c","f"])
lista.agregar(2, [1, 3], [1500, 20000],["c","f"])
lista.agregar(3, [1, 2], [1500, 20000],["c","f"])

# Imprimir la lista enlazada
lista.imprimir()

# mover a la siguiente posición
