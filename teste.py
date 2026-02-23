# Módulo de teste para o estudo do comando 'gh'

class Teste:
    
    def __init__(self):
        self._nome = "Astride"
    
    def qualidades(self):
        return f"A {self._nome} é linda!"
    

def main():
    t = Teste()
    s = t.qualidades()
    print(s)


if __name__ == "__main__":
    main()