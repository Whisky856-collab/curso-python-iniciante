"""
PROGRAMA DE ENSINO DE PYTHON PARA INICIANTES
Versão: 1.0
Autor: Fabricio
"""

def mostrar_bem_vindo():
    print("""
    **************************************
    *                                    *
    *  BEM-VINDO AO CURSO DE PYTHON!     *
    *                                    *
    *  Vamos aprender Python do zero!   *
    *                                    *
    **************************************
    """)

def explicar_o_que_e_python():
    print("\n--- O QUE É PYTHON? ---")
    print("""
Python é uma linguagem de programação poderosa e fácil de aprender.
É usada para:
- Desenvolvimento web (Django, Flask)
- Ciência de dados e Machine Learning
- Automação de tarefas
- Desenvolvimento de jogos
- E muito mais!

Por que aprender Python?
1. Sintaxe simples e legível
2. Grande comunidade de apoio
3. Muitas bibliotecas úteis
4. Alta demanda no mercado de trabalho
""")

def configurar_ambiente():
    print("\n--- CONFIGURANDO SEU AMBIENTE ---")
    print("""
Para começar a programar em Python, você precisa:
1. Instalar Python: https://www.python.org/downloads/
2. Escolher um editor de código (VS Code, PyCharm, ou IDLE que vem com Python)
3. Criar um arquivo com extensão .py (ex: meu_programa.py)

Você também pode usar ambientes online como:
- Replit (replit.com)
- Google Colab (colab.research.google.com)
""")

def ensinar_conceitos_basicos():
    print("\n--- CONCEITOS BÁSICOS ---")
    
    # Variáveis
    print("\nVARIÁVEIS:")
    print("""
Variáveis são como caixas que guardam informações.
Em Python, criamos variáveis assim:""")
    print("""
nome = "João"  # Texto (string)
idade = 25     # Número inteiro (int)
altura = 1.75  # Número decimal (float)
aprendendo = True  # Valor lógico (boolean)""")
    
    # Tipos de dados
    print("\nTIPOS DE DADOS PRINCIPAIS:")
    print("""
- str (texto): "Olá mundo", 'Python'
- int (inteiro): 10, -5, 0
- float (decimal): 3.14, -0.001
- bool (lógico): True, False""")
    
    # Operadores
    print("\nOPERADORES BÁSICOS:")
    print("""
+  Soma           (5 + 3 = 8)
-  Subtração      (10 - 4 = 6)
*  Multiplicação  (3 * 4 = 12)
/  Divisão        (10 / 2 = 5)
// Divisão inteira (10 // 3 = 3)
%  Módulo (resto) (10 % 3 = 1)
** Exponenciação  (2 ** 3 = 8)""")

def ensinar_estruturas_controle():
    print("\n--- ESTRUTURAS DE CONTROLE ---")
    
    # Condicionais
    print("\nIF/ELIF/ELSE:")
    print("""
if condição:
    # código se verdadeiro
elif outra_condição:
    # código se esta for verdadeira
else:
    # código se todas falsas""")
    
    print("\nExemplo prático:")
    print("""
idade = 18
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")""")
    
    # Loops
    print("\nLOOPS (FOR E WHILE):")
    print("""
# For loop (para cada item em uma sequência)
for i in range(5):  # Repete 5 vezes
    print(i)
    
# While loop (enquanto condição for verdadeira)
contador = 0
while contador < 5:
    print(contador)
    contador += 1""")

def ensinar_funcoes():
    print("\n--- FUNÇÕES ---")
    print("""
Funções são blocos de código reutilizáveis.
Elas ajudam a organizar seu programa.""")
    
    print("\nComo criar uma função:")
    print("""
def saudacao(nome):
    # Esta função recebe um nome e retorna uma saudação
    return f"Olá, {nome}!"
    
# Usando a função
mensagem = saudacao("Maria")
print(mensagem)  # Saída: Olá, Maria!""")

def ensinar_colecoes():
    print("\n--- COLEÇÕES DE DADOS ---")
    
    # Listas
    print("\nLISTAS:")
    print("""
# Listas guardam vários itens em ordem
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessa o primeiro item: maçã
frutas.append("uva")  # Adiciona um item
frutas.remove("banana")  # Remove um item""")
    
    # Dicionários
    print("\nDICIONÁRIOS:")
    print("""
# Dicionários guardam pares chave-valor
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "engenheiro"
}
print(pessoa["nome"])  # Acessa o valor pela chave""")

def mostrar_exemplo_completo():
    print("\n--- EXEMPLO COMPLETO ---")
    print("""
# Programa que calcula a média de notas
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Lista de notas
notas_aluno = [7.5, 8.0, 6.5, 9.0]

# Calcula e mostra a média
media = calcular_media(notas_aluno)
print(f"A média do aluno é: {media:.2f}")

# Verifica se foi aprovado
if media >= 7:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado.")""")

def mostrar_recursos_avancados():
    print("\n--- TÓPICOS PARA APRENDER DEPOIS ---")
    print("""
1. Trabalhando com arquivos
2. Tratamento de erros (try/except)
3. Programação Orientada a Objetos
4. Módulos e bibliotecas
5. Trabalhando com APIs
6. Pandas para análise de dados
7. Desenvolvimento web com Flask/Django""")

def mostrar_recursos_aprendizado():
    print("\n--- RECURSOS PARA CONTINUAR APRENDENDO ---")
    print("""
1. Documentação oficial: docs.python.org
2. Livro: 'Python Crash Course' (Eric Matthes)
3. Cursos online gratuitos:
   - Curso em Vídeo (Gustavo Guanabara)
   - Python for Everybody (Coursera)
4. Pratique em sites como:
   - Codewars
   - LeetCode (problemas iniciantes)
   - HackerRank""")

def main():
    mostrar_bem_vindo()
    
    while True:
        print("\nMENU PRINCIPAL:")
        print("1. O que é Python?")
        print("2. Configurar ambiente")
        print("3. Conceitos básicos")
        print("4. Estruturas de controle")
        print("5. Funções")
        print("6. Coleções de dados")
        print("7. Exemplo completo")
        print("8. Tópicos avançados")
        print("9. Recursos para continuar aprendendo")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção (0-9): ")
        
        if opcao == "0":
            print("\nObrigado por aprender Python comigo! Até a próxima!")
            break
        elif opcao == "1":
            explicar_o_que_e_python()
        elif opcao == "2":
            configurar_ambiente()
        elif opcao == "3":
            ensinar_conceitos_basicos()
        elif opcao == "4":
            ensinar_estruturas_controle()
        elif opcao == "5":
            ensinar_funcoes()
        elif opcao == "6":
            ensinar_colecoes()
        elif opcao == "7":
            mostrar_exemplo_completo()
        elif opcao == "8":
            mostrar_recursos_avancados()
        elif opcao == "9":
            mostrar_recursos_aprendizado()
        else:
            print("Opção inválida. Por favor, escolha um número de 0 a 9.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()