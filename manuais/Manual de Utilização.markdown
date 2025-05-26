# Manual de Utilização

## Introdução
Este manual descreve como utilizar o SafeCloud via interface web segura (HTTPS), com acesso protegido por VPN, para gerir ficheiros, credenciais, e fragmentos.

## Pré-requisitos
- Concluídos o [Manual de Instalação](#manual-de-instalacao) e o [Manual de Configuração](#manual-de-configuracao).
- Backend ativo (local ou Kubernetes).
- VPN ativa (se Kubernetes).
- Certificados configurados.

## Aceder à Interface Web
1. **Localmente (HTTPS)**:
   ```bash
   cd ~/Desktop/Projeto3Cadeiras
   source venv/bin/activate
   lsof -i :5000
   kill -9 <PID>
   python3 app.py
   ```
   Aceda a `https://localhost:5000` no Brave (aceite o certificado autoassinado).

2. **Kubernetes (via VPN)**:
   - Certifique-se de que a VPN está ativa:
     ```bash
     sudo openvpn --config ~/Desktop/Projeto3Cadeiras/vpn/safecloud.ovpn
     ```
   - Port-forward:
     ```bash
     kubectl port-forward $(kubectl get pods -l app=backend -o jsonpath='{.items[0].metadata.name}') 5000:5000
     ```
   - Aceda a `https://localhost:5000`.

## Login e Registo
1. **Registo**:
   - Aceda a `https://localhost:5000/register`.
   - Preencha o formulário (nome de utilizador, palavra-passe).
   - Credenciais são armazenadas em `/mnt/db/credentials.db` (tabela `users`).
   - Verifique:
     ```bash
     sqlite3 /mnt/db/credentials.db "SELECT * FROM users"
     ```

2. **Login**:
   - Aceda a `https://localhost:5000/login`.
   - Insira credenciais.
   - Redirecionado para `/dashboard`.

## Carregar Ficheiros
1. **Criar Ficheiro de Teste**:
   ```bash
   echo "Test file" > ~/Desktop/Projeto3Cadeiras/Uploads/test.txt
   ```

2. **Upload**:
   - Aceda a `https://localhost:5000/upload`.
   - Selecione `test.txt` e submeta.
   - Esperado: “Ficheiro 'test.txt' carregado com sucesso!”.
   - Verifique:
     ```bash
     ls -l ~/Desktop/Projeto3Cadeiras/Uploads
     sqlite3 /mnt/db/credentials.db "SELECT file_id, filename FROM files"
     ```

## Reconstruir e Descarregar Ficheiros
1. **Reconstruir**:
   - Aceda a `https://localhost:5000/rebuild?filename=test.txt`.
   - Esperado: Link para descarregar `test.txt_reconstruida.txt`.

2. **Verificar**:
   ```bash
   ls -l ~/Desktop/Projeto3Cadeiras/Uploads/*_reconstruida*
   ```

## Verificar Fragmentos
1. **Inspecionar**:
   ```bash
   sqlite3 /mnt/db/fragment1.db ".schema"
   sqlite3 /mnt/db/fragment1.db "SELECT * FROM fragments"
   sqlite3 /mnt/db/fragment2.db "SELECT * FROM fragments"
   ```
   Esperado: Dados como `test.txt|1|<binary_data>`.

## Verificar Certificados
1. **Localmente**:
   ```bash
   openssl x509 -in ~/Desktop/Projeto3Cadeiras/certs/server.crt -text -noout
   ```
2. **Kubernetes**:
   ```bash
   kubectl get secret safecloud-tls -o yaml
   ```

## Resolução de Problemas
- **Upload Falha**: Verifique `enctype="multipart/form-data"` em `upload.html`.
- **Certificado Inválido**: Aceite o aviso no navegador ou use Let’s Encrypt.
- **VPN Desconectada**: Reinicie (`sudo openvpn --config ...`).