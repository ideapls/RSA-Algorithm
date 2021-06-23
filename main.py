from numeroPrimo import GeradorNumeroPrimo
from gerarChaves import Chaves
from criptografia import Criptografia

p = GeradorNumeroPrimo()
numero_p = p.numero_primo
print('\n P :', str(numero_p))

q = GeradorNumeroPrimo()
numero_q = q.numero_primo
print('\n Q :', str(numero_q))

minhas_chaves = Chaves(numero_p, numero_q)
minhas_chaves.gerar_chaves()

mensagem = Criptografia()
mensagem_cifrada = mensagem.encripta_mensagem()
mensagem.decripta_mensagem(mensagem_cifrada)
