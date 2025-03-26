# 🚀 End-to-End Context Testing System for Financial Applications

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Financial applications require rigorous testing to ensure compliance, security, and accuracy. Manually creating test cases is time-consuming and prone to errors. This project automates test case generation and execution using an AI-driven approach with a T5-based model, Flask, JIRA integration, and Selenium.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
Testing financial applications manually is inefficient and often incomplete. This project was inspired by the need for a scalable and intelligent testing system that ensures financial transactions are processed correctly while reducing manual effort.

## ⚙️ What It Does
- **AI-Powered Test Case Generation**: Uses a T5-based model to generate test cases from feature descriptions.
- **JIRA Integration**: Fetches feature descriptions directly from JIRA.
- **Excel-Based Test Case Management**: Stores and tracks test cases with execution status.
- **Automated Test Execution**: Uses Selenium to execute test cases on a sample financial application.
- **Real-Time Test Monitoring**: Updates test results in the Excel sheet automatically.

## 🛠️ How We Built It
- **Trained a T5 Model** on sample financial test cases to generate context-aware test cases.
- **Developed a Flask Web App** to interact with the AI model and fetch feature descriptions.
- **Integrated JIRA API** for seamless test case generation from issue descriptions.
- **Used Pandas with Excel** to store and track test cases.
- **Automated Execution with Selenium**, logging into the sample financial application to verify transactions.

## 🚧 Challenges We Faced
- **Fine-tuning the T5 Model** to generate relevant and meaningful test cases.
- **JIRA API Integration** and handling different formats of feature descriptions.
- **Ensuring UI & API Compatibility** for Selenium test execution.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Start the Flask server  
   ```sh
   Context_aware_test case_generator.ipynb
   ```
4. Run the Selenium test script  
   ```sh
   python TESTCASE_automantion.py
   ```

## 🏗️ Tech Stack
- **AI Model**: T5 Transformer (Hugging Face)
- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Test Case Management**: Excel (Pandas)
- **JIRA Integration**: JIRA API
- **Automation**: Selenium, Watchdog
- **Sample App**: Flask-based Transaction Fee Calculator

## 👥 Team
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)

This project streamlines financial application testing, making it faster, smarter, and more efficient! 🚀

