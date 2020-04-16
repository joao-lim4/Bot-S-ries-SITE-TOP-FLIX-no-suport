from pynput.mouse import Button, Controller
from selenium import webdriver
import time
from PIL import Image,ImageGrab
import pytesseract  
import json
import webbrowser

"""     BOT SERIES TOP FLIX

    Desenvolvi esse bot para passar os episodios da serie que eu estava vendo, teste ele unicamente na serie manifesto que so contem 2 temporadas
    para configurar ele no seu pc basta instalar todas a bibliotecas e cnfigurar a posição do mouse e tambem a posição do screenShot.

    Feito isso insira a posição de cada episodio no arquivo json.
    O site tem um problema no scroll que acaba bugando o bot para resolver isso basta centralizar o maximo possivel de episodios na tela e alterar na 
    de voltar a pag.


"""

    
def extrate(nome): #Essa é a função que estrai o texto da imagem é verifica se tem uma guia de propaganda aberta e se tiver ela fecha.
    guia_aberta =  str(pytesseract.image_to_string(Image.open(nome)))
    if(guia_aberta != ""): #se na variavel guia aberta retorna algum texto quer dizer que o print tinha texto por tanto ele fecha a guia aberta.
        mouse = Controller()
        mouse.position = (470,17)#a posição do X onde fecha a guia 
        mouse.click(Button.left, 1)
        print('Uma guia de propaganda acabou de ser fechada!')
    else:
        print('Não tem nenhuma guia de propaganda aberta.')
        
def screen_shot(): #Essa é a função que tira o print e executa a função extrate no print tirado.
    time.sleep(4.0)
    img = ImageGrab.grab(bbox =(240,5,400,35)) #y  x  w  h  substituir os valores ate que o print seja tirado corretamente da guia.

    #img.show() Descomente essa função para não ter que abrir todas as imagens, ele ja abre automaticamente.

    img.save(r"C:\Users\cl4sh\OneDrive\Área de Trabalho\reprodutor\guia.jpg") # troque o diretorio para o diretorio que estiver no seu pc
    extrate('guia.jpg')

def reproduzir(): # Coloca o player em tela cheia e reproduz 
    mouse = Controller()
    mouse.position = (1327,784) # Localização do botão de tela cheia na minha tela, basta tirar um print da sua tela quando o player estiver aberto e abrir ele no paint para ver a localização do item na sua tela.
    mouse.click(Button.left, 1)
    time.sleep(1.0)
    print('Reprodutor colocado em tela cheia.')
    time.sleep(2.0)
    mouse.position = (20,1186) # Localização do potão player na minha tela, basta sustituir pela posição da sua tela.
    mouse.click(Button.left, 1)
    print('Video reproduzindo.')
    mouse.position = (1,1)

def voltar(): #Função minimiza o player e fecha ele basta tirar um print da tela, abrir no paint e substituir os valores.
    mouse = Controller()
    mouse.position = (1580,1184)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    print('Reprodutor minimizado.')
    time.sleep(3.0)
    mouse.position = (1347,153)
    mouse.click(Button.left, 1)
    time.sleep(3.0)
    screen_shot()
    print('Reprodutor fechado')
    screen_shot()

def voltar_pagina(): #Função do scroll, no meu pc ele bugava então para resolver toda vez que acabava um episodio essa função sobe toda o scroll e depois desce centralizando os episodios de novo.
    mouse = Controller()
    index = 1
    while index < 6:
        mouse.position = (1590,121) #Sobe todo o site.
        mouse.click(Button.left, 1)
        time.sleep(0.5)
        index += 1
   
    mouse.position = (1591,1150)#clica na setinha para descer e centralizar os episodios corretamente 
    mouse.click(Button.left, 20)#Clica 20 vezes por que no meu pc é a quantidade exata é so ver certinho no seu pc e mudar.



def ler_json():
    with open('json.json', 'r', encoding='utf-8') as file:
        return json.load(file)
   
def iniciar_player(eixoX,eixoY,episodio): #Recebe o episodio que você está e clica no episodio
    time.sleep(1)
    screen_shot()
    mouse = Controller()
    #mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = (eixoX,eixoY)
    mouse.click(Button.left, 1)
    time.sleep(2)
    screen_shot
    print('O episodio nº ' + str(episodio) + ' sera reproduzido.')
    time.sleep(3.0)

def request():
    webbrowser.open('https://topflix.tv/series/assistir-online-manifest-seriado/') #link da serie que eu estava assitindo, so substituir pelo link da sua série.

def pag_temporada(): #Essa função verifica se tem propaganda e fecha se tiver, ele clica na segunda temporada pra mim pois é a que eu estava assisindo.
    screen_shot()
    time.sleep(1.5)
    mouse = Controller()
    mouse.position = (771,674)
    mouse.click(Button.left, 1)
    screen_shot()
    mouse.position = (771,674) #Clica nos episodios.
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = (1341,816)#Fecha a primeira temporada.
    mouse.click(Button.left,1)
    time.sleep(1)
    mouse.position = (1342,878) # Abre a segunda temporada.
    mouse.click(Button.left, 1)
    time.sleep(1.5)
    mouse.position = (1591,1150) #Centaliza os episodios na tela.
    mouse.click(Button.left, 20)
        
    


def controller(): #Função Loop de episodios.
    episodios = [0] #O episodio que você está. Contador de episodios kkk.
    data = ler_json() # recebe o json com todo o conteudo de posição dos episodios.
    ep = [1] #O episodio que você está.
   
    while(episodios[0] < 13):
        eixoX = data[f'episodio{ep[0]}']['posicaoX']
        eixoY = data[f'episodio{ep[0]}']['posicaoY']
        iniciar_player(eixoX,eixoY,ep[0])
        time.sleep(2.5)
        time.sleep(30)
        reproduzir()
        time.sleep(2580) # tempo de 45 minutos que é o tempo em media do episodio da minha serie so substituir pelo tempo de cada episodio dura.
        voltar()
        voltar_pagina()
        ep[0] += 1  
        episodios[0] += 1

request()
time.sleep(6)
pag_temporada()
controller()
