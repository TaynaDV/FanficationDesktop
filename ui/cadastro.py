import customtkinter as ctk
from controllers.usuario import verificar_username, verificar_email, cadastrar_usuario

class TelaCadastro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fanfication")
        self.geometry("750x600")
        self.configure(fg_color="#30292F")

        # Título
        self.label_titulo = ctk.CTkLabel(
            self,
            text="Fanfication",
            font=("Georgia", 36, "bold"),
            text_color="#5F5AA2"
        )
        self.label_titulo.pack(pady=(40, 0))

        # Subtítulo
        self.label_subtitulo = ctk.CTkLabel(
            self,
            text="Criar conta",
            font=("Georgia", 20),
            text_color="#8F8AA2"
        )
        self.label_subtitulo.pack(pady=(5, 30))

        # Campo username
        self.entry_username = ctk.CTkEntry(
            self, placeholder_text="Username", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_username.pack(pady=(0, 2))
        self.label_erro_username = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11)
        )
        self.label_erro_username.pack(pady=(0, 8))

        # Campo email
        self.entry_email = ctk.CTkEntry(
            self, placeholder_text="Email", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_email.pack(pady=(0, 2))
        self.label_erro_email = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11)
        )
        self.label_erro_email.pack(pady=(0, 8))

        # Campo senha
        self.entry_senha = ctk.CTkEntry(
            self, placeholder_text="Senha", show="*", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_senha.pack(pady=(0, 10))

        # Campo data nascimento
        self.entry_data_nasc = ctk.CTkEntry(
            self, placeholder_text="Data de nascimento (DD/MM/AAAA)", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_data_nasc.pack(pady=(0, 20))

        # Botão cadastrar
        self.btn_cadastrar = ctk.CTkButton(
            self, text="Cadastrar", width=300, height=45,
            font=("Arial", 15, "bold"),
            fg_color="#5F5AA2", hover_color="#355691",
            command=self.cadastrar
        )
        self.btn_cadastrar.pack(pady=(0, 15))

        # Link login
        self.frame_login = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_login.pack()

        self.label_tem_conta = ctk.CTkLabel(
            self.frame_login, text="Já tem conta?",
            text_color="#3F4045", font=("Arial", 13)
        )
        self.label_tem_conta.pack(side="left")

        self.btn_login = ctk.CTkButton(
            self.frame_login, text="Entre aqui",
            fg_color="transparent", text_color="#5F5AA2",
            hover_color="#30292F", width=100, font=("Arial", 13, "bold"),
            command=self.ir_para_login
        )
        self.btn_login.pack(side="left")

    def cadastrar(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        data_nasc = self.entry_data_nasc.get()

        valido = True

        if verificar_username(username):
            self.entry_username.configure(border_color="red")
            self.label_erro_username.configure(text="Username já existe!")
            valido = False
        else:
            self.entry_username.configure(border_color="#5F5AA2")
            self.label_erro_username.configure(text="")

        if verificar_email(email):
            self.entry_email.configure(border_color="red")
            self.label_erro_email.configure(text="Email já cadastrado!")
            valido = False
        else:
            self.entry_email.configure(border_color="#5F5AA2")
            self.label_erro_email.configure(text="")

        if valido:
            cadastrar_usuario(username, email, senha, data_nasc)
            self.destroy()
            from ui.feed import TelaFeed
            app = TelaFeed()
            app.mainloop()

    def ir_para_login(self):
        self.destroy()
        from ui.login import TelaLogin
        app = TelaLogin()
        app.mainloop()

app = TelaCadastro()
app.mainloop()