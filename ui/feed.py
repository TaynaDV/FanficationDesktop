import customtkinter as ctk

class TelaFeed(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="#30292F")
        self.app = app
        self.usuario = app.usuario

        # ── HEADER ──────────────────────────────────────────
        self.frame_header = ctk.CTkFrame(self, fg_color="#413F54", height=60, corner_radius=0)
        self.frame_header.pack(fill="x")
        self.frame_header.pack_propagate(False)

        self.label_logo = ctk.CTkLabel(
            self.frame_header, text="Fanfication",
            font=("Georgia", 22, "bold"), text_color="#5F5AA2"
        )
        self.label_logo.pack(side="left", padx=20)

        self.entry_busca = ctk.CTkEntry(
            self.frame_header, placeholder_text="Buscar histórias...",
            width=400, height=35, font=("Arial", 13),
            fg_color="#30292F", border_color="#5F5AA2", text_color="white"
        )
        self.entry_busca.pack(side="left", padx=20)

        self.btn_busca = ctk.CTkButton(
            self.frame_header, text="Buscar", width=80, height=35,
            font=("Arial", 13), fg_color="#5F5AA2", hover_color="#355691",
            command=self.buscar
        )
        self.btn_busca.pack(side="left")

        # ── CONTEÚDO PRINCIPAL ──────────────────────────────
        self.frame_conteudo = ctk.CTkScrollableFrame(self, fg_color="#30292F")
        self.frame_conteudo.pack(fill="both", expand=True, padx=20, pady=10)

        self.carregar_categorias()

        # ── BARRA INFERIOR ──────────────────────────────────
        self.frame_nav = ctk.CTkFrame(self, fg_color="#413F54", height=60, corner_radius=0)
        self.frame_nav.pack(fill="x", side="bottom")
        self.frame_nav.pack_propagate(False)

        self.btn_biblioteca = ctk.CTkButton(
            self.frame_nav, text="📚  Biblioteca", width=180, height=45,
            font=("Arial", 13), fg_color="transparent",
            text_color="white", hover_color="#5F5AA2",
            command=self.app.mostrar_biblioteca
        )
        self.btn_biblioteca.pack(side="left", expand=True)

        self.btn_criar = ctk.CTkButton(
            self.frame_nav, text="✏️  Criar", width=180, height=45,
            font=("Arial", 13), fg_color="transparent",
            text_color="white", hover_color="#5F5AA2",
            command=self.app.mostrar_editor
        )
        self.btn_criar.pack(side="left", expand=True)

        username = self.usuario[1] if self.usuario else "Perfil"
        self.btn_perfil = ctk.CTkButton(
            self.frame_nav, text=f"👤  {username}", width=180, height=45,
            font=("Arial", 13), fg_color="transparent",
            text_color="white", hover_color="#5F5AA2",
            command=self.app.mostrar_perfil
        )
        self.btn_perfil.pack(side="left", expand=True)

    def carregar_categorias(self):
        categorias = [
            "Em alta 🔥",
            "Novidades ✨",
            "Romance 💕",
            "Fantasia 🧙",
            "Terror 👻",
            "Ficção Científica 🚀"
        ]

        for categoria in categorias:
            label_cat = ctk.CTkLabel(
                self.frame_conteudo, text=categoria,
                font=("Georgia", 18, "bold"), text_color="#5F5AA2"
            )
            label_cat.pack(anchor="w", pady=(15, 5))

            frame_linha = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
            frame_linha.pack(fill="x", pady=(0, 5))

            for i in range(4):
                card = ctk.CTkFrame(
                    frame_linha, fg_color="#413F54",
                    width=180, height=220, corner_radius=12
                )
                card.pack(side="left", padx=8)
                card.pack_propagate(False)

                capa = ctk.CTkFrame(
                    card, fg_color="#30292F",
                    width=160, height=140, corner_radius=8
                )
                capa.pack(padx=10, pady=(10, 5))
                capa.pack_propagate(False)

                ctk.CTkLabel(
                    capa, text="📖", font=("Arial", 40)
                ).pack(expand=True)

                ctk.CTkLabel(
                    card, text=f"História {i+1}",
                    font=("Arial", 12, "bold"), text_color="white"
                ).pack(padx=10, anchor="w")

                ctk.CTkLabel(
                    card, text="Autor desconhecido",
                    font=("Arial", 10), text_color="#8F8AA2"
                ).pack(padx=10, anchor="w")

    def buscar(self):
        pass