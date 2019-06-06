import os, glob, cv2, shutil, numpy as np
from PIL import Image

path = input('Qual o caminho da pasta onde estão as fotos? ')
n_path = input('Qual o caminho da pasta para onde as fotos vão? ')

c = 0
w = [268, 676] # LARGURAS /// WIDHT
h = [268, 676] # ALTURAS /// HEIGHT

def list(path, c):

    if os.path.isdir(path):
        os.chdir(path)
        for file in glob.glob('*'):
            if os.path.isdir(path + file):
                list(path + file + '/')
            else:
                picture = cv2.imread(file)
                height = np.size(picture, 0)
                width = np.size(picture, 1)

                if height in h and width in w:
                    mo_path = path + '\\' + file
                    mn_path = n_path + '\\' + file
                    shutil.move(mo_path, mn_path)
                    c += 1
        print(c, end="")

    else:
        print (path)

list(path, c)
print(' ARQUIVO(S) MOVIDO(S)')
os.system('pause')

#------------------------ REFERÊNCIAS ------------------------#
# http://graciomar.com.br/blog/35/python-uma-funcao-recursiva-para-listar-arquivos-de-uma-pasta-e-das-subpastas
# http://blog.thedigitalcatonline.com/blog/2015/02/11/default-arguments-in-python
# http://www.php2python.com/wiki/function.getimagesize
# https://pt.stackoverflow.com/questions/146080/h%C3%A1-uma-maneira-de-imprimir-tudo-sem-a-quebra-de-linha
# https://pt.stackoverflow.com/questions/82733/como-concatenar-multiplas-strings-em-python
# https://pt.stackoverflow.com/questions/293096/python-movendo-arquivos-para-outra-pasta
# https://stackoverflow.com/questions/13033278/image-size-python-opencv/23207185
# https://gist.github.com/robsonpiere/fc256f6e7b7301d2d12343372cde93f9
