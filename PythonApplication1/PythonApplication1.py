def fill_in_the_blanks():
    # Câu gốc
    original_sentence = "Tôi là sinh viên ngành UNETI"
    
    # Tạo câu có chỗ trống (bỏ 2 từ ngẫu nhiên)
    words = original_sentence.split()
    blanks = [2, 4]  # Vị trí các từ bị bỏ trống (0-based index)
    
    displayed_sentence = []
    answers = {}
    
    for i, word in enumerate(words):
        if i in blanks:
            displayed_sentence.append("___")
            answers[i] = word
        else:
            displayed_sentence.append(word)
    
    # Hiển thị câu có chỗ trống
    print("Hãy điền từ còn thiếu vào chỗ trống:")
    print(" ".join(displayed_sentence))
    
    # Yêu cầu người dùng nhập các từ còn thiếu
    user_answers = {}
    for blank_pos in sorted(answers.keys()):
        user_input = input(f"Nhập từ còn thiếu tại vị trí {blank_pos + 1}: ")
        user_answers[blank_pos] = user_input
    
    # Kiểm tra kết quả
    print("\nKết quả:")
    correct = True
    for pos in answers:
        if user_answers.get(pos, "").lower() == answers[pos].lower():
            print(f"Vị trí {pos + 1}: Đúng ({answers[pos]})")
        else:
            print(f"Vị trí {pos + 1}: Sai. Đáp án đúng là: {answers[pos]}")
            correct = False
    
    if correct:
        print("\nChúc mừng! Bạn đã điền đúng tất cả.")
    else:
        print("\nCố gắng lần sau nhé!")

# Chạy chương trình
if __name__ == "__main__":
    fill_in_the_blanks()