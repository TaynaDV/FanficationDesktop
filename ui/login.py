import customtkinter as ctk

class TelaLogin(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="#30292F")
        self.app = app

        self.label_titulo = ctk.CTkLabel(
            self, text="Fanfication",
            font=("Georgia", 36, "bold"),
            text_color="#5F5AA2"
        )
        self.label_titulo.pack(pady=(60, 30))

        self.entry_email = ctk.CTkEntry(
            self, placeholder_text="Email", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_email.pack(pady=(0, 2))
        self.label_erro_email = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11), height=15
        )
        self.label_erro_email.pack(pady=(0, 3))

        self.entry_senha = ctk.CTkEntry(
            self, placeholder_text="Senha", show="*", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_senha.pack(pady=(0, 2))
        self.label_erro_senha = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11), height=15
        )
        self.label_erro_senha.pack(pady=(0, 3))

        self.label_erro_geral = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11), height=15
        )
        self.label_erro_geral.pack(pady=(0, 3))

        self.btn_login = ctk.CTkButton(
            self, text="Entrar", width=300, height=45,
            font=("Arial", 15, "bold"),
            fg_color="#5F5AA2", hover_color="#355691",
            command=self.fazer_login
        )
        self.btn_login.pack(pady=(10, 20))

        self.frame_cadastro = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_cadastro.pack()

        self.label_nao_tem_conta = ctk.CTkLabel(
            self.frame_cadastro, text="Ainda não tem conta?",
            text_color="#3F4045", font=("Arial", 13)
        )
        self.label_nao_tem_conta.pack(side="left")

        self.btn_cadastro = ctk.CTkButton(
            self.frame_cadastro, text="Cadastre-se",
            fg_color="transparent", text_color="#5F5AA2",
            hover_color="#30292F", width=100,
            font=("Arial", 13, "bold"),
            command=self.app.mostrar_cadastro
        )
        self.btn_cadastro.pack(side="left")

    def fazer_login(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        valido = True

        if not email:
            self.entry_email.configure(border_color="red")
            self.label_erro_email.configure(text="Email obrigatório!")
            valido = False
        elif "@" not in email:
            self.entry_email.configure(border_color="red")
            self.label_erro_email.configure(text="Email inválido!")
            valido = False
        else:
            self.entry_email.configure(border_color="#5F5AA2")
            self.label_erro_email.configure(text="")

        if not senha:
            self.entry_senha.configure(border_color="red")
            self.label_erro_senha.configure(text="Senha obrigatória!")
            valido = False
        else:
            self.entry_senha.configure(border_color="#5F5AA2")
            self.label_erro_senha.configure(text="")

        if valido:
            try:
                from controllers.usuario import fazer_login
                usuario = fazer_login(email, senha)
                if usuario:
                    self.app.mostrar_feed(usuario)
                else:
                    self.label_erro_geral.configure(text="Email ou senha incorretos!")
            except Exception as e:
                print(e)
                self.label_erro_geral.configure(text="Erro ao conectar. Tente novamente.")