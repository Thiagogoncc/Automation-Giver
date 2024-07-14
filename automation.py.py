# Importação para clicks a partir de imagem ou coordenadas do mouse
import pyautogui
# Importação da biblioteca de tempo para quando eu precisar que meu código espere
import time
# Importação da biblioteca de tempo randomico
import random

pyautogui.press('winleft')
time.sleep(2)
pyautogui.write('Google Chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://cli.giver.com.br/administrador')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('f11')
time.sleep(5)

# 2. Entrar no sistema (assumindo que login/senha já estão salvos)

while True:
    img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Entrar-giver.png', confidence=0.4)
    if img is not None:
        pyautogui.click(img)
        break  # Sai do loop após clicar na imagem
 
 # 2.1 Se o script não encontrar o botão ele irá tentar clicar a cada 3 segundos até encontrar e conseguir clicar 
 
    else:
        print('Imagem para login não encontrada. Tentando novamente em 3 segundos...')
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente

# 3. Entrar no WhatsApp e escolher qual rotina irá mandar mensagem (sempre começará da primeira rotina e quando acabar ela irá ir para as próximas)
time.sleep(15)
while True:
    img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Capturar-icone-whatsapp.png', confidence=0.5)
    if img is not None:
        pyautogui.click(img)
        break  # Sai do loop após clicar na imagem
 
  # 3.1 Se o script não encontrar o botão ele irá tentar clicar a cada 3 segundos até encontrar e conseguir clicar 
 
    else:
        print('Imagem para login não encontrada. Tentando novamente em 3 segundos...')
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente

# Espera 15 segundos para que o as rotinas carreguem após o clique
time.sleep(15)

# 5 Após carregamento das rotinas do WathsApp, clicar na primeira rotina e primeiro cliente para mandar mensagem (para que aconteça perfeitamente a tela precia estar com o zoom de 100%) 

pyautogui.click(x=1534, y=217)  # Click na primeira pauta que aparecer
time.sleep(2)
pyautogui.click(x=1532, y=276)  # Click no primeiro cliente que aparecer
time.sleep(10) # Esperar até o carregamento do cliente (Coloquei 10 segundos caso a internet não seja boa, este campo pode ser costumizável para mais ou para menos tempo de espera)


# 6. Enviar a mensagem no WhatsApp (existem duas variações, portanto duas fotos)
while True:
    img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Enviar-icone-whatsapp.png', confidence=0.7)
    img2 = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Enviar-icone-whatsapp-2.png', confidence=0.7)
    
    if img is not None:
        pyautogui.click(img)
        break  # Sai do loop após clicar na imagem
    elif img2 is not None:
        pyautogui.click(img2)
        break  # Sai do loop após clicar na imagem
    else:
        print('Imagem para mandar mensagem não encontrada. Tentando novamente em 3 segundos...')
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente

# Espera 10 segundos para garantir que abra a tela de selecionar a mensagem (será sempre selecionada a primeira mensagem)
time.sleep(10)

# 7  Selecionar mensagem/Enviar Whatsapp/Iniciar conversa/Mandar mensagem

while True: # Selecionar a mensagem
    img = pyautogui.locateCenterOnScreen(
        r'assets/Pyatogui-images/Selecionar-icone-whatsapp.png', confidence=0.5)
    if img:
        pyautogui.click(img)
        break  # Sai do loop se a imagem foi encontrada e clicada
    else:
        print('Imagem para mandar mensagem não encontrada. Tentando novamente em 3 segundos...')
    time.sleep(3)  # Espera 3 segundos antes de tentar novamente
time.sleep(5)

while True:  # Enviar WhatsApp
    img = pyautogui.locateCenterOnScreen(
        r'assets/Pyatogui-images/Enviar-mensagem-whatsapp.png', confidence=0.7)
    if img:
        pyautogui.click(img)
        break  # Sai do loop se a imagem foi encontrada e clicada
    else:
        print('Imagem para mandar mensagem não encontrada. Contactar Thiago Gabriel (11) 95393-0034. Tentando novamente em 3 segundos...')
    time.sleep(3)  # Espera 3 segundos antes de tentar novamente
