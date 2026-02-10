# save as record_30min_with_overlay.py
import cv2, os, time
from datetime import datetime

SAVE_DIR = "recordings"
FACE_SAVE_DIR = "event_faces"
DURATION_MINUTES = 180  # 3 hours
COOLDOWN = 2
MIN_FACE_SIZE = (60, 60)
GRID_SIZE = 80
PADDING = 15
TARGET_RES = (1280, 720)
FPS = 30

os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(FACE_SAVE_DIR, exist_ok=True)

def open_camera():
    for be in (cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY):
        cap = cv2.VideoCapture(0, be)
        if not cap.isOpened():
            cap.release()
            continue
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, TARGET_RES[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, TARGET_RES[1])
        cap.set(cv2.CAP_PROP_FPS, FPS)
        # warm-up
        ok = 0
        for _ in range(8):
            ret, _ = cap.read()
            if ret: ok += 1
            cv2.waitKey(1)
        if ok >= 4:
            print(f"✅ Camera opened with backend {be}")
            return cap
        cap.release()
    return None

def choose_writer(path, fps, frame_size):
    fourcc_mp4v = cv2.VideoWriter_fourcc(*'mp4v')  # type: ignore[attr-defined]
    w = cv2.VideoWriter(path, fourcc_mp4v, fps, frame_size)
    if w.isOpened(): return w, path
    # fallback
    avi = os.path.splitext(path)[0] + ".avi"
    fourcc_xvid = cv2.VideoWriter_fourcc(*'XVID')  # type: ignore[attr-defined]
    w = cv2.VideoWriter(avi, fourcc_xvid, fps, frame_size)
    return w, avi

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # type: ignore[attr-defined]
    if face_cascade.empty():
        raise RuntimeError("Failed to load Haar cascade.")

    cap = open_camera()
    if cap is None:
        raise RuntimeError("❌ Could not open camera.")

    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = cap.get(cv2.CAP_PROP_FPS) or FPS
    if fps <= 1: fps = FPS

    last_capture = {}
    face_count = 0
    global_start = time.time()
    session_count = 0

    print("="*50)
    print(f"Recording 3-hour sessions (with overlay)")
    print("="*50)

    while True:
        # Create new video file for each 3-hour session
        session_count += 1
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = os.path.join(SAVE_DIR, f"event_overlay_session{session_count}_{ts}.mp4")
        writer, final_path = choose_writer(out_path, fps, frame_size)
        if not writer.isOpened():
            cap.release()
            raise RuntimeError("❌ Could not open VideoWriter.")

        start = time.time()
        print(f"\n{'='*50}")
        print(f"Session {session_count} - Recording → {final_path}")
        print(f"{'='*50}")

        session_running = True
        while session_running:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Frame grab failed; stopping.")
                session_running = False
                break

            current_time = time.time()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4, minSize=MIN_FACE_SIZE
            )

            for (x, y, w, h) in faces:
                pos_key = f"{x // GRID_SIZE}_{y // GRID_SIZE}"
                if pos_key not in last_capture or (current_time - last_capture[pos_key]) > COOLDOWN:
                    y1 = max(0, y - PADDING); y2 = min(frame.shape[0], y + h + PADDING)
                    x1 = max(0, x - PADDING); x2 = min(frame.shape[1], x + w + PADDING)
                    face_img = frame[y1:y2, x1:x2]
                    filename = f"face_{face_count + 1:05d}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]}.jpg"
                    cv2.imwrite(os.path.join(FACE_SAVE_DIR, filename), face_img)
                    face_count += 1
                    last_capture[pos_key] = current_time
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 200, 0), 3)
                    cv2.putText(frame, 'SAVED', (x, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 220, 255), 2)
                    cv2.putText(frame, 'WAIT', (x, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 220, 255), 2)

            # Stats overlay
            elapsed = int(current_time - start)
            cv2.rectangle(frame, (10, 10), (420, 120), (0, 0, 0), -1)
            cv2.putText(frame, f'Total Saved: {face_count}', (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            cv2.putText(frame, f'Now Detecting: {len(faces)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 0), 2)
            cv2.putText(frame, f'Time: {elapsed // 60}m {elapsed % 60}s', (20, 102), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

            # Write to video file and preview
            writer.write(frame)
            cv2.imshow('Recording with Overlay (Q=Stop)', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("⏹ Stopped by user.")
                session_running = False
                break

            if (time.time() - start) >= DURATION_MINUTES * 60:
                print(f"⏱ Session {session_count} complete (3 hours)—starting next session.")
                break

        writer.release()
        print(f"✅ Session {session_count} saved: {final_path}")
        
        if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"\n{'='*50}")
    print(f"✅ Total sessions recorded: {session_count}")
    print(f"✅ Total faces saved: {face_count}")
    print(f"✅ Faces saved in: {FACE_SAVE_DIR}")
    print(f"{'='*50}")
    
if __name__ == "__main__":
    main()