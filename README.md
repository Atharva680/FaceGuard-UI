# FaceGuard UI 🛡️🎥  
### Real-Time Face Detection & Event Recording System with Smart UI

FaceGuard UI is a Python-based computer vision system designed for **events, offices, classrooms, and surveillance setups**.  
It performs **real-time face detection**, **intelligent face capture**, and **long-duration video recording** with a clean and informative **live user interface (UI)**.

---

## ✨ Key Highlights

- 🎯 High-accuracy real-time face detection  
- 📸 Smart face capture with cooldown & duplicate prevention  
- 🧠 False-positive filtering (blur, size, ROI, geometry checks)  
- 🎥 Long-duration recording (3–10 hours) with session handling  
- 🖥️ Clean live UI with overlays & status indicators  
- ⚡ Optimized for real-world environments (events & crowds)

---

## 🖥️ Live UI Overview

FaceGuard UI provides a **clear, operator-friendly interface** while running.

### 🔲 Bounding Box Colors
| Color | Meaning |
|-----|--------|
| 🟩 Green | Face detected & image SAVED |
| 🟨 Yellow | Face detected but in COOLDOWN |
| 🟧 Orange | Face detected but REJECTED (blur / low quality) |
| ⬜ Gray Box | Active ROI (Region of Interest) |

---

### 📊 On-Screen Stats Panel (Top-Left)

Displays in real time:
- **Total Faces Saved**
- **Current Valid Faces**
- **Session Time (minutes & seconds)**

This allows the operator to **monitor performance without checking logs**.

---

### 🎮 Keyboard Controls

| Key | Action |
|----|-------|
| **Q** | Stop recording & exit safely |
| **R** | Toggle ROI overlay (if enabled) |

---

## 📁 Project Structure
FaceGuard-UI/
├── liveface.py # Live face detection & capture
├── record_30min_with_overlay.py # 3-hour session video recorder
├── probe_cams.py # Camera detection utility
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── rec.txt # Recording notes
├── event_faces/ # Captured face images
├── recordings/ # Recorded event videos
└── .github/ # GitHub workflows & templates

---

## ⚙️ System Requirements

### 💻 Hardware
- Webcam / USB camera / CCTV feed
- Recommended: 720p or 1080p camera

### 🧪 Software
- Python **3.8+**
- Windows / Linux / macOS

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FaceGuard-UI.git
cd FaceGuard-UI
2️⃣ Install Dependencies
pip install -r requirements.txt

🔍 Camera Check (Recommended)

Before running the main app:

python probe_cams.py


This verifies:

Available camera indexes

Supported OpenCV backends (DSHOW / MSMF)

▶️ Running the System
🔴 Start Event Recording (3-Hour Sessions)
python record_30min_with_overlay.py

What Happens:

Camera initializes with best backend

Live preview window opens

Face detection starts instantly

Faces are:

Validated

De-duplicated

Saved automatically

Video is recorded with overlays

New session starts every 3 hours automatically

🧠 Smart Face Validation Logic

FaceGuard UI avoids junk detections using:

✅ Minimum face size check

✅ Aspect ratio validation

✅ Blur detection (Laplacian variance)

✅ Brightness thresholding

✅ ROI gating (center-focused detection)

✅ Cooldown-based duplicate prevention

Result: Clean dataset, fewer false faces.

📂 Output Details
📸 Captured Faces

Saved to:

event_faces/


Format:

face_00023_20260210_143522_123.jpg

🎥 Recorded Videos

Saved to:

recordings/


Format:

event_overlay_session2_20260210_120001.mp4

⚡ Performance Notes

CPU Usage: ~15–30%

Disk: ~3GB per 3-hour session (720p @ 30 FPS)

Face Capture Speed: < 1 second per face

🧪 Best Practices

Ensure good lighting

Camera at eye level

Avoid backlight

Test for 2–3 minutes before long sessions

🚀 Use Cases

🎓 College events & seminars

🏢 Office attendance monitoring

🎤 Conferences & expos

🏫 Classrooms

🛡️ Surveillance & monitoring

📜 License

This project is released under the MIT License.
You are free to use, modify, and distribute with attribution.

🙌 Author

Developed by Atharva shinde


