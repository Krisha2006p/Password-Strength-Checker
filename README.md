# 🔐 Password Strength Checker

A web-based application that evaluates password strength using Information Entropy mathematics rather than simple pattern matching. Built with Python (Flask) and a custom styling interface.

---

## 🚀 Features

*   **Entropy-Based Calculation:** Calculates the raw mathematical entropy (bits) of a password based on character variety and length.
*   **Real-World Crack Time Estimation:** Estimates how long it would take a "Strong Attacker" (capable of 100 billion guesses/second) to brute-force the password.
*   **Input Validation:** Strictly enforces standard ASCII characters (Letters, Numbers, Symbols) to ensure data integrity.
*   **Responsive UI:** A dark-themed, minimalist interface styled with CSS.

---

## 🧠 The Logic: How It Works

Unlike simple checkers that just look for "one uppercase letter," this tool uses the **Entropy** formula to determine the sheer mathematical difficulty of guessing the password.

### 1. The Formula
The entropy $E$ is calculated as:

$$E = L \times \log_2(R)$$

Where:
*   $L$ = **Length** of the password.
*   $R$ = **Pool Size** (The variety of characters used).

### 2. Pool Size ($R$) Determination
The application dynamically adjusts the pool size based on the character types detected:
*   **Lowercase only:** Pool = 26
*   **Uppercase only:** Pool = 26
*   **Numbers:** Pool = 10
*   **Symbols:** Pool ≈ 32

*Example:* If a password uses lowercase + numbers, the pool becomes $26 + 10 = 36$.

### 3. Crack Time Calculation
The tool assumes a **"Strong Attacker"** scenario (e.g., a GPU cluster or botnet) capable of making **100 Billion ($10^{11}$)** guesses per second.

$$ \text{Seconds to Crack} = \frac{2^E}{100,000,000,000} $$

---

## 🛠️ Tech Stack

*   **Backend:** Python 3, Flask
*   **Frontend:** HTML5, CSS3 (Custom responsive design)
*   **Math:** Python `math` library for logarithmic calculations

---
## 📂 Project Structure

```text
password-strength-checker/
├── static/
│   └── style.css       # Dark mode styling and layout
├── templates/
│   └── index.html      # Main interface
├── .gitignore          # Specifies files to exclude from Git
├── app.py              # Flask routes and entry point
├── logic.py            # Core entropy and time conversion logic
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---
## 🛠️ Installation & Run

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Krisha2006p/Password-Strength-Checker.git
    ```

2.  **Navigate to the directory**
    ```bash
    cd Password-Strength-Checker
    ```

3. **Create & Activate Virtual Environment (Optional but recommended):**

    **Create the virtual environment:**
    ```bash
    python -m venv venv
    ```

    **Activate it:**
   * Windows:
       ```bash
       venv\Scripts\activate
       # OR if using PowerShell:
       .\venv\Scripts\Activate.ps1
       ```
   * Mac/Linux:
       ```bash
       source venv/bin/activate
       ```
    
4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask app**
    ```bash
    python app.py
    ```

6. **Open in browser**
    ```
    http://127.0.0.1:5000
    ```

