import cv2
import face_recognition
import numpy as np
import csv
import os
from datetime import datetime
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from PIL import Image, ImageTk

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("얼굴 인식 출결 시스템")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#2c3e50")
        
        self.video_capture = cv2.VideoCapture(1) #카메라 선택 기본 캠0 따로캠1
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video_capture.set(cv2.CAP_PROP_FPS, 30)
        
        self.frame = Frame(self.root, bg="#34495e", padx=20, pady=20)
        self.frame.pack(fill=BOTH, expand=True)
        
        self.canvas = Canvas(self.frame, width=640, height=480)
        self.canvas.pack(side=LEFT, padx=10, pady=10)
        
        button_frame = Frame(self.frame, bg="#34495e")
        button_frame.pack(side=RIGHT, padx=10, pady=10, anchor=N)
        
        self.btn_register = ttk.Button(button_frame, text="사용자 등록", command=self.register_user, style="Custom.TButton")
        self.btn_register.pack(fill=X, pady=5)
        
        self.attendance_log = Text(button_frame, height=30, width=50, font=("Helvetica", 12), bg="#ecf0f1", fg="#2c3e50")
        self.attendance_log.pack(fill=BOTH, pady=5)
        
        self.known_faces = []
        self.known_ids = []
        self.load_registered_users()
        
        self.recorded_users = set()
        
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Helvetica", 14, "bold"), foreground="#2c3e50", background="#3498db", padding=10)
        
        self.update_frame()
    
    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.known_faces, face_encoding)
                face_distances = face_recognition.face_distance(self.known_faces, face_encoding)
                best_match_index = np.argmin(face_distances)
                
                if matches[best_match_index]:
                    user_id = self.known_ids[best_match_index]
                    if user_id not in self.recorded_users:
                        self.log(f"출결 확인: {user_id}")
                        self.save_attendance(user_id)
                        self.recorded_users.add(user_id)
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, user_id, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        
        self.root.after(33, self.update_frame)
    
    def register_user(self):
        user_id = simpledialog.askstring("사용자 등록", "사용자 ID를 입력하세요:")
        if user_id:
            num_images = simpledialog.askinteger("사진 등록", "등록할 사진의 개수를 입력하세요:")
            if num_images:
                for i in range(num_images):
                    ret, frame = self.video_capture.read()
                    if ret:
                        cv2.imwrite(f"faces/{user_id}_{i+1}.jpg", frame)
                        self.log(f"{user_id}의 사진 {i+1}장 등록 완료")
                self.load_registered_users()
                self.log(f"{user_id} 등록 완료")
    
    def load_registered_users(self):
        self.known_faces = []
        self.known_ids = []
        
        faces_folder = "faces"
        for filename in os.listdir(faces_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                face_image = face_recognition.load_image_file(os.path.join(faces_folder, filename))
                face_encoding = face_recognition.face_encodings(face_image)[0]
                self.known_faces.append(face_encoding)
                user_id = os.path.splitext(filename)[0].split("_")[0]
                self.known_ids.append(user_id)
    
    def save_attendance(self, user_id):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user_id, timestamp])
    
    def log(self, message):
        self.attendance_log.insert(END, message + "\n")
        self.attendance_log.see(END)

if __name__ == "__main__":
    root = Tk()
    attendance_system = AttendanceSystem(root)
    root.mainloop()