time.sleep(5)

while True:  # Iniciar Conversa
    img = pyautogui.locateCenterOnScreen(
        r'assets/Pyatogui-images/Iniciar-conversa.png', confidence=0.7)
    if img:
        pyautogui.click(img)
        break  # Sai do loop se a imagem foi encontrada e clicada
    else:
        print('Imagem para iniciar conversa não encontrada. Contactar Thiago Gabriel (11) 95393-0034. Tentando novamente em 3 segundos...')
    time.sleep(3)  # Espera 3 segundos antes de tentar novamente
time.sleep(5)

while True: #Iniciar conversa
    img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Usar-whatsapp-web.png', confidence=0.4)
    if img:
        pyautogui.click(img)
        break  # Sai do loop se a imagem foi encontrada e clicada
    else:
        print('Imagem para usar o WhatsApp Web não encontrada. Contactar Thiago Gabriel (11) 95393-0034. Tentando novamente em 3 segundos...')
    time.sleep(3)  # Espera 3 segundos antes de tentar novamente
time.sleep(15)

#7.1 Tentar 3 vezes mandar a mensagem, caso o número for inválido após 3 tentativas o sistema irá fechar a aba e seguir com o ciclo

tentativas = 3  # Número de tentativas
intervalo = 3   # Intervalo entre tentativas (em segundos)

for tentativa in range(tentativas):
    try:
        img = pyautogui.locateCenterOnScreen(
            r'assets/Pyatogui-images/Mandar-mensagem.png', 
            confidence=0.9)
        if img:
            pyautogui.click(img)
            break  # Sai do loop se a imagem foi encontrada e clicada
    except Exception as e:
        print(f"Erro ao tentar localizar a imagem: {e}")
    if tentativa < tentativas - 1:
        print(f'Tentativa {tentativa + 1} falhou. Tentando novamente em {intervalo} segundos...')
        time.sleep(intervalo)
    else:
        print('Não foi possível localizar a imagem após 3 tentativas. Fechando a aba...')
time.sleep(10)

# 7.2 Sair da aba do WhatsApp/Sucesso no contato
pyautogui.hotkey('ctrl', 'w')
time.sleep(5)

# 8 Sucesso no contato (Todos os contatos clicarmos será colocado no sucesso do contato, mesmo se o número for inválido. Para que o script continue funcionando)

while True:
    img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Sucesso-no-Contato.png', confidence=0.7)
    
    if img:
        pyautogui.click(img)
        break  # Sai do loop se a imagem foi encontrada e clicada
    else:
        print('Imagem para mandar mensagem não encontrada. Tentando novamente em 3 segundos...')
    time.sleep(3)  # Espera 3 segundos antes de tentar novamente
time.sleep(15)

# 9 ----------------------------------------------------------LOOPING  O SCRIPT FICARÁ EM LOOPING MANDANDO PAUTAS GIVER------------------------------------------------


