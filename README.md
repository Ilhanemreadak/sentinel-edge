# Sentinel Edge

> **Multi‑Modal Edge AI Security Platform**  |  CCTV + Acoustic + LLM SITREP  |  8‑week PoC

![Build](https://img.shields.io/github/actions/workflow/status/your‑org/sentinel‑edge/build.yml?branch=main)
![License](https://img.shields.io/github/license/your‑org/sentinel‑edge)

---

## ✨ Project Summary

Sentinel Edge is a plug‑and‑play software stack that fuses **computer vision, acoustic event detection, low‑latency edge inference, and large‑language‑model summarisation** to generate NATO‑style situation reports (SITREPs) for forward bases, border posts, and critical infrastructure.

<p align="center"><img src="docs/architecture.svg" width="650" alt="High‑Level Architecture"></p>

---

## 🚀 Key Features

* **Real‑Time Object Detection** – Day/night cameras, IR capable; humans, vehicles, drones.
* **Acoustic Event Classification** – Gunshot, explosion, drone rotor, engine noise.
* **Sensor Fusion & Tracking** – Correlates vision + audio + ADS‑B/AIS feeds.
* **LLM SITREP Generator** – Llama‑3 fine‑tuned to output concise, priority‑sorted reports.
* **Cross‑Platform Tactical UI** – .NET MAUI desktop/tablet app; live video, map, PDF export.
* **Edge‑to‑Core Scalability** – Jetson Orin nodes forward events to Kafka↔FastAPI core.

---

## 🏗️ Tech Stack

| Layer           | Tech                                                        |
| --------------- | ----------------------------------------------------------- |
|  Edge Inference | **C++**, PyTorch 2.6, YOLO‑v8m                              |
| Backend API     | **Python 3.11**, FastAPI, Kafka                             |
| Data Lake       | TimescaleDB + PostGIS                                       |
| UI              | **C# .NET MAUI**, gRPC                                      |
| DevOps          | Docker Compose → k3s (Helm)                                 |
| License         | Code: **Apache 2.0**  •  Model Weights: **OpenRAIL‑M v1.3** |

---

## 🛠️ Quick Start (Dev)

```bash
# 1. Clone
$ git clone https://github.com/your‑org/sentinel‑edge.git && cd sentinel‑edge

# 2. Build & run services (CPU)
$ docker compose up ‑d backend edge ui db kafka

# 3. Tail logs
$ docker compose logs -f edge

# 4. Open UI
$ open http://localhost:8080   # or ctrl‑click URL on Windows
```

> **GPU / Jetson:** see [`edge/README.md`](edge/README.md) for CUDA base image & Jetson deploy notes.

---

## 📂 Repository Layout

```
├─ edge/               # C++ inference node
│  ├─ src/
│  └─ Dockerfile
├─ backend/            # FastAPI + Kafka consumer/producer
│  ├─ app/
│  └─ requirements.txt
├─ ui/                 # .NET MAUI client
├─ models/             # YOLO weights, audio checkpoints (OpenRAIL licensed)
├─ charts/             # Helm / k3s manifests
└─ docs/               # Architecture diagrams, spec sheets
```

---

## 🗺️ Roadmap

See **[`roadmap.md`](roadmap.md)** for the 8‑week milestone plan.

Key upcoming milestones:

1. **M1 – Edge RTSP Pipeline (07 Jul)**
2. **M2 – FastAPI + Kafka Skeleton (14 Jul)**
3. **M3 – Audio Pipeline PoC (28 Jul)**
4. **M4 – UI Alpha + SITREP LLM (11 Aug)**
5. **M5 – End‑to‑End Demo (30 Aug)**

---

## 🤝 Contributing

Pull requests are welcome! Please sign the CLA bot on your first PR.
For major changes, open a discussion first to propose your idea.

1. Fork → Feature branch → PR targeting `develop`.
2. Ensure `pre‑commit` passes (`flake8`, `clang‑format`, `dotnet format`).
3. One ✔ review + green CI required for merge.

---

## 📜 License

* **Source Code:** [Apache License 2.0](LICENSE)
* **Model Weights & Checkpoints:** [OpenRAIL‑M v1.3](models/LICENSE_MODEL)

> "Export regulations may apply. End‑user is responsible for compliance with applicable laws."
> © 2025 Your Name / Your Org

---

## 📧 Contact

| Role         | Name  | E‑mail                                    |
| ------------ | ----- | ----------------------------------------- |
| Project Lead | İlhan Emre ADAK | [dev.adak.ie@outlook.com](mailto:dev.adak.ie@outlook.com) |
| AI Engineer  | İlhan Emre ADAK | [dev.adak.ie@outlook.com](mailto:dev.adak.ie@outlook.com) |
| UI Engineer  | —     | —                                         |

Feel free to reach out for collaboration or sponsorship opportunities.
