# 📅 Personal Todo Web App

Todo Web Application สำหรับจัดการงานประจำวันพร้อมระบบ Due Date ที่ช่วยให้คุณติดตามงานที่ใกล้ครบกำหนดได้อย่างมีประสิทธิภาพ

## ✨ Features

- **📋 จัดการ Todo**: เพิ่ม, แก้ไข, ลบงานได้ง่าย
- **📅 Due Date System**: กำหนดวันครบกำหนดสำหรับแต่ละงาน
- **🔔 Smart Notifications**: แสดงสถานะงาน (เลยกำหนด, วันนี้, ยังไม่ครบกำหนด)
- **📊 Filter & View**: ดูงานตามสถานะต่างๆ
- **💾 Auto Save**: บันทึกข้อมูลอัตโนมัติ
- **📱 Responsive Design**: ใช้งานได้ทั้งบน Desktop และ Mobile

## 🚀 API Endpoints

### Todo Operations
- `GET /` - หน้าแรกของ Web App
- `GET /todos` - ดู Todo ทั้งหมด
- `GET /todos/upcoming` - ดูงานที่ยังไม่ครบกำหนด
- `GET /todos/{id}` - ดู Todo เฉพาะ ID
- `POST /todos` - เพิ่ม Todo ใหม่
- `PUT /todos/{id}` - แก้ไข Todo
- `DELETE /todos/{id}` - ลบ Todo

### System
- `GET /health` - ตรวจสอบสถานะระบบ

## 📦 Installation & Setup

### วิธีที่ 1: รันด้วย Python

```bash
# 1. Clone repository
git clone <repository-url>
cd personal-todo-app

# 2. สร้าง virtual environment
python -m venv venv
source venv/bin/activate  # บน Windows: venv\Scripts\activate

# 3. ติดตั้ง dependencies
pip install -r requirements.txt

# 4. รันแอปพลิเคชัน
uvicorn main:app --reload

# 5. เปิดเบราว์เซอร์ไปที่
# http://localhost:8000
```

### วิธีที่ 2: รันด้วย Docker

```bash
# 1. Build Docker image
docker build -t personal-todo-app .

# 2. รัน container
docker run -p 8000:8000 personal-todo-app

# 3. เปิดเบราว์เซอร์ไปที่
# http://localhost:8000
```

### วิธีที่ 3: ใช้งานผ่าน Dev Container (VS Code)

```bash
# 1. เปิดโปรเจกต์ใน VS Code
# 2. กด Ctrl+Shift+P และเลือก "Dev Containers: Reopen in Container"
# 3. VS Code จะสร้าง development environment อัตโนมัติ
```

## 📂 Project Structure

```
personal-todo-app/
├── __pycache__/          # Python cache files
├── .devcontainer/        # VS Code dev container config
│   └── devcontainer.json
├── templates/            # HTML templates
│   └── index.html
├── .gitignore           # Git ignore rules
├── Dockerfile           # Docker configuration
├── main.py              # FastAPI application
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── todos.json           # Data storage (auto-generated)
```

## 🎯 Usage Guide

### เพิ่ม Todo ใหม่
1. กรอกรายละเอียดงานในช่อง "รายละเอียดงาน"
2. เลือกวันครบกำหนดใน "วันครบกำหนด"
3. คลิก "✨ เพิ่มงาน"

### ดูงานตามสถานะ
- **📋 ทั้งหมด**: แสดงงานทั้งหมด
- **⏰ ยังไม่ครบกำหนด**: แสดงงานที่ยังไม่ถึงวันครบกำหนด
- **🔥 เลยกำหนด**: แสดงงานที่เลยกำหนดแล้ว

### แก้ไขงาน
1. คลิกปุ่ม "✏️ แก้ไข" ในงานที่ต้องการแก้ไข
2. เปลี่ยนแปลงข้อมูลตามต้องการ
3. คลิก "💾 บันทึก"

### ลบงาน
1. คลิกปุ่ม "🗑️ ลบ" ในงานที่ต้องการลบ
2. ยืนยันการลบในกล่องโต้ตอบ

## 🎨 UI Features

### Status Indicators
- **🔴 เลยกำหนด**: งานที่เลยวันครบกำหนดแล้ว (สีแดง)
- **🟡 วันนี้**: งานที่ครบกำหนดวันนี้ (สีเหลือง)
- **🟢 ยังไม่ครบกำหนด**: งานที่ยังมีเวลา (สีเขียว)

### Responsive Design
- ✅ Desktop-friendly interface
- ✅ Mobile-optimized layout
- ✅ Touch-friendly buttons
- ✅ Readable fonts and colors

## 🔧 Technical Details

### Backend (FastAPI)
- **Framework**: FastAPI 0.104.1
- **Server**: Uvicorn with auto-reload
- **Data Storage**: JSON file (todos.json)
- **Validation**: Pydantic models
- **Templates**: Jinja2

### Frontend (Vanilla JavaScript)
- **Styling**: Pure CSS with gradients and animations
- **Interactivity**: Vanilla JavaScript (no frameworks)
- **Icons**: Unicode emojis
- **Responsive**: CSS Grid and Flexbox

### Data Model
```python
class Todo(BaseModel):
    id: int
    task: str
    due: date
```

## 🔒 Security & Performance

- ✅ Input validation with Pydantic
- ✅ XSS protection with HTML escaping
- ✅ Error handling and user feedback
- ✅ Optimized CSS with minimal JavaScript
- ✅ Health check endpoint for monitoring

## 🐛 Troubleshooting

### ปัญหาที่พบบ่อย

**1. ไม่สามารถเข้าถึง localhost:8000**
```bash
# ตรวจสอบว่า port 8000 ว่างหรือไม่
lsof -i :8000

# ใช้ port อื่นแทน
uvicorn main:app --port 8080
```

**2. ข้อมูล Todo หายไป**
```bash
# ตรวจสอบไฟล์ todos.json
ls -la todos.json

# ถ้าไฟล์หาย ระบบจะสร้างใหม่อัตโนมัติ
```

**3. Docker build ล้มเหลว**
```bash
# ลบ image เก่าและ build ใหม่
docker rmi personal-todo-app
docker build --no-cache -t personal-todo-app .
```

## 🔮 Future Enhancements

- [ ] User authentication system
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Push notifications
- [ ] Task categories and tags
- [ ] Priority levels
- [ ] Export to calendar
- [ ] Dark mode toggle
- [ ] Collaborative todos
- [ ] Mobile app version

## 📄 License

MIT License - feel free to use and modify for your own projects!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**Happy Todo Management! 🎉**

สร้างโดย [Your Name] สำหรับการจัดการงานอย่างมีประสิทธิภาพ
