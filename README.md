# 🤖 AI-Powered Interview Question Creator

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

An intelligent tool designed to streamline the interview preparation process by automatically generating questions and answers from PDF documents. Ideal for recruiters, educators, and students.

---

### 🌟 Overview

The **AI Interview Question Creator** automates the tedious task of creating interview materials. By simply uploading a PDF document—such as a resume, job description, or study guide—the application leverages a Large Language Model (LLM) to extract key information and generate a comprehensive set of relevant questions and their corresponding answers.

![UI Placeholder](https://via.placeholder.com/800x400.png?text=Application+Screenshot+Here)

---

## ✨ Key Features

* **📄 Smart PDF Parsing**: Effortlessly extracts text and context from any uploaded PDF document.
* **🧠 AI-Powered Generation**: Utilizes advanced AI to generate insightful, context-aware questions and detailed answers.
* **💾 Multiple Export Options**: Download the generated Q&A pairs in user-friendly **CSV** or styled **HTML** formats.
* **🚀 Local Deployment**: Runs on a lightweight and fast local server powered by **FastAPI**.
* **🌐 Public Sharing (Optional)**: Easily share a live version of your local app with anyone, anywhere, using **ngrok**.
* **💻 Intuitive Web Interface**: A clean and simple UI for a smooth user experience.

---

## 🛠️ Technology Stack

* **Backend**: Python, FastAPI
* **AI/ML**: Google Generative AI (or other LLM pipelines)
* **PDF Processing**: PyPDF2
* **Environment**: Conda
* **Frontend**: HTML, CSS (served via FastAPI)

---

## 📂 Project Structure

Interview-Question-Creator/
│
├── app.py                  # Main FastAPI application logic and endpoints
├── requirements.txt        # List of Python dependencies for pip
├── README.md               # You are here!
│
├── src/
│   └── helper.py           # Core logic for PDF parsing and LLM interaction
│
├── static/
│   ├── docs/               # Directory for sample PDF files
│   └── output/             # Default location for generated CSV/HTML files
│
├── templates/
│   └── index.html          # Frontend HTML template
│
└── .env                    # Environment variables (e.g., API keys)


---

## ⚙️ Installation and Setup

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites

* Python 3.10 or higher
* [Conda](https://docs.conda.io/en/latest/miniconda.html) package manager

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/Interview-Question-Creator.git](https://github.com/your-username/Interview-Question-Creator.git)
cd Interview-Question-Creator
```

### 3. Create and Activate Conda Environment
This will create an isolated environment for the project's dependencies.


# Create a new conda environment named 'interview'
```bash
conda create -n interview python=3.10 -y

# Activate the environment
conda activate interview
```
4. Install Dependencies
Install all the required Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
5. Set Up Environment Variables
You'll need an API key from an LLM provider (e.g., Google AI Studio).

Create a file named .env in the root directory.

Add your API key to this file:

Code snippet

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
▶️ Running the Application
Once the setup is complete, you can start the FastAPI server.

Bash

python app.py
The application will be accessible in your web browser at:
http://127.0.0.1:8080

📝 How to Use
Navigate to the Web Interface: Open http://127.0.0.1:8080 in your browser.

Upload a PDF: Click the "Choose File" button and select a PDF document from your local machine.

Generate Q&A: Click the "Analyze" button to start the generation process. The AI will parse the document and create the questions and answers.

Download Results: Once processing is complete, download links for CSV and HTML files will appear.

View Output:

Open the CSV file in any spreadsheet program (like Excel or Google Sheets).

Open the HTML file in a web browser to view a neatly formatted table.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or want to fix a bug, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some amazing feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a Pull Request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.
