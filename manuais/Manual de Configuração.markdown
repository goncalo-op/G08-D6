# Manual de Configuração

## Introdução
Este manual explica como configurar o SafeCloud, incluindo montagens no Minikube, certificados SSL/TLS, VPN, gestão de portas, aplicação de manifestos Kubernetes, e inicialização das bases de dados.

## Pré-requisitos
- Concluído o [Manual de Instalação](#manual-de-instalacao).
- Cluster Minikube ativo (`minikube status`).
- Ficheiros do projeto em `~/Desktop/Projeto3Cadeiras`.

## Passos de Configuração

1. **Iniciar Minikube**
   ```bash
   minikube start --driver=docker
   kubectl config use-context minikube
   ```

2. **Configurar Montagens (em Background)**
   Abra dois terminais:
   - **Terminal 1**: Montar diretório do projeto:
     ```bash
     minikube mount ~/Desktop/Projeto3Cadeiras:/home/$USER/Desktop/Projeto3Cadeiras
     ```
   - **Terminal 2**: Montar diretório de bases de dados:
     ```bash
     sudo mkdir -p /mnt/db
     sudo chown $USER:$USER /mnt/db
     minikube mount /mnt/db:/mnt/db
     ```
   Mantenha ambos ativos.

3. **Configurar VPN**
   - Copie o ficheiro de configuração VPN (e.g., `safecloud.ovpn`) para `~/Desktop/Projeto3Cadeiras/vpn/`.
   - Inicie a VPN:
     ```bash
     sudo openvpn --config ~/Desktop/Projeto3Cadeiras/vpn/safecloud.ovpn
     ```
   - Verifique conectividade:
     ```bash
     ip addr show tun0
     ```
   - Mantenha a VPN ativa para acesso ao cluster.

4. **Configurar Certificados no Flask**
   Edite `app.py`:
   ```bash
   nano ~/Desktop/Projeto3Cadeiras/app.py
   ```
   Modifique a linha final (`app.run`):
   ```python
   if __name__ == "__main__":
       app.run(debug=True, host="0.0.0.0", ssl_context=('/home/salithekid/Desktop/Projeto3Cadeiras/certs/server.crt', '/home/salithekid/Desktop/Projeto3Cadeiras/certs/server.key'))
   ```
   Salve.

5. **Verificar Conflitos de Porta**
   ```bash
   lsof -i :5000
   ```
   Elimine o processo, se necessário:
   ```bash
   kill -9 <PID>
   ```

6. **Aplicar Manifestos Kubernetes**
   ```bash
   kubectl create -f ~/Desktop/Projeto3Cadeiras/k8s/backend.yaml
   kubectl create -f ~/Desktop/Projeto3Cadeiras/k8s/credentials.yaml
   for i in {1..11}; do kubectl create -f ~/Desktop/Projeto3Cadeiras/k8s/fragment${i}-db.yaml; done
   ```
   Se ocorrerem erros `localhost:8080`:
   ```bash
   kubectl create -f ~/Desktop/Projeto3Cadeiras/k8s/ --validate=false
   ```

7. **Configurar Certificados no Kubernetes**
   Crie um segredo para os certificados:
   ```bash
   kubectl create secret tls safecloud-tls --cert=~/Desktop/Projeto3Cadeiras/certs/server.crt --key=~/Desktop/Projeto3Cadeiras/certs/server.key
   ```
   Edite `k8s/backend.yaml` para usar HTTPS (adicione ingress ou container port 443).

8. **Iniciar Túnel Minikube (em Background)**
   Abra um terceiro terminal:
   ```bash
   minikube tunnel
   ```
   Mantenha ativo.

9. **Verificar Pods**
   ```bash
   kubectl get pods
   ```
   Esperado: `backend`, `credentials`, `fragment1-db` a `fragment11-db` em `Running`. Se `Pending`:
   ```bash
   kubectl describe pod $(kubectl get pods -l app=backend -o jsonpath='{.items[0].metadata.name}')
   ```
   Reinicie, se necessário:
   ```bash
   kubectl delete pod $(kubectl get pods -l app=backend -o jsonpath='{.items[0].metadata.name}')
   kubectl create -f ~/Desktop/Projeto3Cadeiras/k8s/backend.yaml
   ```

10. **Verificar Bases de Dados**
    ```bash
    ls -l /mnt/db/*.db
    sqlite3 /mnt/db/credentials.db ".schema"
    ```

## Resolução de Problemas
- **Mount Fails**: Verifique permissões (`ls -ld /mnt/db`).
- **Pod Pending**: Confirme mounts e imagem `python:3.9`.
- **VPN Não Conecta**: Verifique `safecloud.ovpn` e logs (`journalctl -u openvpn`).
- **Certificados Rejeitados**: Use `curl -k https://localhost:5000` para testar localmente.