Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print (ola mundo)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print ("ola mundo")
ola mundo
>>> nome = "Udi"
>>> 
>>> print (nome)
Udi
>>> 
>>> profissao = "aluno"
>>> idade = 39
>>> altura = 1.70
>>> 
>>> print (profissao)
aluno
>>> print (idade)
39
>>> print (altura)
1.7
>>> 
>>> print (altura + idade + profissao)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (altura + idade + profissao)
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> 
>>> 
>>> print (altura,idade,profissao)
1.7 39 aluno
>>> 
>>> print (nome,altura,idade, profissao)
Udi 1.7 39 aluno
>>> 
>>> prit ("nome,idade,profissao")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    prit ("nome,idade,profissao")
NameError: name 'prit' is not defined. Did you mean: 'print'?
>>> 
>>> print ("nome,idade,profissao")
nome,idade,profissao
>>> 
>>> print ("ola udi")
ola udi
