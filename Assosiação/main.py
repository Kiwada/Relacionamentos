from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Maquiavel')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()




escritor.ferramenta = caneta
escritor.ferramenta.escrever()


del escritor
print(caneta.marca)
maquina.escrever()
