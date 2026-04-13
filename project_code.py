print("송도 생활을 마치고 신촌에 처음 도착했다. 연대앞 버스정류장이다.")
print("현재 시각은 11시.")
print("1시 수업은 이윤재관 511호다.")
print("배가 고프다.\n")

hero = {
    "배고픔": True,
    "위치": "연대앞 버스정류장",
    "x": 0,  
    "y": 2   
}

env = {
    "현재시각": "11:00"
}

# --------------------------------------------------------
# 여기까지 작성 후 첫 번째 Commit & Push 진행
# --------------------------------------------------------

map_data = [
    ["공학관", "백양로1", "백주년기념관"],
    ["공학원", "백양로1", "공터1"],
    ["연대앞 버스정류장", "정문", "세브란스병원"],
    ["막힘", "막힘", "버스정류장"]  
]


while True:
    direction = input("이동할 방향을 입력하세요 (동, 서, 남, 북) 또는 '종료': ")
    
    if direction == "종료":
        print("이동을 마칩니다.\n")
        break
        

    next_x = hero["x"]
    next_y = hero["y"]
    
    if direction == "동":
        next_x = next_x + 1
    elif direction == "서":
        next_x = next_x - 1
    elif direction == "남":
        next_y = next_y + 1
    elif direction == "북":
        next_y = next_y - 1
    else:
        print("올바른 방향(동, 서, 남, 북)을 입력해주세요.\n")
        continue

    
    if next_x < 0 or next_x > 2 or next_y < 0 or next_y > 3:
        print("그 방향은 막혔어.\n")
        
    
    elif map_data[next_y][next_x] == "막힘":
        print("그 방향은 막혔어.\n")
        
    
    else:
        hero["x"] = next_x
        hero["y"] = next_y
        hero["위치"] = map_data[next_y][next_x]
        print(f"[{hero['위치']}] 으로 이동했습니다.\n")

# --------------------------------------------------------
# 여기까지 작성 후 두 번째 Commit & Push 진행
# --------------------------------------------------------





