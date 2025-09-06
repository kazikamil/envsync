# 🌍 envsync

A lightweight CLI tool to **manage and sync environment variables** across multiple projects and environments.  

Stop juggling `.env` files manually — switch, add, and sync your environment variables with a single command.

---

## 🚀 Features
- 🔄 **Switch** between environments instantly (`dev`, `staging`, `prod`, etc.)
- ➕ **Add** environment variables without opening editors
- 📂 **Sync** environment variables across projects or team members
- ✅ **Keep configs consistent** and portable

---

## 📦 Installation



### Local development
Clone the repo and install dependencies in editable mode:

```bash
git clone https://github.com/your-username/envsync.git
cd envsync
pip install -e .
```

---
## 🛠 Commands

### 🔄 Switch environments
```bash
envsync switch staging
```
Switches to `staging.env` instantly.

---

### ➕ Add a new variable
```bash
envsync add API_KEY=123456
```
Adds (or updates) `API_KEY` in the current environment.

---

### 📂 Sync environments
```bash
envsync sync
```
Syncs variables from `.env.local` to `.env`.



## 📚 Examples

Switch between environments:
```bash
envsync switch dev
envsync switch prod
```

Add new variables:
```bash
envsync add DATABASE_URL=postgres://user:pass@localhost:5432/db
envsync add DEBUG=True
```

Sync with another project:
```bash
envsync sync ../another-project/.env
```

---

## 📖 Project Structure
```
envsync/
│   __init__.py
│   main.py
.gitignore
LICENSE
README.md
pyproject.toml
setup.py
requirements.txt   # optional
examples/          # optional usage samples
```

---

## 🤝 Contributing

1. Fork the repo  
2. Create your feature branch (`git checkout -b feature/awesome-feature`)  
3. Commit changes (`git commit -m 'Add awesome feature'`)  
4. Push to the branch (`git push origin feature/awesome-feature`)  
5. Open a Pull Request 🎉  

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).  
