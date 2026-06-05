#!/usr/bin/env python3
"""
Script para gerenciar o dashboard Fluxo de Caixa Bucaneiro
- Abrir localmente
- Exportar versão final
- Preparar para GitHub
"""

import os
import sys
import webbrowser
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

# Cores para terminal
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Diretório do script
SCRIPT_DIR = Path(__file__).parent.absolute()
INDEX_FILE = SCRIPT_DIR / "index.html"
README_FILE = SCRIPT_DIR / "README.md"

def print_header():
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("  💸 FLUXO DE CAIXA BUCANEIRO — GERENCIADOR")
    print("=" * 60)
    print(f"{Colors.RESET}\n")

def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.RESET}")

def print_info(msg):
    print(f"{Colors.BLUE}ℹ {msg}{Colors.RESET}")

def print_warning(msg):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.RESET}")

def print_error(msg):
    print(f"{Colors.RED}✗ {msg}{Colors.RESET}")

def open_local():
    """Abre o dashboard no navegador local"""
    print_info("Abrindo dashboard localmente...")

    if not INDEX_FILE.exists():
        print_error(f"Arquivo não encontrado: {INDEX_FILE}")
        return False

    file_url = INDEX_FILE.as_uri()
    webbrowser.open(file_url)
    print_success(f"Dashboard aberto em: {file_url}")
    print_info("Edite os dados no navegador e clique em '💾 Salvar'")
    return True

def show_menu():
    """Mostra menu de opções"""
    print_header()
    print(f"{Colors.BOLD}Escolha uma opção:{Colors.RESET}\n")
    print("  1. 📂 Abrir dashboard localmente")
    print("  2. 📤 Exportar versão final para GitHub")
    print("  3. 🔄 Sincronizar com GitHub (git push)")
    print("  4. 📖 Ver instruções")
    print("  5. ❌ Sair")
    print()

def export_to_github():
    """Prepara a versão final para GitHub"""
    print_info("Preparando versão final...")
    print_warning("IMPORTANTE: Você já salvou os dados no dashboard?")
    response = input("Confirmar (s/n)? ").strip().lower()

    if response != 's':
        print_warning("Exportação cancelada")
        return False

    try:
        # Backup da versão anterior
        backup_dir = SCRIPT_DIR / "backups"
        backup_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"index_backup_{timestamp}.html"

        if INDEX_FILE.exists():
            shutil.copy(INDEX_FILE, backup_file)
            print_success(f"Backup criado: {backup_file.name}")

        # Instruções
        print()
        print_info("Próximas etapas:")
        print("  1. Vá até o navegador com o dashboard aberto")
        print("  2. Clique em '🌐 Publicar para Sócios'")
        print("  3. Baixe o arquivo 'bucaneiro-dashboard.html'")
        print("  4. Renomeie para 'index.html'")
        print("  5. Mova para a pasta do projeto")
        print()
        print_success("Pronto para fazer commit no GitHub!")

        return True

    except Exception as e:
        print_error(f"Erro na exportação: {e}")
        return False

def git_push():
    """Faz commit e push no GitHub"""
    print_info("Sincronizando com GitHub...")

    # Verifica se está em um repositório git
    if not (SCRIPT_DIR / ".git").exists():
        print_error("Não é um repositório git. Execute primeiro:")
        print(f"  git init")
        print(f"  git remote add origin https://github.com/seu-usuario/fluxo-caixa-bucaneiro.git")
        return False

    try:
        # Git status
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=SCRIPT_DIR,
            capture_output=True,
            text=True
        )

        if not result.stdout.strip():
            print_warning("Nenhuma mudança para fazer commit")
            return False

        print("Mudanças detectadas:")
        print(result.stdout)

        response = input(f"\n{Colors.BOLD}Fazer commit e push? (s/n){Colors.RESET} ").strip().lower()

        if response != 's':
            print_warning("Push cancelado")
            return False

        # Mensagem de commit
        message = input("Mensagem de commit (padrão: 'Atualiza dashboard'): ").strip()
        if not message:
            message = "Atualiza dashboard"

        # Add all
        subprocess.run(["git", "add", "."], cwd=SCRIPT_DIR)
        print_info("Arquivos adicionados")

        # Commit
        subprocess.run(["git", "commit", "-m", message], cwd=SCRIPT_DIR)
        print_success("Commit realizado")

        # Push
        subprocess.run(["git", "push", "origin", "main"], cwd=SCRIPT_DIR)
        print_success("Push para GitHub concluído! 🎉")

        return True

    except FileNotFoundError:
        print_error("Git não encontrado. Instale git em seu PC")
        return False
    except Exception as e:
        print_error(f"Erro no git: {e}")
        return False

def show_instructions():
    """Mostra instruções de uso"""
    print_header()
    print(f"{Colors.BOLD}Como usar:{Colors.RESET}\n")
    print("1. ABRIR LOCALMENTE")
    print("   • Escolha opção 1")
    print("   • Edite os dados no navegador")
    print("   • Clique em '💾 Salvar'\n")

    print("2. EXPORTAR PARA GITHUB")
    print("   • Escolha opção 2")
    print("   • Siga as instruções")
    print("   • Baixe o arquivo 'bucaneiro-dashboard.html'")
    print("   • Mude para 'index.html'\n")

    print("3. SINCRONIZAR COM GITHUB")
    print("   • Escolha opção 3")
    print("   • Aprove o commit")
    print("   • Digite uma mensagem")
    print("   • Arquivo vai para GitHub!\n")

    print(f"{Colors.BOLD}Arquivos da pasta:{Colors.RESET}")
    print(f"  • {INDEX_FILE.name} — Dashboard principal")
    print(f"  • {README_FILE.name} — Documentação")
    print(f"  • backups/ — Versões anteriores\n")

    input("Pressione ENTER para voltar ao menu...")

def main():
    """Loop principal"""
    while True:
        show_menu()
        choice = input(f"{Colors.BOLD}Opção ({Colors.GREEN}1-5{Colors.RESET}{Colors.BOLD}):{Colors.RESET} ").strip()

        if choice == '1':
            open_local()
            input("\nPressione ENTER quando terminar...")
        elif choice == '2':
            export_to_github()
            input("\nPressione ENTER para continuar...")
        elif choice == '3':
            git_push()
            input("\nPressione ENTER para continuar...")
        elif choice == '4':
            show_instructions()
        elif choice == '5':
            print_info("Até logo! 👋\n")
            sys.exit(0)
        else:
            print_error("Opção inválida")

        print()

if __name__ == "__main__":
    main()
