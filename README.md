# Sentinel Edge

> **Multi-Modal Edge AI Security Platform**  |  CCTV + Acoustic + LLM SITREP  |  8-Week PoC

![Build](https://img.shields.io/github/actions/workflow/status/Ilhanemreadak/sentinel-edge/build.yml?branch=main)  ![License](https://img.shields.io/github/license/Ilhanemreadak/sentinel-edge)

---

## ✨ Project Summary

Sentinel Edge is a plug-and-play solution designed to **empower security teams** at forward operating bases, border checkpoints, and sensitive installations. By integrating:

1. **Multi-spectral Vision** (optical + infrared),
2. **Acoustic Event Detection** (gunshots, explosions, drone rotors),
3. **Sensor Fusion & Tracking** across modalities,
4. **Low-Latency Edge Inference** on Jetson/ARM,
5. **LLM-Powered SITREP Generation**,

—Sentinel Edge transforms raw sensor feeds into **actionable, NATO-style Situation Reports** in real time. This PoC platform demonstrates a robust, scalable architecture capable of adapting to diverse field requirements.

<p align="center"><img src="docs/architecture.svg" width="650" alt="High-Level Architecture"></p>

---

## 🚀 Key Features

1. **Real-Time Object Detection**

   * Supports both day and IR-enabled night vision.
   * Detects personnel, ground vehicles, drones, maritime craft.
   * Leverages YOLO-v8m fine-tuned on defense datasets.

2. **Acoustic Event Classification**

   * Classifies gunshots, explosions, rotor noise, engine sounds.
   * Uses PANNs/Wav2Vec2 for sub-second inference.
   * Triggers alerts when anomalous audio is detected.

3. **Sensor Fusion & Geolocation**

   * Correlates feeds from CCTV, microphones, ADS-B/AIS.
   * Tracks targets across sensors; outputs merged time-series.
   * Optional geofencing: define zones of interest or exclusion.

4. **LLM-Based SITREP Generator**

   * Llama-3 Instruct fine-tuned to NATO STANAG style.
   * Summarizes prioritized threats, timestamps, and metadata.
   * Outputs in JSON, plain text, and PDF report formats.

5. **Cross-Platform Tactical UI**

   * .NET MAUI desktop and tablet app.
   * Live video feed, heatmap overlay, geospatial layers.
   * PDF export and slide deck generation.

6. **Edge-to-Core Scalability**

   * Edge nodes run C++/PyTorch containers for inference.
   * Kafka for durable, high-throughput event streaming.
   * FastAPI + TimescaleDB at core; optional k3s for production.

---

## 🛠️ Quick Start (Development)

### Prerequisites

* Docker Engine & Docker Compose v2
* Python 3.11
* Git

### 1. Clone the Repository

```bash
$ git clone https://github.com/Ilhanemreadak/sentinel-edge.git
$ cd sentinel-edge
```

### 2. Start Core Services

```bash
$ docker compose up --build -d
```

* **Kafka**, **Zookeeper**, **TimescaleDB + PostGIS**, **FastAPI** containers will launch.
* Use `docker compose logs -f` to monitor startup.

### 3. Create Kafka Topic

```bash
$ docker exec -it sentinel-edge-kafka-1 \
    kafka-topics.sh --bootstrap-server localhost:9092 \
    --create --topic hdfs-traces --partitions 3 --replication-factor 1
```

### 4. Setup Python Virtual Environment

```bash
$ cd backend
$ python -m venv .venv
$ source .venv/bin/activate         # macOS/Linux
$ .\.venv\Scripts\Activate.ps1    # Windows PowerShell
```

### 5. Install Dependencies & Launch Producer

```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt   # installs aiokafka, asyncpg, FastAPI, etc.
$ python infra/kafka/producer.py     # generates mock events every 2s
```

### 6. Start Consumer to Ingest into DB

```bash
$ python infra/kafka/consumer.py     # reads from Kafka, writes to TimescaleDB
```

### 7. Run the API Server

```bash
$ uvicorn main:app --reload           # rest API at http://127.0.0.1:8000
```

### 8. Verify Health Endpoint

```bash
$ curl http://127.0.0.1:8000/api/health
{"status":"ok"}
```

### 9. Fetch Recent Anomalies

```bash
$ curl "http://127.0.0.1:8000/api/anomalies?limit=5"
# Returns JSON array of latest detected events
```

> **Tip:** On NVIDIA-enabled hosts, enable GPU support by adding `--gpus all` to `docker compose run` commands.

---

## 📂 Repository Structure

```text
edge/                   C++ RTSP inference node with Dockerfile
backend/                FastAPI app + Kafka producer & consumer
 ├─ infra/              Dockerfiles, entrypoint scripts
 ├─ kafka/              Producer & consumer scripts
 ├─ app/                FastAPI code, routers, schemas, models
 └─ requirements.txt    Python dependencies
ui/                     .NET MAUI client (XAML + C#)
models/                 Pretrained model weights & audio checkpoints
charts/                 Helm charts & k3s manifests for production
docs/                   Architecture diagrams, API specs, slides
```

---

For the detailed 8-week roadmap, see [roadmap.md](roadmap.md). For architectural insights, view \[docs/architecture.svg].

---

Happy hacking and stay secure! 🚀

---

## 🤝 Contributing

Pull requests are welcome! Please sign the CLA bot on your first PR. For major changes, open a discussion first to propose your idea.

1. Fork the repository and create a feature branch targeting `develop`.
2. Write clear, focused commits and ensure all code passes `pre-commit` checks (e.g., `flake8`, `clang-format`, `dotnet format`).
3. Submit a pull request with a descriptive title and summary. One ✔️ review plus green CI is required for merge.

---

## 📜 License

* **Source Code:** [Apache License 2.0](LICENSE)
* **Model Weights & Checkpoints:** [OpenRAIL-M v1.3](models/LICENSE_MODEL)

> Export regulations may apply. End users are responsible for compliance with applicable laws.

---

## 📧 Contact

| Role         | Name            | Email                                                     |
| ------------ | --------------- | --------------------------------------------------------- |
| Project Lead | İlhan Emre ADAK | [dev.adak.ie@outlook.com](mailto:dev.adak.ie@outlook.com) |
| AI Engineer  | İlhan Emre ADAK | [dev.adak.ie@outlook.com](mailto:dev.adak.ie@outlook.com) |
| UI Engineer  | —               | —                                                         |

Feel free to reach out for collaboration or sponsorship opportunities.
