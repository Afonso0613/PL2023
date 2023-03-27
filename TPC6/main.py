import ply.lex as lex


class MyLexer():
    estados=(
        ('comentario', 'exclusivo'),
    )

    tokens=(
        'FUNCTION', 
        'WHILE',
        'NOME',
        'INT',
        'FOR',
        'IN',
        'PROGRAM',
        'IF',
        'ELSE',
        'NUMERO',
        'COMENTARIO_START' #Inicio de um comentario de multiplas linhas
        'COMENTARIO_END' #Fim de um comentario de multiplas linhas
        'COMENTARIOS' #Conteudo dos comentarios
        'COMENTARIO_SINGLE' #Comentario de apenas uma linha
        'PO_E_VIR', # ;
        'VIR', # ,
        'E_CHAVE', #{
        'D_CHAVE', #}
        'E_PAREN', #(
        'D_PAREN', #)
        'E_PAREN_R', #[
        'D_PAREN_R', #]
        'IGUAL', #=
        'MAIS', #+
        'MENOS', #-
        'VEZES', # *
        'DIVIDIR', #/
        'MENOR', #<
        'MAIOR', #>
        'MAIOR_OU_I', # >=
        'MENOR_OU_I', #<=
        'EQUI',
        'DIFF',
        'PONTOS_TAMANHO' 
        )
    

def __init__ (self):
    self.lexer: lex.Lexer= lex.lex(module=self)

    self.parent=0
    self.chaveta=0
    self.par_reto=0

    self.palavras_reservadas={
        "function": "FUNCTION",
        "while" : "WHILE",
        "int" : "INT",
        "for" : "FOR",
        "in" : "IN",
        "program" : "PROGRAM",
        "if": "IF",
        "else" :"ELSE",
    }

t_ANY_ingnore= ' \t\n'

t_MENOR= r"\<" 
t_COMENTARIO_SINGLE= r"\/\/.*"
t_PO_E_VIR=r";"
t_VIR= r"\,"
t_COMENTARIO= r"[^(\/\*)]+"
t_PONTOS_TAMANHO= r"\.\."
t_NUMERO= r"\d+"
t_VEZES= r"\*"
t_DIVIDIR= r"\/"
t_MENOS= r"-"
t_MAIOR= r"\>"
t_IGUAL= r"\="


def t_E_PAREN_R(self, t):
    r"\["
    self.par_reto += 1
    return t

def t_D_PAREN_R(self, t):
    r"\]"
    if self.par_reto == 0:
            print("Unexpected ]")
            return t
    self.par_reto -= 1
    return t

def t_E_PAREN (self,t):
    r"\("
    self.parent+=1
    return t

def t_D_PAREN (self,t):
    r"\)"
    if self.parent==0:
         print ("Uexcpected )")
         return t
    self.parent -=1
    return t

def t_E_CHAVE (self,t):
    r"\{"
    self.chaveta+=1
    return t

def t_D_CHAVE (self,t):
    r"\}"
    if self.chaveta==0:
         print ("Uexcpected }")
         return t
    self.chaveta -=1
    return t

def t_COMENTARIO_START(self, t):
    r"\/\*"
    t.lexer.begin('comment')
    return t

def t_COMENTARIO_END(self, t):
    r"\*\/"
    t.lexer.begin('INITIAL')
    return t

def t_NOME(self, t):
    r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"
    t.type = self.palavras_reservadas.get(t.value, "NOME")
    return t

def t_ANY_error(self, t):
    print("Illegal character", t.value[0])
    t.lexer.skip(1)
    return t

def tokenize (self,data):
    self.lexer.input(data)

def main():
    if len(argv)==1:
        print ("Ficheiro não foi especificado")
        return

    file = argv[1]
    lexer = MyLexer()
    with open(file, "r") as file:
        lexer.tokenize(file.read())

    while tok := lexer.lexer.token():
        print(tok)

if __name__ == "__main__":
    main()