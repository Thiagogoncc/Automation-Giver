# Bem-vindo ao Script de Automação de Mensagens no WhatsApp!

## O que o Script Faz

Este script automatiza o envio de mensagens via WhatsApp usando o navegador Google Chrome e a interface da Giver. Ele navega até a página de administração da Giver, faz login, seleciona uma rotina no WhatsApp, e envia mensagens para os clientes listados. O processo é repetido indefinidamente, com intervalos aleatórios entre 30 e 240 segundos entre os ciclos.

## O Que Você Precisa Saber

### Pré-requisitos

1. **Instalação do Python**:
   - Certifique-se de que o Python está instalado na sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

2. **Instalação das Bibliotecas Necessárias**:
   - Abra o terminal ou prompt de comando e execute o seguinte comando para instalar a biblioteca necessária:
     ```sh
     pip install pyautogui
     ```
     - `pyautogui` é usado para automação de interação com a tela.

3. **Bibliotecas Padrão do Python**:
   - As seguintes bibliotecas são parte da biblioteca padrão do Python e não precisam ser instaladas separadamente:
     - `time` é usada para gerenciar os intervalos de espera no script.
     - `random` é usada para gerar intervalos de tempo aleatórios entre as execuções do script.
   - Estas bibliotecas são incluídas automaticamente na instalação do Python e podem ser usadas diretamente no script após a importação.

4. **Instalação do Google Chrome**:
   - Certifique-se de que o Google Chrome está instalado na sua máquina.

5. **Configuração do WhatsApp Web**:
   - O WhatsApp que enviará as mensagens precisa estar já conectado no WhatsApp Web. Não use o WhatsApp principal da loja para evitar riscos de banimento.

6. **Login na Giver**:
   - O login da loja deve estar salvo na página de login da Giver, pois o script só clicará em "Entrar".

7. **Configuração do Zoom da Tela**:
   - Certifique-se de que o zoom da tela está em 100%.

8. **Imagens de Referência**:
   - Cada monitor tem um contraste diferente, e o script reconhece imagens através de prints. É indicado que todas as imagens no arquivo sejam substituídas por prints tirados no próprio computador das mesmas imagens, sem trocar o nome dos arquivos. Se o script não clicar na imagem após a troca, diminua o nível de confiança no código (por exemplo, de "confidence=0.9" para um valor menor). Não deixe o número muito baixo para manter a confiabilidade.

9. **Intervalo entre Mensagens**:
   - O script espera entre 30 a 240 segundos para enviar a próxima mensagem. Para ajustar esse intervalo, edite a linha 281 no código:
     ```python
     random.randint(30, 240)
     ```
     - Substitua "30, 240" pelos valores desejados.

## Detalhes do Funcionamento do Script

### Início do Script
- O script abre o Google Chrome, navega para a página de administração da Giver, e entra no sistema.

### Envio de Mensagens
- O script clica na primeira pauta e no primeiro cliente que aparecer.
- Ele tenta localizar o ícone de envio de mensagem no WhatsApp no sistema Giver (existem duas variações de ícones e ele é inteligente para clicar em qualquer um que aparecer).
- Após localizar e clicar no ícone, ele aguarda 10 segundos para a abertura da tela de seleção de mensagens.
- O script seleciona a primeira mensagem disponível e a envia.

### Tentativas de Envio com Whatsapp Web Aberto
- O Script manda mensagem para o cliente direto.
- Se a imagem do ícone de envio não for encontrada, o script tentará novamente a cada 3 segundos. (Pode não ser encontrada quando o número do cliente é inválido)
- Se o envio falhar após três tentativas, a aba do WhatsApp será fechada e o script sempre clicrá em "concluído" em giver, para que apareça o próximo cliente.

### Ciclo e Looping
- O script repete o processo para cada cliente na rotina.
- Após completar uma rotina, o script espera um intervalo aleatório entre 30 a 240 segundos antes de iniciar o próximo ciclo.
- O script permanece em looping eterno, repetindo o envio de mensagens indefinidamente.

### Comportamento em Caso de Falha
- Se uma imagem específica não for encontrada, o script continuará tentando até que a imagem seja localizada e clicada.
- Para segurança e eficiência, ajustes no nível de confiança para reconhecimento de imagem podem ser necessários.
- Caso o script pare completamente (se a sua internet ficar latente ele irá parar, lembre-se que ele é um script que funciona através da internet entrando em sites como 
giver e whatsapp web e precisa tudo fluir normalmente) apenas coloque-o para rodar novamente.
