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
            self, text="Fanfication",
            font=("Georgia", 36, "bold"),
            text_color="#5F5AA2"
        )
        self.label_titulo.pack(pady=(30, 0))

        # Subtítulo
        self.label_subtitulo = ctk.CTkLabel(
            self, text="Criar conta",
            font=("Georgia", 20),
            text_color="#8F8AA2"
        )
        self.label_subtitulo.pack(pady=(5, 20))

        # Campo username
        self.entry_username = ctk.CTkEntry(
            self, placeholder_text="Username", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_username.pack(pady=(0, 2))
        self.label_erro_username = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11), height=15
        )
        self.label_erro_username.pack(pady=(0, 3))

        # Campo email
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

        # Campo senha
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

        # Campo data nascimento
        self.entry_data_nasc = ctk.CTkEntry(
            self, placeholder_text="Data de nascimento (DD/MM/AAAA)", width=300, height=45,
            font=("Arial", 14), fg_color="#413F54",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_data_nasc.pack(pady=(0, 2))
        self.label_erro_data = ctk.CTkLabel(
            self, text="", text_color="red", font=("Arial", 11), height=15
        )
        self.label_erro_data.pack(pady=(0, 3))

        # Mensagem de sucesso
        self.label_sucesso = ctk.CTkLabel(
            self, text="", text_color="#5F5AA2", font=("Arial", 12), height=15
        )
        self.label_sucesso.pack(pady=(0, 5))

        # Botão cadastrar
        self.btn_cadastrar = ctk.CTkButton(
            self, text="Cadastrar", width=300, height=45,
            font=("Arial", 15, "bold"),
            fg_color="#5F5AA2", hover_color="#355691",
            command=self.cadastrar
        )
        self.btn_cadastrar.pack(pady=(5, 10))

        # Link login
        self.frame_login = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_login.pack(pady=(5, 0))

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

    def validar_data(self, data):
        try:
            from datetime import datetime
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def cadastrar(self):
        username = self.entry_username.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()
        data_nasc = self.entry_data_nasc.get().strip()

        valido = True

        if not username:
            self.entry_username.configure(border_color="red")
            self.label_erro_username.configure(text="Username obrigatório!")
            valido = False
        elif verificar_username(username):
            self.entry_username.configure(border_color="red")
            self.label_erro_username.configure(text="Username já existe!")
            valido = False
        else:
            self.entry_username.configure(border_color="#5F5AA2")
            self.label_erro_username.configure(text="")

        if not email:
            self.entry_email.configure(border_color="red")
            self.label_erro_email.configure(text="Email obrigatório!")
            valido = False
        elif "@" not in email:
            self.entry_email.configure(border_color="red")
            self.label_erro_email.configure(text="Email inválido!")
            valido = False
        elif verificar_email(email):
            self.entry_email.configure(border_color="red")
            self.label_erro_email.configure(text="Email já cadastrado!")
            valido = False
        else:
            self.entry_email.configure(border_color="#5F5AA2")
            self.label_erro_email.configure(text="")

        if not senha:
            self.entry_senha.configure(border_color="red")
            self.label_erro_senha.configure(text="Senha obrigatória!")
            valido = False
        elif len(senha) < 6:
            self.entry_senha.configure(border_color="red")
            self.label_erro_senha.configure(text="Senha deve ter no mínimo 6 caracteres!")
            valido = False
        else:
            self.entry_senha.configure(border_color="#5F5AA2")
            self.label_erro_senha.configure(text="")

        if not data_nasc:
            self.entry_data_nasc.configure(border_color="red")
            self.label_erro_data.configure(text="Data de nascimento obrigatória!")
            valido = False
        elif not self.validar_data(data_nasc):
            self.entry_data_nasc.configure(border_color="red")
            self.label_erro_data.configure(text="Data inválida! Use DD/MM/AAAA")
            valido = False
        else:
            self.entry_data_nasc.configure(border_color="#5F5AA2")
            self.label_erro_data.configure(text="")

        if valido:
            try:
                from datetime import datetime
                data_formatada = datetime.strptime(data_nasc, "%d/%m/%Y").strftime("%Y-%m-%d")
                cadastrar_usuario(username, email, senha, data_formatada)
                self.label_sucesso.configure(
                    text="✓ Conta criada com sucesso!",
                    text_color="#5F5AA2"
                )
                self.after(2000, lambda: self.ir_para_feed(username))
            except Exception as e:
                self.label_sucesso.configure(
                    text="Erro ao cadastrar. Tente novamente.",
                    text_color="red"
                )

    def ir_para_feed(self, username):
        self.destroy()
        from ui.feed import TelaFeed
        app = TelaFeed(usuario=username)
        app.mainloop()

    def ir_para_login(self):
        self.destroy()
        from ui.login import TelaLogin
        app = TelaLogin()
        app.mainloop()

app = TelaCadastro()
app.mainloop()