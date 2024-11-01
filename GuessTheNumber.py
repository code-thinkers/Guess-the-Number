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
