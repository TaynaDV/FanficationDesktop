import customtkinter as ctk
from PIL import Image
from controllers.usuario import buscar_perfil, atualizar_perfil, buscar_seguidores, buscar_seguindo
from controllers.historias import buscar_historias_usuario
from controllers.lista import buscar_listas
import tkinter.filedialog as filedialog

class TelaPerfil(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="#30292F")
        self.app = app
        self.usuario = app.usuario
        self.foto_path = None

        perfil = buscar_perfil(self.usuario[0])

        # ── HEADER ──────────────────────────────────────────
        self.frame_header = ctk.CTkFrame(self, fg_color="#413F54", height=60, corner_radius=0)
        self.frame_header.pack(fill="x")
        self.frame_header.pack_propagate(False)

        self.label_logo = ctk.CTkLabel(
            self.frame_header, text="Fanfication",
            font=("Georgia", 22, "bold"), text_color="#5F5AA2"
        )
        self.label_logo.pack(side="left", padx=20)

        self.btn_voltar = ctk.CTkButton(
            self.frame_header, text="← Voltar", width=80, height=35,
            font=("Arial", 13), fg_color="transparent",
            text_color="white", hover_color="#5F5AA2",
            command=lambda: self.app.mostrar_feed(self.usuario)
        )
        self.btn_voltar.pack(side="right", padx=20)

        # ── CONTEÚDO ────────────────────────────────────────
        self.frame_conteudo = ctk.CTkScrollableFrame(self, fg_color="#30292F")
        self.frame_conteudo.pack(fill="both", expand=True, padx=20, pady=10)

        # Foto e info do perfil
        self.frame_topo = ctk.CTkFrame(self.frame_conteudo, fg_color="#413F54", corner_radius=12)
        self.frame_topo.pack(fill="x", pady=(10, 20))

        # Foto de perfil
        self.frame_foto = ctk.CTkFrame(self.frame_topo, fg_color="#30292F", width=100, height=100, corner_radius=50)
        self.frame_foto.pack(side="left", padx=20, pady=20)
        self.frame_foto.pack_propagate(False)

        self.label_foto = ctk.CTkLabel(
            self.frame_foto, text="👤", font=("Arial", 40)
        )
        self.label_foto.pack(expand=True)

        if perfil and perfil[3]:
            self.carregar_foto(perfil[3])

        self.btn_foto = ctk.CTkButton(
            self.frame_foto, text="✏️", width=25, height=25,
            font=("Arial", 12), fg_color="#5F5AA2",
            hover_color="#355691", corner_radius=12,
            command=self.escolher_foto
        )
        self.btn_foto.place(relx=0.7, rely=0.7)

        # Info do perfil
        self.frame_info = ctk.CTkFrame(self.frame_topo, fg_color="transparent")
        self.frame_info.pack(side="left", padx=10, pady=20, fill="x", expand=True)

        self.label_username = ctk.CTkLabel(
            self.frame_info,
            text=perfil[1] if perfil else self.usuario[1],
            font=("Georgia", 24, "bold"), text_color="white"
        )
        self.label_username.pack(anchor="w")

        # Seguidores e seguindo
        seguidores = buscar_seguidores(self.usuario[0])
        seguindo = buscar_seguindo(self.usuario[0])

        self.frame_stats = ctk.CTkFrame(self.frame_info, fg_color="transparent")
        self.frame_stats.pack(anchor="w", pady=5)

        ctk.CTkLabel(
            self.frame_stats,
            text=f"{len(seguidores)} seguidores",
            font=("Arial", 12), text_color="#8F8AA2"
        ).pack(side="left", padx=(0, 15))

        ctk.CTkLabel(
            self.frame_stats,
            text=f"{len(seguindo)} seguindo",
            font=("Arial", 12), text_color="#8F8AA2"
        ).pack(side="left")

        # Bio
        self.entry_bio = ctk.CTkTextbox(
            self.frame_info, width=400, height=60,
            font=("Arial", 13), fg_color="#30292F",
            border_color="#5F5AA2", text_color="white"
        )
        self.entry_bio.pack(anchor="w", pady=(5, 0))

        if perfil and perfil[2]:
            self.entry_bio.insert("0.0", perfil[2])

        self.btn_salvar = ctk.CTkButton(
            self.frame_info, text="Salvar perfil", width=120, height=32,
            font=("Arial", 12), fg_color="#5F5AA2", hover_color="#355691",
            command=self.salvar_perfil
        )
        self.btn_salvar.pack(anchor="w", pady=(8, 0))

        # ── ABAS ────────────────────────────────────────────
        self.frame_abas = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        self.frame_abas.pack(fill="x", pady=(0, 10))

        self.btn_aba_historias = ctk.CTkButton(
            self.frame_abas, text="Histórias",
            width=150, height=35, font=("Arial", 13),
            fg_color="#5F5AA2", hover_color="#355691",
            command=lambda: self.mudar_aba("historias")
        )
        self.btn_aba_historias.pack(side="left", padx=(0, 5))

        self.btn_aba_listas = ctk.CTkButton(
            self.frame_abas, text="Listas de leitura",
            width=150, height=35, font=("Arial", 13),
            fg_color="#413F54", hover_color="#355691",
            command=lambda: self.mudar_aba("listas")
        )
        self.btn_aba_listas.pack(side="left", padx=(0, 5))

        self.btn_aba_seguindo = ctk.CTkButton(
            self.frame_abas, text="Seguindo",
            width=150, height=35, font=("Arial", 13),
            fg_color="#413F54", hover_color="#355691",
            command=lambda: self.mudar_aba("seguindo")
        )
        self.btn_aba_seguindo.pack(side="left")

        # Frame do conteúdo das abas
        self.frame_aba_conteudo = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        self.frame_aba_conteudo.pack(fill="both", expand=True)

        self.carregar_aba_historias()

        # ── BARRA INFERIOR ──────────────────────────────────
        self.frame_nav = ctk.CTkFrame(self, fg_color="#413F54", height=60, corner_radius=0)
        self.frame_nav.pack(fill="x", side="bottom")
        self.frame_nav.pack_propagate(False)

        self.btn_feed = ctk.CTkButton(
            self.frame_nav, text="🏠  Feed", width=180, height=45,
            font=("Arial", 13), fg_color="transparent",
            text_color="white", hover_color="#5F5AA2",
            command=lambda: self.app.mostrar_feed(self.usuario)
        )
        self.btn_feed.pack(side="left", expand=True)

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
            font=("Arial", 13), fg_color="#5F5AA2",
            text_color="white", hover_color="#355691"
        )
        self.btn_perfil.pack(side="left", expand=True)

    def carregar_foto(self, path):
        try:
            img = Image.open(path)
            img = img.resize((100, 100))
            ctk_img = ctk.CTkImage(img, size=(100, 100))
            self.label_foto.configure(image=ctk_img, text="")
            self.label_foto.image = ctk_img
            self.foto_path = path
        except:
            pass

    def escolher_foto(self):
        path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if path:
            self.carregar_foto(path)

    def salvar_perfil(self):
        bio = self.entry_bio.get("0.0", "end").strip()
        atualizar_perfil(self.usuario[0], bio, self.foto_path)
        self.label_username.configure(text="✓ Perfil salvo!")
        self.after(2000, lambda: self.label_username.configure(text=self.usuario[1]))

    def mudar_aba(self, aba):
        for widget in self.frame_aba_conteudo.winfo_children():
            widget.destroy()

        self.btn_aba_historias.configure(fg_color="#413F54")
        self.btn_aba_listas.configure(fg_color="#413F54")
        self.btn_aba_seguindo.configure(fg_color="#413F54")

        if aba == "historias":
            self.btn_aba_historias.configure(fg_color="#5F5AA2")
            self.carregar_aba_historias()
        elif aba == "listas":
            self.btn_aba_listas.configure(fg_color="#5F5AA2")
            self.carregar_aba_listas()
        elif aba == "seguindo":
            self.btn_aba_seguindo.configure(fg_color="#5F5AA2")
            self.carregar_aba_seguindo()

    def carregar_aba_historias(self):
        self.btn_aba_historias.configure(fg_color="#5F5AA2")
        try:
            historias = buscar_historias_usuario(self.usuario[0])
            if not historias:
                ctk.CTkLabel(
                    self.frame_aba_conteudo,
                    text="Nenhuma história publicada ainda.",
                    text_color="#8F8AA2", font=("Arial", 13)
                ).pack(pady=20)
            else:
                for h in historias:
                    card = ctk.CTkFrame(
                        self.frame_aba_conteudo, fg_color="#413F54", corner_radius=10
                    )
                    card.pack(fill="x", pady=5)
                    ctk.CTkLabel(
                        card, text=h[2],
                        font=("Arial", 14, "bold"), text_color="white"
                    ).pack(anchor="w", padx=15, pady=(10, 2))
                    ctk.CTkLabel(
                        card, text=h[5],
                        font=("Arial", 12), text_color="#8F8AA2"
                    ).pack(anchor="w", padx=15, pady=(0, 10))
        except Exception as e:
            print(e)
            ctk.CTkLabel(
                self.frame_aba_conteudo,
                text="Erro ao carregar histórias.",
                text_color="red", font=("Arial", 13)
            ).pack(pady=20)

    def carregar_aba_listas(self):
        self.btn_aba_listas.configure(fg_color="#5F5AA2")

        self.btn_criar_lista = ctk.CTkButton(
            self.frame_aba_conteudo, text="+ Nova lista",
            width=150, height=35, font=("Arial", 13),
            fg_color="#5F5AA2", hover_color="#355691",
            command=self.criar_lista
        )
        self.btn_criar_lista.pack(anchor="w", pady=(0, 10))

        try:
            listas = buscar_listas(self.usuario[0])
            if not listas:
                ctk.CTkLabel(
                    self.frame_aba_conteudo,
                    text="Nenhuma lista criada ainda.",
                    text_color="#8F8AA2", font=("Arial", 13)
                ).pack(pady=20)
            else:
                for l in listas:
                    frame_lista = ctk.CTkFrame(
                        self.frame_aba_conteudo, fg_color="#413F54", corner_radius=10
                    )
                    frame_lista.pack(fill="x", pady=5)

                    ctk.CTkLabel(
                        frame_lista, text=l[2],
                        font=("Arial", 14, "bold"), text_color="white"
                    ).pack(side="left", padx=15, pady=10)

                    ctk.CTkButton(
                        frame_lista, text="Excluir",
                        width=80, height=30, font=("Arial", 12),
                        fg_color="#A33030", hover_color="#7A1F1F",
                        command=lambda id=l[0]: self.excluir_lista(id)
                    ).pack(side="right", padx=15, pady=10)
        except Exception as e:
            print(e)
            ctk.CTkLabel(
                self.frame_aba_conteudo,
                text="Erro ao carregar listas.",
                text_color="red", font=("Arial", 13)
            ).pack(pady=20)

    def carregar_aba_seguindo(self):
        self.btn_aba_seguindo.configure(fg_color="#5F5AA2")
        try:
            seguindo = buscar_seguindo(self.usuario[0])
            if not seguindo:
                ctk.CTkLabel(
                    self.frame_aba_conteudo,
                    text="Você ainda não segue ninguém.",
                    text_color="#8F8AA2", font=("Arial", 13)
                ).pack(pady=20)
            else:
                for u in seguindo:
                    card = ctk.CTkFrame(
                        self.frame_aba_conteudo, fg_color="#413F54", corner_radius=10
                    )
                    card.pack(fill="x", pady=5)
                    ctk.CTkLabel(
                        card, text=f"👤  {u[1]}",
                        font=("Arial", 14), text_color="white"
                    ).pack(side="left", padx=15, pady=10)
        except Exception as e:
            print(e)
            ctk.CTkLabel(
                self.frame_aba_conteudo,
                text="Erro ao carregar seguindo.",
                text_color="red", font=("Arial", 13)
            ).pack(pady=20)

    def criar_lista(self):
        dialog = ctk.CTkInputDialog(
            text="Nome da nova lista:", title="Nova lista"
        )
        nome = dialog.get_input()
        if nome:
            from controllers.lista import criar_lista
            criar_lista(self.usuario[0], nome)
            self.mudar_aba("listas")

    def excluir_lista(self, id_lista):
        from controllers.lista import excluir_lista
        excluir_lista(id_lista)
        self.mudar_aba("listas")