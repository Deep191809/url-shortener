
# 🔗 URL Shortener

A simple and efficient web-based URL Shortener built with **Flask (Python)** and **MySQL**.

## 🚀 Features

- ✅ Shortens long URLs into concise links
- ✅ Redirects to original URLs via shortened links
- ✅ Copy-to-clipboard button for quick access
- ✅ Light/Dark mode with theme toggle and persistence
- ✅ Shows last 5 shortened URLs with pagination
- ✅ Clean and modern responsive UI

---

## 🛠️ Installation Guide (Windows / macOS)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

> Replace `your-username` with your actual GitHub username.

---

### Step 2: Install Python & Virtual Environment

- **Windows**: Install Python 3.11+ from [python.org](https://www.python.org/downloads/).
- **Mac**: Use [Homebrew](https://brew.sh/) or download Python from official site.

Then run:

```bash
python -m venv venv
```

Activate environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Setup MySQL Database

- Make sure MySQL Server is installed and running.
- Create a database named:

```sql
CREATE DATABASE url_shortener;
```

- Then create the required table:

```sql
USE url_shortener;

CREATE TABLE urls (
  id INT AUTO_INCREMENT PRIMARY KEY,
  original_url TEXT NOT NULL,
  short_id VARCHAR(10) NOT NULL UNIQUE
);
```

---

### Step 5: Setup Environment Variables

Create a `.env` file in the root directory with:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener
```

---

### Step 6: Run the Application

```bash
python app.py
```

- Open browser and go to: `http://127.0.0.1:5000/psquare_lab_iitr/`

---

## 📂 Project Structure

```
url-shortener/
├── app.py
├── db.py
├── templates/
│   └── index.html
├── .env
├── requirements.txt
└── README.md
```

---

## 📈 Future Enhancements

- Add user authentication
- Track analytics for each short link
- Add QR code generation
- Deploy the app on a cloud platform (e.g., Render, Vercel, or Heroku)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📧 Contact

**Developer:** Deep Punia  
**Email:** deeppunia2004@gmail.com  
**Project Mentor:**  Parikshit Pareek
