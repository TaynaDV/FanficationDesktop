import customtkinter as ctk

ctk.set_appearance_mode("dark")

class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fanfication")
        self.geometry("400x600")
        self.configure(fg_color="#30292F")
        
        # Título
        self.label_titulo = ctk.CTkLabel(
            self, 
            text="Fanfication",
            font=("Georgia", 36, "bold"),
            text_color="#5F5AA2"
        )
        self.label_titulo.pack(pady=40)
        
        # Campo email
        self.entry_email = ctk.CTkEntry(
            self,
            placeholder_text="Email",
            width=300,
            height=45,
            font=("Arial", 14),
            fg_color="#413F54",
            border_color="#5F5AA2",
            text_color="white"
        )
        self.entry_email.pack(pady=10)
        
        # Campo senha
        self.entry_senha = ctk.CTkEntry(
            self,
            placeholder_text="Senha",
            show="*",
            width=300,
            height=45,
            font=("Arial", 14),
            fg_color="#413F54",
            border_color="#5F5AA2",
            text_color="white"
        )
        self.entry_senha.pack(pady=10)
        
        # Botão login
        self.btn_login = ctk.CTkButton(
            self,
            text="Entrar",
            width=300,
            height=45,
            font=("Arial", 15, "bold"),
            fg_color="#5F5AA2",
            hover_color="#355691"
        )
        self.btn_login.pack(pady=20)
        
        ## Frame cadastro
        self.frame_cadastro = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_cadastro.pack(pady=20)

        self.label_nao_tem_conta = ctk.CTkLabel(
            self.frame_cadastro,
            text="Ainda não tem conta?",
            text_color="#3F4045",
            font=("Arial", 13)
        )
        self.label_nao_tem_conta.pack(side="left")

        self.btn_cadastro = ctk.CTkButton(
            self.frame_cadastro,
            text="Cadastre-se",
            fg_color="transparent",
            text_color="#5F5AA2",
            hover_color="#30292F",
            width=100,
            font=("Arial", 13, "bold")
        )
        self.btn_cadastro.pack(side="left")
app = TelaLogin()
app.mainloop()