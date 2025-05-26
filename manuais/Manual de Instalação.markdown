# Manual de Instalação

## Introdução
Este manual descreve como instalar as dependências e preparar o ambiente para o sistema SafeCloud, um serviço de armazenamento de ficheiros seguro com suporte a HTTPS (certificados SSL/TLS) e acesso via VPN, num sistema Debian (e.g., Kali Linux).

## Pré-requisitos
- **Sistema Operativo**: Debian/Kali Linux.
- **Hardware**: 8GB RAM, 2 CPUs, 20GB de espaço livre.
- **Internet**: Necessária para descarregar dependências.
- **Permissões**: Acesso `sudo`.

## Passos de Instalação

1. **Atualizar Pacotes do Sistema**
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Instalar Docker**
   ```bash
   sudo apt install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
   sudo usermod -aG docker $USER
   ```
   Termine a sessão e reinicie-a para aplicar as alterações do grupo.

3. **Instalar Minikube**
   ```bash
   curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube
   minikube version
   ```

4. **Instalar `kubectl`**
   ```bash
   sudo apt install -y kubectl
   kubectl version --client
   ```

5. **Instalar Python e Virtualenv**
   ```bash
   sudo apt install -y python3 python3-pip python3-venv sqlite3
   ```

6. **Instalar OpenVPN (para VPN)**
   ```bash
   sudo apt install -y openvpn
   ```

7. **Clonar Repositório do Projeto**
   ```bash
   mkdir -p ~/Desktop
   cd ~/Desktop
   git clone <url-repositorio> Projeto3Cadeiras
   ```
   Substitua `<url-repositorio>` pelo URL do teu repositório Git.

8. **Configurar Ambiente Virtual**
   ```bash
   cd ~/Desktop/Projeto3Cadeiras
   python3 -m venv venv
   source venv/bin/activate
   pip install flask bcrypt
   ```

9. **Gerar Certificados SSL/TLS (Self-Signed)**
   Crie certificados para HTTPS:
   ```bash
   mkdir -p ~/Desktop/Projeto3Cadeiras/certs
   openssl req -x509 -newkey rsa:4096 -nodes -out ~/Desktop/Projeto3Cadeiras/certs/server.crt -keyout ~/Desktop/Projeto3Cadeiras/certs/server.key -days 365 -subj "/CN=localhost"
   chmod 600 ~/Desktop/Projeto3Cadeiras/certs/*
   ```
   Alternativa: Use Let’s Encrypt (requer domínio público).

10. **Verificar Estrutura de Diretórios**
    ```bash
    ls ~/Desktop/Projeto3Cadeiras
    ```
    Esperado: `app.py`, `templates/`, `Uploads/`, `k8s/`, `venv/`, `certs/`, `vpn/`.

## Resolução de Problemas
- **Docker sem Permissões**: Verifique o grupo `docker` (`groups`).
- **Minikube Não Inicia**: Confirme o Docker ativo (`sudo systemctl status docker`).
- **Erro PEP 668**: Ative o virtualenv (`source venv/bin/activate`).
- **Certificados Inválidos**: Verifique permissões (`ls -l ~/Desktop/Projeto3Cadeiras/certs`).