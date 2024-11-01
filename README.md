# Đoán Số - Trò Chơi Thú Vị! 🎮✨

Chào mừng bạn đến với dự án **Đoán Số**! Trong trò chơi này, bạn sẽ thử tài phán đoán số mà chương trình đã chọn. Đây là một hoạt động thú vị để cải thiện kỹ năng lập trình của bạn và cũng là cách tuyệt vời để học hỏi về logic và điều kiện trong lập trình!

## Mô Tả Dự Án 📝

Trò chơi "Đoán Số" cho phép người chơi đoán một số ngẫu nhiên mà máy tính đã chọn trong khoảng từ 1 đến 100. Chương trình sẽ cung cấp phản hồi cho người chơi để giúp họ biết được liệu số đoán của mình quá cao, quá thấp, hay đúng!

## Cách Chạy Dự Án 🚀

1. **Cài đặt Python**: Đảm bảo bạn đã cài đặt Python trên máy tính của mình. Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).

2. **Chạy Mã Nguồn**: Sao chép mã nguồn và mở tệp Python (.py) trong một trình soạn thảo mã. Sau đó, chạy chương trình:
   ```bash
   python GuessTheNumber.py
   ```

## Mã Nguồn 📄

Dưới đây là mã nguồn chính của dự án:

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Chọn số ngẫu nhiên từ 1 đến 100
    attempts = 0  # Đếm số lần đoán
    guessed = False  # Biến kiểm tra xem số đã được đoán chưa

import random

def guess_the_number():
    print("🎉 Chào mừng bạn đến với trò chơi 'Guess the Number'! 🎉")
    print("Tôi đã chọn một số ngẫu nhiên từ 1 đến 100. Bạn hãy cố gắng đoán số đó!")

    # Tạo số ngẫu nhiên từ 1 đến 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Nhập số đoán từ người chơi
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
                break  # Kết thúc trò chơi

        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

# Chạy trò chơi
guess_the_number()
```

## Ghi Chú 📌

- **Khám Phá Thêm**: Hãy thử thay đổi khoảng số hoặc thêm một số tính năng mới để làm cho trò chơi thú vị hơn!
- **Chia Sẻ Sáng Tạo**: Nếu bạn tạo ra một phiên bản độc đáo của trò chơi, đừng quên chia sẻ với bạn bè và cộng đồng nhé! 🌍

## Liên Hệ 🤝

Nếu bạn có bất kỳ câu hỏi nào hoặc cần hỗ trợ, hãy liên hệ với chúng tôi qua [Fanpage CodeThinkers](https://www.facebook.com/CodeThinkers).

---

Hãy cùng nhau khám phá và sáng tạo với lập trình nhé! 💖