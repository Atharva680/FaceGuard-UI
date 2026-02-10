# FaceGuard UI 🛡️🎥  
### Real-Time Face Detection & Event Recording System with Smart UI

FaceGuard UI is a **Python-based computer vision system** built using OpenCV for **real-time face detection, intelligent face capture, and long-duration event video recording**.

The system is designed for **events, offices, classrooms, conferences, and surveillance environments**, providing a clean and informative **live user interface (UI)** with smart validation logic to reduce false detections.

---

## ✨ Key Features

- 🎯 Real-time face detection using OpenCV
- 📸 Automatic face image capture
- 🔁 Cooldown-based duplicate prevention
- 🧠 Smart face validation logic
- 🎥 Long-duration video recording (3-hour sessions)
- 🔄 Automatic session rollover
- 🖥️ Live UI with bounding boxes and statistics
- ⚙️ Multi-backend camera support (DSHOW / MSMF / ANY)
- 📂 Organized output folders for faces and recordings
- 🚀 Optimized for real-world usage

---

## 🖥️ Live UI Overview

The application runs with a **live preview window** showing detection results and system statistics.

### 🔲 Bounding Box Indicators

| Color | Meaning |
|------|--------|
| 🟩 Green | Face detected and image saved |
| 🟨 Yellow | Face detected but in cooldown |
| ⬛ Black Panel | Statistics overlay |

---

### 📊 On-Screen Statistics Panel

Displayed in the top-left corner:
- **Total Saved Faces**
- **Current Face Detections**
- **Elapsed Session Time**

This allows operators to monitor performance without checking logs.

---

### 🎮 Keyboard Controls

| Key | Action |
|----|-------|
| **Q** | Stop recording and exit safely |

---

## 📁 Project Structure

```

FaceGuard-UI/
├── liveface.py                      # Live face detection & capture
├── record_30min_with_overlay.py     # 3-hour session video recorder with UI
├── probe_cams.py                    # Camera detection utility
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── rec.txt                          # Recording notes
├── event_faces/                     # Captured face images
├── recordings/                      # Recorded event videos
└── .github/                         # GitHub workflows & templates

````

---

## ⚙️ System Requirements

### 💻 Hardware
- Webcam / USB camera / CCTV feed
- Recommended resolution: **720p or 1080p**

### 🧪 Software
- **Python 3.8 or higher**
- Supported OS:
  - Windows
  - Linux
  - macOS

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FaceGuard-UI.git
cd FaceGuard-UI
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔍 Camera Check (Recommended)

Before running the main application, verify camera availability:

```bash
python probe_cams.py
```

This utility checks:

* Available camera indexes
* Supported OpenCV camera backends (DSHOW / MSMF / ANY)

---

## ▶️ Running the System

### 🔴 Start Event Recording (3-Hour Sessions)

```bash
python record_30min_with_overlay.py
```

### What Happens When You Run It

1. Camera initializes using the best available backend
2. Live preview window opens
3. Face detection starts instantly
4. Each detected face is:

   * Validated
   * De-duplicated
   * Saved automatically
5. Video is recorded with overlays
6. A new recording session starts automatically every 3 hours
7. Press **Q** to stop safely

---

## 🧠 Smart Face Validation Logic

FaceGuard UI minimizes false detections and junk data using:

* ✅ Minimum face size threshold
* ✅ Aspect ratio validation
* ✅ Blur detection (Laplacian variance)
* ✅ Brightness thresholding
* ✅ ROI-based detection focus
* ✅ Cooldown-based duplicate prevention

### Result

* ✔ Clean face image dataset
* ✔ Reduced false positives
* ✔ Stable long-duration operation

---

## 📂 Output Details

### 📸 Captured Faces

Saved in:

```
event_faces/
```

Filename format:

```
face_00023_20260210_143522_123.jpg
```

---

### 🎥 Recorded Videos

Saved in:

```
recordings/
```

Filename format:

```
event_overlay_session2_20260210_120001.mp4
```

---

## ⚡ Performance Notes

* **CPU Usage:** ~15–30% (depends on camera and resolution)
* **Disk Usage:** ~3 GB per 3-hour session (720p @ 30 FPS)
* **Face Capture Speed:** Less than 1 second per face

---

## 🧪 Best Practices

* Ensure good, even lighting
* Place camera at eye level
* Avoid strong backlighting
* Test the system for 2–3 minutes before long sessions
* Ensure sufficient disk space for long recordings

---

## 🚀 Use Cases

* 🎓 College events & seminars
* 🏢 Office attendance monitoring
* 🎤 Conferences & expos
* 🏫 Classrooms
* 🛡️ Surveillance & monitoring

---

## 🔮 Future Enhancements (Optional)

* Known vs Unknown face recognition
* Attendance CSV export
* Web-based dashboard
* Deep learning models (FaceNet / ArcFace)
* Cloud storage integration

---

## 📜 License

This project is released under the **MIT License**.
You are free to use, modify, and distribute this project with proper attribution.

---

## 🙌 Author

**Developed by Atharva Shinde**


```



