# 💸 Fluxo de Caixa — Bucaneiro

Dashboard interativo de fluxo de caixa para gerenciar recebíveis e pagamentos do Bucaneiro.

## 📌 Como Compartilhar no GitHub + GitHub Pages

### Passo 1: Criar o repositório no GitHub

1. Acesse **github.com** e faça login
2. Clique no **+** no canto superior direito → **New repository**
3. Nome: `fluxo-caixa-bucaneiro`
4. Descrição: `Dashboard de fluxo de caixa do Bucaneiro`
5. Escolha **Public** (para compartilhar)
6. Clique em **Create repository**

### Passo 2: Enviar os arquivos

Opção A - Via GitHub Desktop (mais fácil):
1. Baixe o [GitHub Desktop](https://desktop.github.com)
2. Abra e faça login
3. Clique em **File** → **Clone Repository**
4. Cole a URL do seu repositório (ex: `https://github.com/seu-usuario/fluxo-caixa-bucaneiro`)
5. Escolha a pasta local
6. Copie os arquivos para essa pasta:
   - `index.html`
   - `README.md`
7. No GitHub Desktop, clique em **Commit to main**
8. Clique em **Publish branch**

Opção B - Via Terminal (linha de comando):
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fluxo-caixa-bucaneiro.git
cd fluxo-caixa-bucaneiro

# Copie os arquivos index.html e README.md para essa pasta
# Depois:

git add .
git commit -m "Adiciona dashboard de fluxo de caixa"
git push origin main
```

### Passo 3: Ativar GitHub Pages

1. Abra o repositório no GitHub
2. Vá em **Settings** (engrenagem no topo)
3. Escolha **Pages** na barra lateral esquerda
4. Em "Source", selecione **main** (branch)
5. Clique em **Save**
6. Aguarde ~2 minutos e pronto! 🎉

Seu link será: `https://seu-usuario.github.io/fluxo-caixa-bucaneiro`

## 📊 O que tem no dashboard

- **Fluxo de Caixa**: Edite recebíveis e pagamentos por dia
- **Importar do NIBO**: Carregue CSV de contas a pagar automaticamente
- **Gráficos**: Visualize saldo por dia
- **Salvar localmente**: Dados são salvos no navegador (localStorage)
- **PDF**: Exporte o dashboard como PDF

## 🔒 Modo Visualização (Read-Only)

Compartilhe com sócios sem permissão de edição:
- Adicione `?view` à URL
- Ex: `https://seu-usuario.github.io/fluxo-caixa-bucaneiro?view`

## 💡 Dicas

- Os dados são salvos **localmente no navegador** — cada pessoa tem sua versão
- Use "Publicar para Sócios" para gerar uma versão fixa para compartilhar
- O NIBO CSV precisa ter colunas: `Previsto para`, `Categoria`, `Valor`

---

**Criado com ❤️ por Claude**
