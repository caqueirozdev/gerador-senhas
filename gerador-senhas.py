import random
import string
import pyperclip

def gerar_senha(tamanho=12, numeros=True, maiusculas=True, minusculas=True, especiais=True):
    caracteres = ""
    
    if numeros:
        caracteres += string.digits  # "0123456789"
    if maiusculas:
        caracteres += string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if minusculas:
        caracteres += string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    if especiais:
        caracteres += string.punctuation  # "!@#$%^&*()_+"

    if not caracteres:
        return "Erro: Nenhum tipo de caractere selecionado!"
    
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    pyperclip.copy(senha)  # Copia a senha gerada para a área de transferência
    return senha

# Interface simples para o usuário
print("Bem-vindo ao Gerador de Senhas Seguras!")
tamanho = int(input("Digite o tamanho da senha desejada: "))
num = input("Incluir números? (s/n): ").strip().lower() == "s"
mai = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
min = input("Incluir letras minúsculas? (s/n): ").strip().lower() == "s"
esp = input("Incluir caracteres especiais? (s/n): ").strip().lower() == "s"

senha_gerada = gerar_senha(tamanho, num, mai, min, esp)
print(f"\nSua senha gerada: {senha_gerada}")
print("A senha foi copiada para a área de transferência! ✅")
