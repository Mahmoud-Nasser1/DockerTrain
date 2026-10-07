# 🚀 Multi-Container Web Application (Flask + Redis + PostgreSQL)

A lightweight, production-ready multi-container architecture built with **Docker** and **Docker Compose**. This project demonstrates how to connect a Python Flask web application with a Redis in-memory cache and a PostgreSQL persistent database, complete with Live Reloading for local development.

---

## 🏗️ Tech Stack & Architecture

* **Web Application:** Python (Flask)
* **Caching Layer:** Redis (In-memory data store for fast hit counting)
* **Database:** PostgreSQL (Persistent relational database)
* **Containerization:** Docker & Docker Compose

---

## ✨ Features

* **Auto-Discovery:** Services communicate seamlessly using Docker Compose internal networking.
* **Data Persistence:** PostgreSQL data is preserved using named Docker Volumes.
* **Live Reloading:** Code changes in `app.py` reflect instantly via Docker Bind Mounts.

---

## 🚀 How to Run

### Prerequisites

Make sure you have installed:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with Docker Compose enabled)

### Step-by-Step Execution

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. **Build and start the containers:**

```bash
docker compose up -d --build
```

3. **Open the application:**

Open your browser and navigate to:

```text
http://localhost:5000/
```
