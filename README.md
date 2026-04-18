<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Version-1.0-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-Subdomain%20Finder-red?style=for-the-badge"/>
</p>

<h1 align="center">🌐 ShadowSub</h1>
<p align="center"><b>Advanced Subdomain Finder for Ethical Hackers</b></p>

---

## 📖 Sobre

**ShadowSub** é uma ferramenta avançada de descoberta de subdomínios desenvolvida para **reconnaissance em pentesting ético**.

Criada por **Mr Joker**, permite identificar subdomínios ativos de forma rápida e eficiente, utilizando multi-threading e análise HTTP/HTTPS.

---

## ⚡ Funcionalidades

- 🌐 Descoberta de subdomínios via wordlist
- ⚡ Multi-threading (rápido e otimizado)
- 🔄 Suporte HTTP + HTTPS
- 🧠 Resolução automática de IP
- 📊 Barra de progresso em tempo real
- 📁 Exportação de resultados em `.txt` e `.json`
- 🎨 Interface CLI com cores

---

## 🔗 Pipeline de Integração

ShadowSub é o **primeiro passo** da suite Shadow:

```
ShadowSub   →  encontra subdomínios        ← aqui
     ↓
ShadowProbe →  verifica quais estão ativos
     ↓
ShadowScan  →  analisa portas e serviços
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/mrjoker-web/ShadowSub.git
cd ShadowSub
pip install requests
```

---

## ▶️ Como usar

Uso básico:

```bash
python shadowsub.py -t example.com -w wordlist.txt
```

Com threads personalizadas (mais rápido):

```bash
python shadowsub.py -t example.com -w wordlist.txt --threads 100
```

---

## 📄 Wordlist

Cria um ficheiro `wordlist.txt` com subdomínios comuns (um por linha):

```
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
```

> 💡 Podes usar wordlists maiores como a [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS) para resultados mais abrangentes.

---

## 📸 Exemplo de Output

```
===========================================
       ShadowSub - Subdomain Finder
       Author: Mr Joker
===========================================
Target: example.com | Wordlist: wordlist.txt

[FOUND] http://admin.example.com   (192.168.1.1)
[FOUND] https://api.example.com    (192.168.1.2)
[FOUND] https://dev.example.com    (192.168.1.3)

[##############################] 100.0%

[+] 3 subdomínios encontrados
[+] Output guardado em subdomains.txt e subdomains.json
===========================================
```

---

## 📁 Ficheiros de Output

| Ficheiro | Formato | Uso |
|---|---|---|
| `subdomains.txt` | Texto simples | Input direto para ShadowProbe |
| `subdomains.json` | JSON estruturado | Automação e scripts |

---

## ⚠️ Disclaimer

> Esta ferramenta foi desenvolvida **apenas para fins educacionais e testes em sistemas autorizados**.  
> O uso indevido é da **inteira responsabilidade do utilizador**.  
> Nunca uses esta ferramenta em sistemas sem autorização explícita.

---

## 👨‍💻 Autor

**Mr Joker**  
🔗 [github.com/mrjoker-web](https://github.com/mrjoker-web)  
🔒 Cybersecurity Enthusiast | Pentesting Tools Developer
