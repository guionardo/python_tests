import shutil, os, glob
'''
Programa para testar a integridade de unidade SD ou pendrive.

O programa cria arquivos até completar todo o espaço da unidade e depois lê todos os arquivos, identificando os erros
'''
class MSequencia:
        
        def __iter__(self):
                self.a = 32
                return self
        
        def __next__(self):
                if self.a<127:
                        self.a += 1
                else:
                        self.a = 32
                return self.a
        

class Arquivo:
        cache = {}

        def __init__(self, arquivo, tamanho = -1):
                self.arquivo = arquivo
                if (tamanho == -1):
                        if (os.path.exists(arquivo)):
                                tamanho = os.path.getsize(arquivo)
                        else:
                                tamanho = 1024

                self.tamanho = tamanho
                self.getCache(tamanho)                

        def getCache(self, tam):                
                if (not str(tam) in self.cache):
                        print("Criando cache de "+str(tam)+" bytes...",end='')                        
                        ms = MSequencia()
                        mi = iter(ms)
                        lista = []
                        for i in range(tam):
                                lista.append(str(chr(next(mi))))                                
                        self.cache[str(tam)] = ''.join(lista)
                        print(" => Cache criado")
                return self.cache[str(tam)]

        def Criar(self):
                f = open(self.arquivo,'w')
                ms = MSequencia()
                mi = iter(ms)
                n = 0
                print("Criando "+self.arquivo+" com "+str(self.tamanho)+" bytes...", end='')
                with open(self.arquivo,"w") as f:
                        f.write(self.cache[str(self.tamanho)])
                        f.close()                

                f.close()
                print(" => Arquivo criado")

        def Testar(self):               
                print("Verificando integridade: "+self.arquivo, end='')
                # Abrir diretamente
                nerros = 0
                with open(self.arquivo, "r") as f:
                        s = f.read()
                        if s!=self.cache[str(self.tamanho)]:
                                i=0
                                for cf in s:                                        
                                        cc = self.cache[str(self.tamanho)][i:i+1]
                                        i+=1
                                        if cf!=cc:
                                                if nerros==0:
                                                        print('')
                                                print("           ERRO: Byte inesperado na posição #"+str(i)+" : Esperado = "+cc+" / Encontrado = "+cf)
                                                nerros+=1
                                return False
                                        
                print(" => OK")
                return True

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield os.path.join(path, file)

free = shutil.disk_usage('G:\\')
tpadrao = 1024*1024
narquivo = 0
arquivos = []

arquivos = files('G:\\')

'''        
while (free.free>0):
        tam = tpadrao if free.free > tpadrao else free.free
        narquivo += 1
        sarquivo = 'G:\\'+(str(hex(narquivo))[2:]).rjust(8,'0')
        a = Arquivo(sarquivo,tam)
        a.Criar()
        arquivos.append(sarquivo)
        free = shutil.disk_usage('G:\\')
'''
print("*** Iniciando testes")
nok = 0
nerros = 0
aerros = []
for arquivo in arquivos:
        a = Arquivo(arquivo)
        if a.Testar():
                nok+=1
        else:
                nerros+=1
                aerros.append(arquivo)

print("Arquivos OK = "+str(nok))
print("Arquivos com erro = "+str(nerros))
if nerros>0:
        print(aerros)