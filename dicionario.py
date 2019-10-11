from time import sleep
while 1:
    try:
        nIndice = int(input('Digite o número da palavra que deseja pesquisar: '))
        print()
    except:
        print()
        print('ERRO: Digite um número!')
        print('')
        sleep(3) #Espera três segundos.
        for nContador in range(0, 70):
            print()
        continue

    if nIndice == 0:
        print('Você pesquisou: 3G/4G/5G.')
        print('O significado é:')
        print('É uma medição da potência do sinal, quanto maior melhor.')

    elif nIndice == 1:
        print('Você pesquisou: 404 ERROR.')
        print('O significado é:')
        print('É um erro que acontece quando é pesquisada uma página que não existe.')

    elif nIndice == 2:
        print('Você pesquisou: Adware.')
        print('O significado é:')
        print('São softwares gratuitos que usam anuncios com fonte de renda.')

    elif nIndice == 3:
        print('Você pesquisou: Afiliação.')
        print('O significado é:')
        print('Produtos de uma empresa que são vendidos por terceiros em seu website.')

    elif nIndice == 4:
        print('Você pesquisou: Avatar.')
        print('O significado é:')
        print('É um símbolo que representa o usuário.')

    elif nIndice == 5:
        print('Você pesquisou: Big Data.')
        print('O significado é:')
        print('É uma grande quantidade de dados.')

    elif nIndice == 6:
        print('Você pesquisou: Bing.')
        print('O significado é:')
        print('É uma plataforma de pesquisa da Microsoft.')

    elif nIndice == 7:
        print('Você pesquisou: BitTorrent.')
        print('O significado é:')
        print('É uma maneira de compartilhar arquivos entre usuários.')

    elif nIndice == 8:
        print('Você pesquisou: Blog.')
        print('O significado é:')
        print('É um site cuja estrutura permite a atualização rápida a partir de acréscimos dos chamados artigos, ou postagens ou publicações. ')

    elif nIndice == 9:
        print('Você pesquisou: Bot.')
        print('O significado é:')
        print('Abreviação de robô.')

    elif nIndice == 10:
        print('Você pesquisou: Banda Larga.')
        print('O significado é:')
        print('É o nome usado para definir qualquer conexão à internet acima da velocidade padrão dos modems (Aparelho que permite que um dispositivo eletrônico (p. ex., um computador) se comunique com outro ou outros por linha telefônica) analógicos.')

    elif nIndice == 11:
        print('Você pesquisou: Captcha.')
        print('O significado é:')
        print('É um teste de desafio cognitivo, utilizado como ferramenta anti-bot.')

    elif nIndice == 12:
        print('Você pesquisou: Nuvem.')
        print('O significado é:')
        print('É a possibilidade de acessar arquivos e executar diferentes tarefas pela internet, sem a necessidade de instalar aplicativos no computador.')

    elif nIndice == 13:
        print('Você pesquisou: Cloud Computing.')
        print('O significado é:')
        print('Refere-se à utilização da memória e das capacidades de armazenamento e cálculo de computadores e servidores compartilhados e interligados por meio da Internet.')

    elif nIndice == 14:
        print('Você pesquisou: Cookie.')
        print('O significado é:')
        print('É um pedaço de texto que um servidor Web pode armazenar no disco rígido do usuário. São utilizados pelos sites principalmente para identificar e armazenar informações sobre os visitantes.')

    elif nIndice == 15:
        print('Você pesquisou: Cyberbullying.')
        print('O significado é:')
        print('É um tipo de violência praticada contra alguém através da internet ou de outras tecnologias relacionadas.')

    elif nIndice == 16:
        print('Você pesquisou: Download.')
        print('O significado é:')
        print('É baixar um arquivo de um servidor remoto para um computador ')

    elif nIndice == 17:
        print('Você pesquisou: Email.')
        print('O significado é:')
        print('É um método que permite enviar e receber mensagens através de sistemas eletrônicos de comunicação.')

    elif nIndice == 18:
        print('Você pesquisou: Facebook.')
        print('O significado é:')
        print('É uma rede social de compartilhamento de fotos, vídeos ou textos sobre a sua vida.')

    elif nIndice == 19:
        print('Você pesquisou: Firewall.')
        print('O significado é:')
        print('É um dispositivo de uma rede de computadores que tem por objetivo aplicar segurança a um determinado ponto da rede.')

    elif nIndice == 20:
        print('Você pesquisou: Google.')
        print('O significado é:')
        print('É a plataforma de pesquisa mais utilizada atualmente.')

    elif nIndice == 21:
        print('Você pesquisou: Apple.')
        print('O significado é:')
        print('É uma empresa norte-americana que tem o objetivo de projetar e comercializar produtos eletrônicos de consumo, software de computador e computadores pessoais.')

    elif nIndice == 22:
        print('Você pesquisou: Microsoft.')
        print('O significado é:')
        print('É uma empresa americana que desenvolve, fabrica, licencia, apoia e vende softwares produtos eletrônicos, computadores e serviços pessoais.')
        
    elif nIndice == 23:
        print('Você pesquisou: Sony.')
        print('O significado é:')
        print('É uma empresa japonesa que fabrica uma infinidade de produtos eletrônicos.')

    elif nIndice == 24:
        print('Você pesquisou: Python.')
        print('O significado é:')
        print('É uma linguagem de programação ideal para iniciantes, fácil compreensão, mostra erros e o criador é Guido van Rossum.')

    elif nIndice == 25:
        print('Você pesquisou: Java.')
        print('O significado é:')
        print('É uma linguagem de programação, que está entre as mais famosas, muito moderna, muito utilizada em jogos e criada por James Gosling.')

    elif nIndice == 26:
        print('Você pesquisou: C/C++/C#.')
        print('O significado é:')
        print('É uma linguagem de programação, que está entre uma das mais populares, influenciou outras linguagens, criada por Dennis Ritchie e com atualizações C++ e C#.')

    elif nIndice == 27:
        print('Você pesquisou: JavaScript.')
        print('O significado é:')
        print('É uma linguagem de programação, sem relação com Java, com o mesmo nome pela fama, muito utilizada na interação com sites e criada por Brendan Eich.')

    elif nIndice == 28:
        print('Você pesquisou: Scratch.')
        print('O significado é:')
        print('É uma linguagem de programação, ideal para crianças iniciantes, utiliza blocos pré-montados, tem diversas línguas e foi criado pelo MIT.')

    elif nIndice == 29:
        print('Você pesquisou: iOS.')
        print('O significado é:')
        print('É um sistema operacional, criado pela Apple, intuitivo, só funciona em iPods, iphones e iPads anteriores ao iPad Air 2,atualizações anuais e feito em C, C++, Objective-C, Swift e Java.')

    elif nIndice == 30:
        print('Você pesquisou: iPadOS.')
        print('O significado é:')
        print('É um sistema operacional, criado pela Apple, intuitivo, e foi criado para atuar somente nos iPads mais recentes (a partindo iPad Air 2), também com atualizações anuais e feito em C, C++, Objective-C e Swift.')

    elif nIndice == 31:
        print('Você pesquisou: macOS.')
        print('O significado é:')
        print('É um sistema operacional, criado pela Apple, intuitivo, e utilizado somente em computadores da Apple, tendo atualizações anuais e feito em C, C++, Objective-C e Swift.')

    elif nIndice == 32:
        print('Você pesquisou: Linux.')
        print('O significado é:')
        print('É um sistema operacional, muito utilizado entre programadores, pois o código fonte pode ser usado, modificado e distribuído, com fins comerciais ou não, por qualquer um, mas respeitando as licenças e feito em C e Assembly.')

    elif nIndice == 33:
        print('Você pesquisou: Android.')
        print('O significado é:')
        print('É o sistema operacional, mais utilizado em dispositivos móveis, baseado em Linux, um dos mais otimizados para esse segmento de equipamentos móveis, feito em C, C++, PHP e Java.')

    elif nIndice == 34:
        print('Você pesquisou: Windows.')
        print('O significado é:')
        print('É o sistema operacional, mais utilizado, criado pela Microsoft, de fácil utilização, pacote Office: softwares, planilhas, documentos e apresentações entre outros... E feito em C, C++ e Assembly.')

    elif nIndice == 35:
        print('Você pesquisou: CPU.')
        print('O significado é:')
        print('''A unidade central de processamento ou CPU, também conhecida como processador, executa a entrada e saída de dados. O papel da CPU pode ser comparado ao papel de um cérebro no funcionamento de um computador. Isto é, realiza operações lógicas, cálculos e processamento de dados.
ATENÇÃO: Não confundir com gabinete.
        ''')

    elif nIndice == 36:
        print('Você pesquisou: Gabinete.')
        print('O significado é:')
        print('Caixa onde se localizam os componentes do computador.')

    elif nIndice == 37:
        print('Você pesquisou: GPU.')
        print('O significado é:')
        print('É um chip dedicado ao processamento de graficos/imagens.')

    elif nIndice == 38:
        print('Você pesquisou: Placa de video.')
        print('O significado é:')
        print('É uma placa especializada em graficos, contendo GPU.')

    elif nIndice == 39:
        print('Você pesquisou: Placa-mãe.')
        print('O significado é:')
        print('É a placa onde há a conexão entre todos os componentes.')

    elif nIndice == 40:
        print('Você pesquisou: Fonte.')
        print('O significado é:')
        print('É o equipamento que prove a energia dos componentes.')

    elif nIndice == 41:
        print('Você pesquisou: Cooler.')
        print('O significado é:')
        print('É o equipamento responsável por resfriar o computador e seus componentes.')

    elif nIndice == 42:
        print('Você pesquisou: HD.')
        print('O significado é:')
        print('É o equipamento responsável pelo armazenamento de dados, sendo ele pior que o SSD já que utiliza um disco optico.')

    elif nIndice == 43:
        print('Você pesquisou: SSD.')
        print('O significado é:')
        print('É o equipamento responsável pelo armazenamento de dados, mas ele é mais rapido que o HD já que usa um tecnologia similar aos cartões se memoria de celulares.')

    elif nIndice == 44:
        print('Você pesquisou: Software.')
        print('O significado é:')
        print('É a parte não material do computador, em que todos os comandos para ele estão armazenados.')

    elif nIndice == 45:
        print('Você pesquisou: Hardware.')
        print('O significado é:')
        print('É a parte física do computador, a qual segue os comandos do Software.')

    elif nIndice == 46:
        print('Você pesquisou: HTML.')
        print('O significado é:')
        print('É a tecnologia em que a base dos websites é feita.')

    elif nIndice == 47:
        print('Você pesquisou: HTTP.')
        print('O significado é:')
        print('É um protocolo para a troca de dados entre website e usuário.')

    elif nIndice == 48:
        print('Você pesquisou: HTTPS.')
        print('O significado é:')
        print('É um protocolo com a mesma função do HTTP, mas com uma maior segurança.')

    elif nIndice == 49:
        print('Você pesquisou: TI')
        print('O significado é:')
        print('É a sigla para tecnologia da informação. É o conjunto de atividades e soluções envolvendo hardware, software, banco de dados, e redes.')

    elif nIndice == 50:
        print('Você pesquisou: IP')
        print('O significado é:')
        print('É o endereço do usuário na internet, que nas mãos erradas possibilita a invasão do computador.')

    elif nIndice == 51:
        print('Você pesquisou: Instagram.')
        print('O significado é:')
        print('É uma rede social do mesmo dono do Facebook, que possui basicamente as mesmas funções, mas com apelo para os jovens.')

    elif nIndice == 52:
        print('Você pesquisou: Meme.')
        print('O significado é:')
        print('É um formato de informação, com um apelo engraçado.')

    elif nIndice == 53:
        print('Você pesquisou: Link.')
        print('O significado é:')
        print('É um atalho para outros websites, imagens, vídeos e/ou texto.')

    elif nIndice == 54:
        print('Você pesquisou: Dropbox.')
        print('O significado é:')
        print('É uma plataforma de armazenamento de dados.')

    elif nIndice == 55:
        print('Você pesquisou: Pinterest.')
        print('O significado é:')
        print('É uma rede social de compartilhamento de imagens.')

    elif nIndice == 56:
        print('Você pesquisou: PHP.')
        print('O significado é:')
        print('É uma linguagem de programação focada em servidores, mas com outras aplicações.')

    elif nIndice == 57:
        print('Você pesquisou: Spam.')
        print('O significado é:')
        print('São mensagens direcionadas a várias pessoas com o intuito de fazê-las comprar algo ou baixar um malware.')

    elif nIndice == 58:
        print('Você pesquisou: Mídia Social.')
        print('O significado é:')
        print('É uma plataforma para compartilhamento de dados, tambem conhecida como rede social.')

    elif nIndice == 59:
        print('Você pesquisou: Tag.')
        print('O significado é:')
        print('São palavras-chaves(relevantes) sobre algum assunto.')

    elif nIndice == 60:
        print('Você pesquisou: Twitter.')
        print('O significado é:')
        print('É uma rede social de compartilhamento de pequenos textos(tweets), que podem conter imagens ou vídeos.')

    elif nIndice == 61:
        print('Você pesquisou: Troll.')
        print('O significado é:')
        print('É uma gíria para enganar uma pessoa na internet.')

    elif nIndice == 62:
        print('Você pesquisou: Vlog.')
        print('O significado é:')
        print('É um vídeo do cotidiano de uma pessoa, tambem chamado de daily vlog quando é diario')

    elif nIndice == 63:
        print('Você pesquisou: URL.')
        print('O significado é:')
        print('É o localizador de um website na internet.')

    elif nIndice == 64:
        print('Você pesquisou: Website.')
        print('O significado é:')
        print('É um site na internet.')

    elif nIndice == 65:
        print('Você pesquisou: Wikipédia.')
        print('O significado é:')
        print('A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet.')

    elif nIndice == 66:
        print('Você pesquisou: WWW.')
        print('O significado é:')
        print('Significa "World Wide Web", que em português é a internet do mundo conectado.')

    elif nIndice == 67:
        print('Você pesquisou: Yahoo!.')
        print('O significado é:')
        print('É uma plataforma de pesquisa de uma ex-executiva da Google.')

    elif nIndice == 68:
        print('Você pesquisou: YouTube.')
        print('O significado é:')
        print('YouTube é uma plataforma de compartilhamento de vídeos.')

    elif nIndice == 69:
        print('Você pesquisou: Upload.')
        print('O significado é:')
        print('Mandar um arquivo para a internet.')

    elif nIndice == 70:
        print('Você pesquisou: Twitch.')
        print('O significado é:')
        print('É uma plataforma de compartilhamento de vídeos ao vivo.')

    elif nIndice == 71:
        print('Você pesquisou: Malware.')
        print('O significado é:')
        print('É um programa de computador destinado a infiltrar-se em um sistema de computador alheio e de forma ilícita, com o intuito de causar alguns danos.')

    elif nIndice == 72:
        print('Você pesquisou: Cache.')
        print('O significado é:')
        print('É uma memória que atua de forma mais rápida em um computador.')

    elif nIndice == 73:
        print('Você pesquisou: Firmware.')
        print('O significado é:')
        print('É uma parte específica de um software que fornece controle para um aparelho específico do dispositivo.')

    elif nIndice == 74:
        print('Você pesquisou: Samsung.')
        print('O significado é:')
        print('É uma corporação sul-coreana que atua em diversos ramos da área de tecnologia da informação.')

    elif nIndice == 75:
        print('Você pesquisou: Cracker/Crack.')
        print('O significado é:')
        print('É o termo usado para designar o indivíduo que pratica a quebra de um sistema de segurança de forma ilegal. E Crack é o nome da ação que ele pratica. ')

    elif nIndice == 76:
        print('Você pesquisou: Worms.')
        print('O significado é:')
        print('É um tipo de malware que é transmitido pela internet.')

    elif nIndice == 77:
        print('Você pesquisou: Cavalos de Tróia.')
        print('O significado é:')
        print('É um malware disfarçado de outro software.')

    elif nIndice == 78:
        print('Você pesquisou: Spywares.')
        print('O significado é:')
        print('É um malware de espionagem utilizado para roubar os dados do usuário.')

    elif nIndice == 79:
        print('Você pesquisou: Hacker/Hack.')
        print('O significado é:')
        print('É um indivíduo que se dedica, com intensidade incomum, a conhecer e modificar os aspectos mais internos de dispositivos, programas e redes de computadores. E Hack é o nome da ação que ele pratica.')

    elif nIndice == 80:
        print('Você pesquisou: Widget.')
        print('O significado é:')
        print('Um widget, numa interface gráfica, é um elemento de interação, tal como janelas, botões, menus, ícones, barras de rolagem, etc.')

    elif nIndice > 80:
        print()
        print('ERRO: Digite um número válido!')
        print('')
        sleep(3) #Espera três segundos.
        for nContador in range(0, 70):
            print()
        continue


    sleep(8) #Espera oito segundos.
    for nContador in range(0, 70):
        print()
        







