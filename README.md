# 🎉 Guess the Number Game 🎉

## Mô Tả
"Guess the Number" là một trò chơi đơn giản được viết bằng Python, nơi người chơi cố gắng đoán một số ngẫu nhiên được máy tính tạo ra trong khoảng từ 1 đến 100. Trò chơi giúp rèn luyện tư duy logic và khả năng lập trình cơ bản.

## Tính Năng
- Người chơi có thể nhập số đoán.
- Máy tính phản hồi nếu số đoán thấp hơn, cao hơn hoặc chính xác với số cần đoán.
- Đếm số lần thử của người chơi.

## Yêu Cầu
- Python 3.x

## Cài Đặt
1. **Cài đặt Python**: Đảm bảo rằng bạn đã cài đặt Python trên máy tính của mình. Bạn có thể tải xuống từ [python.org](https://www.python.org/downloads/).
   
2. **Tạo Tệp Mới**:
   - Mở một trình soạn thảo mã (như VSCode, PyCharm hoặc IDLE) và tạo một tệp mới có tên `guess_the_number.py`.

3. **Sao Chép Mã**:
   - Sao chép mã nguồn trò chơi vào tệp `guess_the_number.py`:

   ```python
   import random

   def guess_the_number():
       print("🎉 Chào mừng bạn đến với trò chơi 'Guess the Number'! 🎉")
       print("Tôi đã chọn một số ngẫu nhiên từ 1 đến 100. Bạn hãy cố gắng đoán số đó!")

       number_to_guess = random.randint(1, 100)
       attempts = 0

       while True:
           try:
               guess = int(input("Nhập số của bạn: "))
               attempts += 1

               if guess < 1 or guess > 100:
                   print("Vui lòng nhập một số trong khoảng từ 1 đến 100.")
                   continue

               if guess < number_to_guess:
                   print("Số bạn đoán thấp hơn số cần đoán. Hãy thử lại!")
               elif guess > number_to_guess:
                   print("Số bạn đoán cao hơn số cần đoán. Hãy thử lại!")
               else:
                   print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {number_to_guess} sau {attempts} lần thử!")
                   break

           except ValueError:
               print("Vui lòng nhập một số hợp lệ!")

   guess_the_number()
