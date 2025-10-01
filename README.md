# RampRabbit
## Overview

RampRabbit is a multi-page Streamlit web application designed to showcase company partners, market information, and key insights in a visually appealing, interactive dashboard. The company name
is Rabbit and the main focus is upon the assistant CorpoRabbit, which is a RAG based implementation chatbot focused upon solving queries of new employees regarding leave policies, more information related 
to Rabbit company, etc;
The application allows users to:

- View partner companies with logos in a column layout.
- Access market presence and company highlights.
- Explore a responsive UI built with Streamlit.
- Chat with CorpoRabbit regarding any HR issues of Rabbit company.

This project is structured to be scalable, making it easy to add new pages, partners, and market data.

---

## Project Structure
RampRabbit/
│── rabbit_main.py # Main Streamlit app
│── pages/ # Multi-page apps or submodules
│ ├── contact.py
│ └── more_info.py
│── images/ # Logos and other images
│ ├── zepto.png
│ ├── alpha.png
│ ├── omega.png
│ └── delta.png
│── requirements.txt # Python dependencies
│── .gitignore
│── README.md

---

## Features
1. CorpoRabbit:
   - The main HR RAG based assistant of company Rabbit.
   - Helps you to solve any queries related to information upon leaves, contacts in the company and whom to inform regarding any query,etc;
2. Contacts:
   - Contacts of the owner of this project(sample).
3. More information:
   - Sample additional information related to the organisation Rabbit.
   - Business partners(sample) of Rabbit.
---
## Installation
Clone the repository:
```bash
git clone https://github.com/RJDEVMAN/RampRabbit.git
cd RampRabbit
