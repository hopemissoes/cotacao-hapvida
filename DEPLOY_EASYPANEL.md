# Deploy no Easypanel (Hostinger VPS)

## Arquivos Necessarios
- `app_cotacao.py` - Aplicacao principal
- `templates/index_cotacao.html` - Interface web
- `requirements.txt` - Dependencias Python
- `Dockerfile` - Configuracao do container

## Passo a Passo

### 1. Acesse o Easypanel
- Entre no painel do Easypanel da sua VPS Hostinger
- Clique em "Create Project" ou "Novo Projeto"

### 2. Crie um novo servico
- Escolha "App" ou "Docker"
- Selecione "GitHub" ou "Upload" dependendo de onde esta o codigo

### 3. Opcao A: Via GitHub
1. Suba os arquivos para um repositorio GitHub
2. No Easypanel, conecte o repositorio
3. O Easypanel detectara automaticamente o Dockerfile

### 3. Opcao B: Via Upload/Docker Image
1. No Easypanel, escolha "Docker Image"
2. Use a imagem customizada ou faca build local

### 4. Configuracoes no Easypanel

**Porta:**
- Container Port: 5000
- Public Port: 80 ou 443 (com SSL)

**Variaveis de Ambiente:**
```
PORT=5000
PYTHONUNBUFFERED=1
```

**Recursos (IMPORTANTE para Selenium):**
- Memory: 2GB (minimo)
- CPU: 1 core (minimo)
- Shared Memory (shm): 2GB

### 5. Dominio
- Configure um dominio ou subdominio no Easypanel
- Ative o SSL (Let's Encrypt)

### 6. Deploy
- Clique em "Deploy" ou "Build & Deploy"
- Aguarde o build do Docker (pode levar alguns minutos)

## Acesso
Apos o deploy, acesse:
- `https://seu-dominio.com` ou
- `http://ip-da-vps:5000`

## Notas Importantes

1. **Memoria**: O Selenium com Chrome precisa de pelo menos 2GB de RAM
2. **Headless**: O Chrome roda em modo headless (sem interface grafica)
3. **Timeout**: Algumas cotacoes podem demorar, ajuste o timeout se necessario
4. **Logs**: Verifique os logs no Easypanel se houver erros

## Troubleshooting

### Erro de memoria
Aumente a memoria do container para 3GB ou mais

### Chrome nao inicia
Verifique se as flags `--no-sandbox` e `--disable-dev-shm-usage` estao ativas

### Timeout
O site pode estar lento, aumente os `time.sleep()` no codigo

## Estrutura do Projeto para Upload

```
cotacao-hapvida/
├── app_cotacao.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── templates/
    └── index_cotacao.html
```