while True:

    # 6. Enviar a mensagem no WhatsApp (existem duas variações, portanto duas fotos)
    while True:
        img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Enviar-icone-whatsapp.png', confidence=0.7)
        img2 = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Enviar-icone-whatsapp-2.png', confidence=0.7)
        
        if img is not None:
            pyautogui.click(img)
            break  # Sai do loop após clicar na imagem
        elif img2 is not None:
            pyautogui.click(img2)
            break  # Sai do loop após clicar na imagem
        else:
            print('Imagem para mandar mensagem não encontrada. Tentando novamente em 3 segundos...')
            time.sleep(3)  # Espera 3 segundos antes de tentar novamente

    # Espera 10 segundos para garantir que abra a tela de selecionar a mensagem (será sempre selecionada a primeira mensagem)
    time.sleep(10)

    # 7  Selecionar mensagem/Enviar Whatsapp/Iniciar conversa/Mandar mensagem

    while True: # Selecionar a mensagem
        img = pyautogui.locateCenterOnScreen(
            r'assets/Pyatogui-images/Selecionar-icone-whatsapp.png', confidence=0.5)
        if img:
            pyautogui.click(img)
            break  # Sai do loop se a imagem foi encontrada e clicada
        else:
            print('Imagem para mandar mensagem não encontrada. Tentando novamente em 3 segundos...')
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    time.sleep(5)

    while True:  # Enviar WhatsApp
        img = pyautogui.locateCenterOnScreen(
            r'assets/Pyatogui-images/Enviar-mensagem-whatsapp.png', confidence=0.7)
        
        if img:
            pyautogui.click(img)
            break  # Sai do loop se a imagem foi encontrada e clicada
        else:
            print('Imagem para mandar mensagem não encontrada. Contactar Thiago Gabriel (11) 95393-0034. Tentando novamente em 3 segundos...')
        
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    time.sleep(5)

    while True:  # Iniciar Conversa
        img = pyautogui.locateCenterOnScreen(
            r'assets/Pyatogui-images/Iniciar-conversa.png', confidence=0.7)
        
        if img:
            pyautogui.click(img)
            break  # Sai do loop se a imagem foi encontrada e clicada
        else:
            print('Imagem para iniciar conversa não encontrada. Contactar Thiago Gabriel (11) 95393-0034. Tentando novamente em 3 segundos...')
        
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    time.sleep(5)

    while True: #Iniciar conversa
        img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Usar-whatsapp-web.png', confidence=0.4)
        
        if img:
            pyautogui.click(img)
            break  # Sai do loop se a imagem foi encontrada e clicada
        else:
            print('Imagem para usar o WhatsApp Web não encontrada. Contactar Thiago Gabriel (11) 95393-0034. Tentando novamente em 3 segundos...')
        
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    time.sleep(15)

    #7.1 Tentar 3 vezes mandar a mensagem, caso o número for inválido após 3 tentativas o sistema irá fechar a aba e seguir com o ciclo

    tentativas = 3  # Número de tentativas
    intervalo = 3   # Intervalo entre tentativas (em segundos)

    for tentativa in range(tentativas):
        try:
            img = pyautogui.locateCenterOnScreen(
                r'assets/Pyatogui-images/Mandar-mensagem.png', 
                confidence=0.9)
            if img:
                pyautogui.click(img)
                break  # Sai do loop se a imagem foi encontrada e clicada
        except Exception as e:
            print(f"Erro ao tentar localizar a imagem: {e}")

        if tentativa < tentativas - 1:
            print(f'Tentativa {tentativa + 1} falhou. Tentando novamente em {intervalo} segundos...')
            time.sleep(intervalo)
        else:
            print('Não foi possível localizar a imagem após 3 tentativas. Fechando a aba...')
    time.sleep(10)

    # 7.2 Sair da aba do WhatsApp/Sucesso no contato
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(5)

    # 8 Sucesso no contato (Todos os contatos clicarmos será colocado no sucesso do contato, mesmo se o número for inválido. Para que o script continue funcionando)

    while True:
        img = pyautogui.locateCenterOnScreen(r'assets/Pyatogui-images/Sucesso-no-Contato.png', confidence=0.7)
        
        if img:
            pyautogui.click(img)
            break  # Sai do loop se a imagem foi encontrada e clicada
        else:
            print('Imagem para mandar mensagem não encontrada. Tentando novamente em 3 segundos...')
        
        time.sleep(3)  # Espera 3 segundos antes de tentar novamente
    time.sleep(15)

    # Espera aleatória entre 30 e 240 (30 segundos a 4 minutos, altere da forma que preferir mas eu digo-te para que deixe assim para evitar banimento) segundos antes de reiniciar o loop
        
     # Espera aleatória entre 30 e 240 segundos antes de reiniciar o loop
    intervalo_espera = random.randint(30, 240)
    print("Esperando {} segundos antes de reiniciar o loop...".format(intervalo_espera))
    time.sleep(intervalo_espera)