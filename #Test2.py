# Tao danh sach de luu diem so
scores = []

# Nhap 10 gia tri tu nguoi dung
for i in range(10):
    score = float(input(f"Enter test score {i+1}: "))
    scores.append(score) # Vong lap chay 10 lan de nhap 10 scores. Moi diem chuyen thanh so thuc (float) va them vao danh sach score
   

# (a) In ra diem thap nhat va cao nhat cua 10 scores
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")

# (b) In ra diem trung binh cua 10 scores
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}") # Trung binh cong bang tong scores chia cho so phan tu trong scores va lam tron 2 chu so thap phan



# (c) In ra diem cao thu hai
sorted_scores = sorted(scores, reverse=True) # sap xep tu cao xuong thap
print(f"Second largest score: {sorted_scores[1]}") # in ki tu thu 2 bat dau tu so thu tu 0

# (d) Kiem tra xem co diem nao lon hon 100 khong
for score in scores:
    if score > 100:
        print(f"Caution: A value over 100 has been entered.")


# (e) Drop the two lowest scores and print out the average of the rest
sorted_scores = sorted(scores) # thu tu lay tu thap den cao
remaining_scores = sorted_scores[2:] # bat dau lay tu phan tu thu ba den phan tu cuoi danh sach
new_average = sum(remaining_scores) / len(remaining_scores)
print(f"Average after dropping two lowest scores: {new_average:.2f}")