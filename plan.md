# plan.md

## Sentinel Edge — Comprehensive Project Plan (v1.0)

> **Scope:** 8‑week delivery of an end‑to‑end, multi‑modal security prototype for forward bases & critical facilities. Incorporates Edge AI (vision + audio), LLM summarisation, real‑time data fusion, and a cross‑platform tactical UI.

---

### 1 │ Project Overview

|                        |                                                                                                                         |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Objective**          | Detect intrusions (person, vehicle, drone, vessel) and acoustic anomalies, then auto‑generate NATO‑STANAG‑like SITREPs. |
| **Users**              | Security operators, patrol commanders, facility managers.                                                               |
| **Pain Points Solved** | CCTV overload, manual log writing, delayed response; lack of sensor fusion.                                             |
| **Success Metrics**    | <150 ms video latency; ≥92 % object‑detection AP50; SITREP draft ⩽10 s after event; MVP demo in 8 weeks.                |

---

### 2 │ Hugging Face Task Map

| #     | HF Task                         | Usage in Sentinel Edge                   | Candidate Model              | Fine‑Tune?                         |
| ----- | ------------------------------- | ---------------------------------------- | ---------------------------- | ---------------------------------- |
| 🎥 1  | Object Detection                | IR/night & day cameras                   | YOLO‑v8m                     | ✓, 5‑class custom set              |
| 🔉 2  | Audio Classification            | Drone, gunshot, explosion, engine        | PANNs CNN14 or Wav2Vec2‑base | ✓ on UrbanSound8K + gunshot corpus |
| 📝 3  | Text Generation / Summarisation | Event → NATO SITREP paragraph            | Llama‑3 8B Instruct          | Prompt‑tuned                       |
| 🏷️ 4 | Zero‑Shot Classification        | Ad‑hoc threat labels ("loitering drone") | BGE‑m3                       | None                               |
| 📊 5  | Time‑Series Forecast            | Alarm heat; patrol route opt.            | Informer                     | Optional                           |

---

### 3 │ Technology Stack

| Layer             | Tech                                   | Rationale                             |
| ----------------- | -------------------------------------- | ------------------------------------- |
| **Edge Node**     | Jetson Orin Nano; C++ 17 + LibTorch    | 30 FPS inferencing, GPIO triggers.    |
| **Model Serving** | PyTorch 2.6; Ultralytics 8             | Quantisation & on‑device export.      |
| **Backend Core**  | Python 3.11; FastAPI; Kafka (Redpanda) | Fast REST & WS, event stream.         |
| **Data Lake**     | TimescaleDB + PostGIS                  | Spatio‑temporal queries.              |
| **LLM Service**   | HF Transformers + vLLM; GPU T4         | High‑throughput prompt generation.    |
| **Dashboard**     | C# .NET MAUI + gRPC                    | Windows/Android tablets; map widgets. |
| **DevOps**        | Docker Compose → k3s (ARM + x86)       | Single‑node dev, edge cluster prod.   |
| **Observability** | Grafana + Prometheus + Loki            | Metrics, logs, alert rules.           |

---

### 4 │ System Architecture

```
┌──── Edge Node ─────────┐     RTSP  ┌──────────── Core ───────────┐
│ Camera / Mic / ADS‑B   ├──────────►│  Kafka  │  FastAPI Fusion    │
│  C++ Infer / GStreamer │   PCM     └──────────┬──────────────────┘
└────────────────────────┘                      │WS / REST
      ▲  gRPC                                    │
      │                                         ▼
┌──────────── UI Client ───────────┐   TimescaleDB/PostGIS
│ .NET MAUI  • live video          │
│ map overlay • PDF export         │
└──────────────────────────────────┘
```

* **Horizontal Scaling:** additional Edge pods publish to topic `edge.events.*`; Core pods autoscale via KEDA.
* **Failover:** Edge caches events if broker unavailable (local SQLite). Load‑balancer (Traefik) handles UI.

---

### 5 │ External Data

