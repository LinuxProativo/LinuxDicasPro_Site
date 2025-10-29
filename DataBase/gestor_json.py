import json
import os


class GestorJSON:
    def __init__(self, arquivo="database.json"):
        self.arquivo = arquivo
        self.dados = {
            "comunicados": [],
            "links": [],
            "produtos": {
                "hotmart": [],
                "shopee": [],
                "mercado_livre": [],
                "amazon": []
            }
        }
        self._carregar()

    def _carregar(self):
        """Carrega o JSON do disco ou cria padrão se não existir."""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, "r", encoding="utf-8") as f:
                    self.dados = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._salvar()  # recria se estiver corrompido
        else:
            self._salvar()

    def _salvar(self):
        """Salva os dados no arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.dados, f, indent=4, ensure_ascii=False)

    # -------------------------
    # COMUNICADOS
    # -------------------------
    def adicionar_comunicado(self, titulo, descricao):
        self.dados["comunicados"].append({"titulo": titulo, "descricao": descricao})
        self._salvar()

    def editar_comunicado(self, indice, dados):
        indice = int(indice)
        if 0 <= indice < len(self.dados["comunicados"]):
            if dados["titulo"] is not None:
                self.dados["comunicados"][indice]["titulo"] = dados["titulo"]
            if dados["descricao"] is not None:
                self.dados["comunicados"][indice]["descricao"] = dados["descricao"]
            self._salvar()

    def remover_comunicado(self, indice):
        if 0 <= indice < len(self.dados["comunicados"]):
            del self.dados["comunicados"][indice]
            self._salvar()

    def listar_comunicados(self):
        return self.dados["comunicados"]

    # -------------------------
    # LINKS
    # -------------------------
    def adicionar_link(self, titulo, subtitulo, link, imagem):
        self.dados["links"].append({
            "titulo": titulo,
            "subtitulo": subtitulo,
            "link": link,
            "link_imagem": imagem
        })
        self._salvar()

    def editar_link(self, indice, dados):
        indice = int(indice)
        if 0 <= indice < len(self.dados["links"]):
            if dados["titulo"] is not None:
                self.dados["links"][indice]["titulo"] = dados["titulo"]
            if dados["subtitulo"] is not None:
                self.dados["links"][indice]["subtitulo"] = dados["subtitulo"]
            if dados["link"] is not None:
                self.dados["links"][indice]["link"] = dados["link"]
            if dados["link_imagem"] is not None:
                self.dados["links"][indice]["link_imagem"] = dados["link_imagem"]
            self._salvar()

    def remover_link(self, indice):
        if 0 <= indice < len(self.dados["links"]):
            del self.dados["links"][indice]
            self._salvar()

    def listar_links(self):
        return self.dados["links"]

    # -------------------------
    # PRODUTOS
    # -------------------------
    def adicionar_produto(self, categoria, nome, descricao, link, imagem):
        if categoria in self.dados["produtos"]:
            self.dados["produtos"][categoria].append({
                "nome": nome,
                "descricao": descricao,
                "link": link,
                "link_imagem": imagem
            })
            self._salvar()

    def editar_produto(self, categoria, indice, dados):
        indice = int(indice)
        if categoria in self.dados["produtos"]:
            if 0 <= indice < len(self.dados["produtos"][categoria]):
                produto = self.dados["produtos"][categoria][indice]
                if dados["nome"] is not None:
                    produto["nome"] = dados["nome"]
                if dados["descricao"] is not None:
                    produto["descricao"] = dados["descricao"]
                if dados["link"] is not None:
                    produto["link"] = dados["link"]
                if dados["link_imagem"] is not None:
                    produto["link_imagem"] = dados["link_imagem"]
                self._salvar()

    def remover_produto(self, categoria, indice):
        if categoria in self.dados["produtos"]:
            if 0 <= indice < len(self.dados["produtos"][categoria]):
                del self.dados["produtos"][categoria][indice]
                self._salvar()

    def listar_produtos(self, categoria):
        if categoria in self.dados["produtos"]:
            return self.dados["produtos"][categoria]
        return []
