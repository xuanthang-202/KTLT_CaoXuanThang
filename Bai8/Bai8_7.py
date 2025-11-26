print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import tkinter
import random
from tkinter import messagebox
# Danh sách các màu có thể có
colors = ['Red', 'Green', 'Pink', 'Black', 
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 0
game_started = False # Biến cờ để kiểm soát lần nhập đầu tiên
# Hàm bắt đầu trò chơi
def startGame(event):
    global timeleft
    global game_started    
    # Đặt thời gian chơi theo Bước 2 (120s) và chỉ chạy một lần
    if not game_started:
        game_started = True
        timeleft = 120
        # Reset điểm khi bắt đầu
        global score
        score = 0
        scoreLabel.config(text = "Score: " + str(score))
        countdown()
        nextColour()
# Hàm chọn và hiển thị màu tiếp theo
def nextColour():
    global score
    global timeleft    
    # Chỉ xử lý khi trò chơi đang diễn ra
    if timeleft > 0 and game_started:
        # Lấy màu hiển thị ở lần chơi trước (là colors[1] trước khi shuffle)
        displayed_colour_name = colors[0] # Tên chữ hiển thị
        correct_input_colour = colors[1]  # MÀU SẮC THỰC CỦA CHỮ
        # Bỏ qua lần nhập đầu tiên (lúc đó e.get() đang trống)
        if e.get() != "":
            # Kiểm tra xem màu nhập vào có khớp với MÀU SẮC THỰC của chữ không
            if e.get().lower() == correct_input_colour.lower(): 
                # Bước 3: Cộng 2 điểm cho lần đoán đúng
                score += 2
            else:
                # Bước 3: Trừ 1 điểm cho lần đoán sai
                score -= 1 
        # Xóa nội dung ô nhập liệu
        e.delete(0, tkinter.END)        
        # Chọn ngẫu nhiên màu chữ (colors[0]) và màu nền (colors[1])
        random.shuffle(colors)        
        # Hiển thị màu chữ ngẫu nhiên và màu nền
        label.config(fg = str(colors[1]), text = str(colors[0]))       
        # Cập nhật điểm trên giao diện
        scoreLabel.config(text = "Score: " + str(score))        
        # Đảm bảo ô nhập liệu luôn được tập trung
        e.focus_set()
# Hàm đếm ngược thời gian
def countdown():
    global timeleft
    global game_started    
    if timeleft > 0 and game_started:
        # Giảm thời gian
        timeleft -= 1        
        # Cập nhật thời gian còn lại
        timeLabel.config(text = "Time left: " + str(timeleft))     
        # Chạy lại hàm sau 1 giây (1000ms)
        timeLabel.after(1000, countdown)
    elif timeleft == 0 and game_started:
        # Khi hết giờ
        game_started = False
        label.config(text = "Hết giờ!", fg = "black")
        timeLabel.config(text = "Time left: 0")
        messagebox.showinfo("Kết thúc", f"Trò chơi kết thúc! Điểm của bạn: {score}")
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")
instructions = tkinter.Label(root, text = "Nhập tên màu sắc của chữ\nChứ không phải chữ hiển thị!", 
                                font = ('Helvetica', 12))
instructions.pack()
scoreLabel = tkinter.Label(root, text = "Nhấn Enter để bắt đầu", 
                           font = ('Helvetica', 12))
scoreLabel.pack()
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), 
                           font = ('Helvetica', 12))
timeLabel.pack()
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
e = tkinter.Entry(root)
# Gắn sự kiện phím Enter để bắt đầu trò chơi
root.bind('<Return>', startGame)
# Gắn sự kiện phím Enter để kiểm tra đáp án và chuyển sang màu mới
e.bind('<Return>', lambda event: nextColour()) 
e.pack()
e.focus_set()
root.mainloop()
