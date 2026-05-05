import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fanfication")
        self.geometry("900x650")
        self.configure(fg_color="#30292F")
        self.usuario = None
        self.frame_atual = None

        self.mostrar_login()

    def trocar_frame(self, novo_frame):
        if self.frame_atual:
            self.frame_atual.destroy()
        self.frame_atual = novo_frame
        self.frame_atual.pack(fill="both", expand=True)

    def mostrar_login(self):
        from ui.login import TelaLogin
        self.trocar_frame(TelaLogin(self))

    def mostrar_cadastro(self):
        from ui.cadastro import TelaCadastro
        self.trocar_frame(TelaCadastro(self))

    def mostrar_feed(self, usuario):
        self.usuario = usuario
        from ui.feed import TelaFeed
        self.trocar_frame(TelaFeed(self))

    def mostrar_perfil(self):
        from ui.perfil import TelaPerfil
        self.trocar_frame(TelaPerfil(self))

    def mostrar_biblioteca(self):
        from ui.biblioteca import TelaBiblioteca
        self.trocar_frame(TelaBiblioteca(self))

    def mostrar_editor(self):
        from ui.editor import TelaEditor
        self.trocar_frame(TelaEditor(self))