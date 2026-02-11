import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(ft.Text("STAR PLATINUM! ZA WARUDO!"))
    
    page.add(
        ft.Text("Olá, meu nome é Jotaro Kujo!"),
        ft.Image(
            src="images/jotaro.jpg",
            height=200,
            width=200
        ),
        ft.Button(
            content="Clique aqui",
            on_click=mostrar_mensagem,
            bgcolor="#D3E602",
            color="white"
        )
    )

ft.app(main)