# app escreve codigo.14º projeto.linguagem utilizada Python

# criado por: Leonardo de Oliveira Prado
# Instagram: arduino2.0tecnologico

# Data de inicio do projeto 08/12/2023
# Data de término do projeto  08/12/2023

#************inclusão das bibliotecas
import flet
import pyautogui
import time
#************variável
TempoEspera = 2
#************app flet 
def main(pagina):
    pagina.title ="app escreve codigo"
    pagina.window_always_on_top = True  # nao fecha o app quando é clicado fora
    pagina.window_resizable = False  # nao abre janala grande
    pagina.window_width = 350  # dimensao app
    pagina.window_height = 450  # dimensao app
    pagina.bgcolor = "#69696969"  # cor de fundo (cinza escuro)
# ************faça isso se o botão "void setup(){" for clicado
    def voidsetup1(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("void setup(){")#escreve 
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def voidloop1(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("void loop(){")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def define(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("#define")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def include(eveto):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("#include < >")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def pinMode(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("pinMode( , );")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def digitalWrite (evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("digitalWrite( , );")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def  digitalRead(evento):
        time.sleep(TempoEspera)
        pyautogui.write("digitalRead( )")

    def analogRead(evento):
        time.sleep(TempoEspera)
        pyautogui.write(" analogRead( )")

    def delay(evento):
        time.sleep(TempoEspera)
        pyautogui.write("delay( );")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def if1(evento):
        time.sleep(TempoEspera)
        pyautogui.write(" if( ){")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def elseif(evento):
        time.sleep(TempoEspera)
        pyautogui.write(" else if( ){")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def else1(evento):
        time.sleep(TempoEspera)
        pyautogui.write(" }else{")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter


# **************intes que queremos na página com nomes e ********cores botao*******cores letra 
    voidsetup1= flet.ElevatedButton("void setup(){ ", bgcolor="#0000FF", color="#000000", on_click=voidsetup1)
    voidlop1 = flet.ElevatedButton("void loop(){", bgcolor="#0000FF", color="#000000", on_click=voidloop1)
    define = flet.ElevatedButton("#define", bgcolor="#4B0082", color="#000000", on_click=define)
    include =flet.ElevatedButton("#include", bgcolor="#4B0082", color="#000000", on_click= include)
    pinMode =flet.ElevatedButton("pinMode( , );", bgcolor="#FF4500", color="#000000", on_click=pinMode)
    digitalWrite = flet.ElevatedButton("digitalWrite( , );", bgcolor="#FF8C00", color="#000000", on_click=digitalWrite)
    digitalRead = flet.ElevatedButton("digitalRead( )", bgcolor="#FF8C00", color="#000000", on_click=digitalRead)
    analogRead = flet.ElevatedButton("analogRead( )", bgcolor="#FF8C00", color="#000000", on_click=analogRead)
    delay = flet.ElevatedButton("delay( );", bgcolor="#FFD700", color="#000000", on_click= delay)
    if1 = flet.ElevatedButton(" if( ){", bgcolor="#663399", color="#000000", on_click= if1 )
    elseif=flet.ElevatedButton("else if( ){", bgcolor="#663399", color="#000000", on_click=  elseif )
    else1=flet.ElevatedButton("}else{", bgcolor="#663399", color="#000000", on_click=  else1)
# **************adicinar os intens na página
    pagina.add(flet.Row([voidsetup1,voidlop1], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([define,include ], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([pinMode], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([digitalWrite,digitalRead ], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([ analogRead,delay], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([if1, elseif, else1], alignment=flet.MainAxisAlignment.CENTER))


#**************forma de visualização do aplicativo (visualização app)
flet.app(target=main)
#**************forma de visualização do aplicativo (visualização web "navegador")
#flet.app(target=main,view=flet.WEB_BROWSER)