'''
0 - 3G/4G/5G
1 - 404 ERROR
2 - Adware
3 - Afiliação
4 - Avatar
5 - Big Data
6 - Bing
7 - BitTorrent
8 - Blog
9 - Bot
10 - Banda Larga
11 - Captcha
12 - Nuvem
13 - Cloud Computing
14 - Cookie
15 - Cyberbullying
16 - Download
17 - Email
18 - Facebook
19 - Firewall
20 - Google
21 - Apple
22 - Microsoft
23 - Sony
24 - Python
25 - Java
26 - C/C++/C#
27 - JavaScript
28 - Scratch
29 - iOS
30 - iPadOS
31 - macOS
32 - Linux
33 - Android
34 - Windows
35 - CPU
36 - Gabinete
37 - GPU
38 - Placa de vídeo
39 - Placa-mãe
40 - Fonte
41 - Cooler
42 - HD
43 - SSD
44 - Software
45 - Hardware
46 - HTML
47 - HTTP
48 - HTTPS
49 - TI
50 - IP
51 - Instagram
52 - Meme
53 - Link
54 - Dropbox
55 - Pinterest
56 - PHP
57 - Spam
58 - Mídia Social
59 - Tag
60 - Twitter
61 - Troll
62 - Vlog
63 - URL
64 - Website
65 - Wikipédia
66 - WWW
67 - Yahoo!
68 - YouTube
69 - Upload
70 - Twitch
71 - Malware
72 - Cache
73 - Firmware
74 - Samsung
75 - Cracker/Crack
76 - Worms
77 - Cavalos de Tróia 
78 - Spywares
79 - Hacker/Hack
80 - Widget
'''

