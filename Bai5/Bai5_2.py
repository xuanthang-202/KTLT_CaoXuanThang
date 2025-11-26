print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import datetime as dt
# Định nghĩa chuỗi định dạng thời gian
format_string = '%Y-%m-%dT%H:%M:%S'
# Chuyển đổi chuỗi thời gian thành đối tượng datetime (t1)
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format_string)
print('--- Chi tiết của t1 (2008-10-12 14:45:52) ---')
print('Day: ' + str(t1.day))
print('Month: ' + str(t1.month))
print('Minute: ' + str(t1.minute))
print('Second: ' + str(t1.second))
# Định nghĩa ngày và giờ hiện tại (t2)
t2 = dt.datetime.now()
# Tính toán sự khác biệt giữa hai thời điểm
diff = t2 - t1
print('\n--- Sự khác biệt thời gian ---')
# In ra tổng số ngày khác biệt trong đối tượng timedelta
print('How many days difference? ' + str(diff.days))
