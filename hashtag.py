import flet as ft

def main(pagina):
    titulo = ft.Text("HashZap")
    titulo_janela = ft.Text("Bem Vindo ao Hashzap")
    
    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)    
        chat.controls.append(texto_mensagem)
        pagina.update() 
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento): 
        mensagem = f"{campo_nome.value}:{campo_mensagem.value}"    
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value =""
        pagina.update() 

    campo_mensagem = ft.TextField(label="Digite Sua Mensagem", on_submit=enviar_mensagem) 
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    # arquivo = ft.FilePicker()
    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        pagina.pubsub.send_all(f"{campo_nome.value}Entrou no chat")
        janela.open = False
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        pagina.add(chat) 
        pagina.add(linha_mensagem)
        pagina.update()
    
    campo_nome = ft.TextField(label="Digite o Seu Nome",on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome,
        actions=[botao_entrar])

    def abrir_dialog(evento):
        pagina.dialog = janela
        pagina.open(janela)
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)