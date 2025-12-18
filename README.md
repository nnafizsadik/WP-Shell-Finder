# 🛡️ WP Shell Finder (Educational Project)

**WP Shell Finder** is a **Python-based WordPress path scanner** designed for **cybersecurity research, learning, and educational purposes only**.
It scans a list of target websites against predefined WordPress paths and checks for a specific response keyword.

> ⚠️ This project is **NOT intended for illegal use**.
> Use it **only on systems you own or have explicit permission to test**.

---

## ✨ Features

* 🚀 Multi-threaded scanning (fast & efficient)
* 🧩 Custom **User-Agent** support
* 🛠️ Customizable **PATHS** list
* 📟 Terminal output for **FOUND / NOT FOUND**
* 📁 Automatically saves **only FOUND results** to `found.txt`
* 🎨 Clean ASCII banner
* 📚 Includes a **free WordPress target list** (example)

---

## 🧑‍💻 Usage

```bash
python scanner.py sites.txt
```

* `sites.txt` → list of target domains (one per line)
* Results:

  * **FOUND / NOT FOUND** shown in terminal
  * **FOUND shells only** saved in `found.txt`

---

## ⚙️ Configuration

### 🔹 User-Agent (Recommended)

For a better experience and to avoid basic blocks, you can **customize or rotate the User-Agent** in the script:

```python
HEADERS = {
    "User-Agent": "Your-Custom-User-Agent-Here"
}
```

---

### 🔹 PATHS (Highly Recommended)

You can add or modify WordPress paths to improve scanning results:

```python
PATHS = [
    "/.well-known/acme-challenge/zmFM.php",
    "/wp-includes/sitemaps/providers/zmFM.php",
    "/wp-includes/pomo/zmFM.php",
    "/wp-admin/css/colors/ectoplasm/zmFM.php",
    "/wp-includes/PHPMailer//zmFM.php",
    "/wp-includes/customize/zmFM.php",
    "/wp-includes/certificates/zmFM.php",
    "/wp-includes/theme-compat/zmFM.php",
]
```

➡️ **For best results**, keep your PATHS list updated with **fresh and relevant paths**.

---

## 📂 WordPress Target List

This repository includes a **free WordPress site list** for testing and learning purposes.

> 🔁 For better accuracy and results:

* Always use a **fresh & updated WordPress list**
* Remove dead or inactive domains

---

## 📘 Educational Purpose & Disclaimer

This project is created **strictly for**:

* Cybersecurity research
* Learning how scanners work
* Understanding web security risks
* Educational demonstrations

### ❗ Disclaimer

The **owner/developer is NOT responsible** for:

* Any illegal usage
* Any damage caused by misuse
* Any actions performed without proper authorization

If you use this tool, **you are solely responsible** for your actions.

---

## 👤 Author

**Nafiz Sadik**

* GitHub: [https://github.com/nnafizsadik](https://github.com/nnafizsadik)
* Portfolio: [https://nafizsadik.me/](https://nafizsadik.me/)
* Email: [studynafizsadik@gmail.com](mailto:nafizsadik@proton.me)

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork it for learning
* 🛠️ Improve it responsibly