| Source                    | Purpose                   | Endpoint                  |
| ------------------------- | ------------------------- | ------------------------- |
| OpenSky Network           | Drone vs ADS‑B mismatch   | `api.opensky-network.org` |
| MarineTraffic (AIS)       | Harbour intrusion         | REST v2 (optional)        |
| UrbanSound8K, ShotSpotter | Audio fine‑tune sets      | HF Datasets               |
| Sentinel‑2 / LandSat      | Future thermal/IR fusion  | AWS OpenData S3           |
| OpenWeather OneCall       | Visibility & IR heuristic | `api.openweathermap.org`  |

---

### 6 │ Work Breakdown Structure (WBS)

1. **Edge Acquisition**
   1.1 RTSP pipeline (GStreamer)
   1.2 YOLOv8 quantise + deploy (.engine)
   1.3 Latency benchmark script
2. **Backend Skeleton**
   2.1 Kafka topic schema (Avro) `edge.events`
   2.2 FastAPI boilerplate (`/events`, `/health`)
3. **Audio Pipeline**
   3.1 Dataset curation
   3.2 Transfer‑learning PANNs
   3.3 GRPC micro‑service (`/audio`)
4. **LLM SITREP Service**
   4.1 Prompt template + STANAG JSON
   4.2 vLLM deployment & load‑test
5. **UI Dashboard**
   5.1 gRPC client stub
   5.2 Mapbox overlay w/ heat layer
6. **Report Generator**
   6.1 Jinja2 → HTML → WeasyPrint
7. **Integration & k3s**
   7.1 Helm chart per service
   7.2 GPU node‑selector & tolerations
8. **Security & Compliance**
   8.1 SBOM (Syft)
   8.2 Apache 2.0 + OpenRAIL‑M license files

---

### 7 │ 8‑Week Sprint Schedule

| Sprint | Calendar        | Epics                        | Key Deliverables                             |
| -----: | --------------- | ---------------------------- | -------------------------------------------- |
|  **1** | 7 Jul – 20 Jul  | Edge RTSP · Backend Skeleton | Running object detect demo; `/health` up     |
|  **2** | 21 Jul – 3 Aug  | Audio Pipeline · Fusion v1   | Gunshot/drone classifier; Avro event merge   |
|  **3** | 4 Aug – 17 Aug  | LLM SITREP · UI v1           | SITREP draft API; MAUI video stream          |
|  **4** | 18 Aug – 31 Aug | k3s Deploy · E2E Demo        | Helm stack on 3‑node cluster; demo recording |

---

### 8 │ Risk Register (Top 5)

| ID | Risk                  | Likelihood | Impact | Mitigation                               |
| -- | --------------------- | ---------- | ------ | ---------------------------------------- |
| R1 | Jetson supply delay   | M          | H      | Keep Pi CM4 fallback image               |
| R2 | LLM latency >10 s     | M          | M      | Enable GPU multi‑query (vLLM)            |
| R3 | Kafka topic overload  | L          | M      | Partition by `site_id`, enable retention |
| R4 | Audio false‑positives | H          | M      | Ensemble w/ temporal smoothing           |
| R5 | Export‑control regs   | M          | H      | Add OpenRAIL misuse clauses, ITAR note   |

---

### 9 │ License & Compliance

* **Source code:** Apache License 2.0
* **Model weights:** OpenRAIL‑M v1.3
  *Prohibits illegal surveillance & unlawful weaponisation.*
* **NOTICE** file lists third‑party attributions (Ultralytics, PANNs, Mapbox SDK).

---

### 10 │ Acceptance Criteria

* [ ] E2E test triggers CCTV + gunshot → single SITREP entry within 12 s.
* [ ] Average object detection AP50 ≥ 92 % on test set.
* [ ] UI heatmap refresh <1 s websockets.
* [ ] Helm deploy on ARM & x86 with same manifest.

---

### 11 │ Deliverables

1. **Docker registry** with tagged images `edge`, `core`, `ui`, `llm`.
2. **GitHub repo** (`sentinel-edge`): code + CI/CD + SBOM.
3. **Demo video** (≤3 min) showing live detection + SITREP.
4. **Final report PDF** detailing metrics & lessons learned.

---

*Last updated: 3 Jul 2025  ✍️ ChatGPT‑assisted*
