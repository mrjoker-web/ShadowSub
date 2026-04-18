<p align="center">
  <h1>ShadowSub</h1>
  <p>⚡ Advanced Subdomain Finder for Ethical Hackers</p>
</p>

---

## 🔍 Sobre o Projeto

**ShadowSub** é uma ferramenta avançada de descoberta de subdomínios desenvolvida para **reconnaissance em pentesting ético**.

Criada por **Mr Joker**, esta tool permite identificar subdomínios ativos de forma rápida e eficiente, utilizando multi-threading e análise HTTP/HTTPS.

---

## ⚡ Funcionalidades

- 🌐 Descoberta de subdomínios via wordlist  
- ⚡ Multi-threading (rápido e otimizado)  
- 🔄 Suporte HTTP + HTTPS  
- 🧠 Resolução automática de IP  
- 📊 Barra de progresso em tempo real  
- 📁 Exportação de resultados (.txt e .json)  
- 🎨 Interface CLI com cores  

---

## 🎯 Objetivo

Facilitar a fase de **reconhecimento (recon)** em testes de segurança, sendo ideal para:

- Pentesters  
- Estudantes de cybersecurity  
- Entusiastas de ethical hacking  

---

## ⚙️ Instalação

```bash
git clone https://github.com/mrjoker-web/ShadowSub.git
cd ShadowSub
pip install requests

▶️ Como usar

python shadowsub.py -t example.com -w wordlist.txt

Com threads personalizadas:

python shadowsub.py -t example.com -w wordlist.txt --threads 100

📄 Wordlist
Cria um ficheiro wordlist.txt com subdomínios comuns:

www
mail
ftp
admin
test
dev
api
beta
staging
portal


📸 Exemplo de Output

[FOUND] http://admin.example.com (192.168.1.1)
[FOUND] https://api.example.com (192.168.1.2)

[##############################] 100.0%

[+] Output guardado em subdomains.txt e subdomains.json
