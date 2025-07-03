# Sentinel Edge — Detailed Roadmap (July → August 2025)

> **Goal:** Deliver a demo‑ready, multi‑modal security system (Edge AI + Audio + LLM summarisation + Tactical UI) in **8 weeks** with a team of ≤ 3 engineers.

---

## 0 │ Milestone Ladder

| ID     | Date (2025) | Description                     | Exit Criteria                                                                  |
| ------ | ----------- | ------------------------------- | ------------------------------------------------------------------------------ |
| **M0** | 07 Jul      | Kick‑off & infrastructure ready | Repo + CI/CD skeleton; Trello board live; licences added.                      |
| **M1** | 14 Jul      | **Edge PoC**                    | Jetson runs YOLOv8m @ ≥ 10 FPS on RTSP stream.                                 |
| **M2** | 28 Jul      | **Fusion v0**                   | FastAPI receives Edge + Audio events → Kafka; Avro schema settled.             |
| **M3** | 11 Aug      | **LLM SITREP v1**               | Llama‑3 prompts generate STANAG‑style reports with ≥ 0.8 ROUGE‑L vs reference. |
| **M4** | 18 Aug      | **UI Alpha**                    | .NET MAUI shows live video, map overlay, real‑time alarm list.                 |
| **M5** | 25 Aug      | **OpenSky integrated**          | ADS‑B feed fused; geo‑alarms trigger on intrusion path.                        |
| **M6** | 31 Aug      | **System Demo**                 | End‑to‑end scenario runs 20 min without crash; PDF SITREP auto‑emailed.        |

---

## 1 │ 8‑Week Timeline (Sprint = 2 weeks)

| Week  | Dates           | Workstream                           | Key Tasks                                              | Deliverables                      |
| ----- | --------------- | ------------------------------------ | ------------------------------------------------------ | --------------------------------- |
| **1** | 07 – 13 Jul     | Edge                                 | • GStreamer capture<br>• YOLOv8m bench                 | Edge Docker image, latency report |
|       |                 | Ops                                  | • CI pipeline (edge)                                   | GitHub Action badge               |
| **2** | 14 – 20 Jul     | Backend                              | • FastAPI skeleton<br>• Kafka docker‑compose           | API spec v0.1                     |
|       | Audio           | • Collect UrbanSound8K, Gunshot      | Dataset folder structure                               |                                   |
| **3** | 21 – 27 Jul     | Audio                                | • Fine‑tune PANNs; on‑device test                      | audio\_model.onnx                 |
|       | Fusion          | • Avro schema v1<br>• Kafka consumer | Event JSON samples                                     |                                   |
| **4** | 28 Jul – 03 Aug | Fusion                               | • Track correlation logic                              | README fusion.md                  |
|       | DevOps          | • Edge metrics → Prometheus          | Grafana dashboard link                                 |                                   |
| **5** | 04 – 10 Aug     | LLM                                  | • Prompt design<br>• Fine‑tune Llama‑3                 | sitrep\_prompt.json, model ckpt   |
|       | Reporting       | • ReportLab PDF template             | sitrep\_template.pdf                                   |                                   |
| **6** | 11 – 17 Aug     | UI                                   | • .NET MAUI live video view<br>• WebSocket alarm panel | UI preview gif                    |
|       | Testing         | • End‑to‑end latency test            | latency\_sheet.csv                                     |                                   |
| **7** | 18 – 24 Aug     | External                             | • OpenSky REST fetch<br>• Geofence alerts              | opensky\_module.py                |
|       | UI              | • Heatmap overlay                    | heatmap\_demo.mp4                                      |                                   |
| **8** | 25 – 31 Aug     | DevOps                               | • k3s Helm charts<br>• Load test > 200 eps             | helm\_release.yaml                |
|       | Demo            | • Scenario script, video record      | demo\_video.mp4                                        |                                   |

---

## 2 │ Workstream Breakdown

### 2.1 Edge AI

* **E‑01** RTSP capture & decode (GStreamer) *(W1)*
* **E‑02** YOLOv8m inferencer C++ wrapper *(W1–2)*
* **E‑03** FPS + Mem telemetry → Prometheus *(W4)*

### 2.2 Audio AI

* **A‑01** Dataset curation *(W2)*
* **A‑02** PANNs fine‑tune & quantisation *(W3)*
* **A‑03** On‑device inference latency test *(W3)*

### 2.3 Backend / Fusion

* **B‑01** FastAPI + Kafka skeleton *(W2)*
* **B‑02** Avro event schema *(W3)*
* **B‑03** Correlation & dedup logic *(W4)*

### 2.4 LLM & Reporting

* **L‑01** Data curation: sample SITREPs *(W4)*
* **L‑02** Prompt engineering *(W5)*
* **L‑03** Fine‑tune & eval *(W5)*
* **L‑04** PDF generator *(W5–6)*

### 2.5 UI

* **U‑01** Project bootstrap (.NET MAUI) *(W5)*
* **U‑02** Live stream component *(W6)*
* **U‑03** Map + heatmap overlay *(W7)*
* **U‑04** PDF export button *(W6–7)*

### 2.6 DevOps

* **D‑01** GitHub Actions (edge, backend) *(W1–2)*
* **D‑02** Observability stack (Prom + Grafana) *(W4)*
* **D‑03** Helm charts + k3s deploy *(W8)*

---

## 3 │ Dependencies & Risks

| Risk ID | Description            | Impact | Mitigation                                      |
| ------- | ---------------------- | ------ | ----------------------------------------------- |
| **R1**  | Jetson Orin shortage   | High   | Order HW week 0; keep x86 fallback container.   |
| **R2**  | Llama‑3 fine‑tune time | Medium | Start HF PEFT early; use quantised 4‑bit.       |
| **R3**  | OpenSky rate limits    | Low    | Cache requests; implement exponential back‑off. |

---

## 4 │ Acceptance Criteria

1. **Detection Accuracy:** mAP ≥ 0.55 on custom validation set.
2. **Audio Recall:** ≥ 0.80 for gunshot & drone prop classes.
3. **End‑to‑End Latency:** ≤ 1.0 s camera → UI marker.
4. **SITREP Quality:** Human SME rating ≥ 4 / 5.
5. **Stability:** 30‑min burn‑in without crash or mem‑leak.

---

## 5 │ Deliverables

* Source code (Apache 2.0) + model weights (OpenRAIL‑M)
* Docker images: edge‑node, backend, fusion, ui
* Helm chart & k3s manifest
* PDF user guide + API spec (OpenAPI 3.1)
* Demo video & slide deck

---

*Document generated 03‑Jul‑2025.*
