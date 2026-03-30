class Biblioteca:
    def __init__(self, paginas, autor):
        self.paginas = paginas
        self.autor = autor

class Livro:
    def __init__(self):
        self.livros = []
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
    def listar_livros(self, disponivel):
        self.disponivel = disponivel
        for livro in self.livros:
            print(f'{livro.paginas} Paginas - {livro.autor}')
            print(f'{"DISPONIVEL" if self.disponivel else "INDISPONIVEL"}')
    

   

pequeno_principe = Biblioteca (85, 'DanDan',)
a_marca_da_vitoria = Biblioteca (185, 'Phil Knight')
livro = Livro()
livro.adicionar_livro(pequeno_principe)
livro.adicionar_livro(a_marca_da_vitoria)
livro.listar_livros(pequeno_principe)

        
        
        

#conter: autor, livro, quantidade de paginas, se esta disponivel ou não para venda
#fazer igual o fabricamotor