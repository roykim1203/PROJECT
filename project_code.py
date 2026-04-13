print("송도 생활을 마치고 신촌에 처음 도착했다. 연대앞 버스정류장이다.")
print("현재 시각은 11시.")
print("1시 수업은 이윤재관 511호다.")
print("배가 고프다.\n")

print("________________")

def init_game():
    player = {
        "hp": 10,
        "cur_loc": "연대앞 버스정류장",
        "x": 0,  
        "y": 6,
        "balance" : 50000,
        "bag" = []
}

env = {
    "Time": "11:00",
    "Difficult" : "Normal"
}

# --------------------------------------------------------
# 여기까지 작성 후 첫 번째 Commit & Push 진행
# --------------------------------------------------------

map_data = [
    [None, None, None, None, "새천년관", "이윤재관"]
    ["백양관", "백양로5", "대강당", "음악관", "알렌관", "ABMRC"]
    ["중앙 도서관", "독수리상", "학생회관", "루스채플", "재활병원", "치과대학"]
    ["체육관", "백양로3", "공터2", "광혜원", "어린이 병원", "세브란스 병원"]
    ["공학관", "백양로2", "백주년기념관", "안과병원", "제중관", None],
    ["공학원", "백양로1", "공터1", "암 병원", "의과대학", None],
    ["연대앞 버스정류장", "정문", "스타벅스", "세브란스병원 버스 정류장", None , None] 
]


while True:
    direction = input("이동할 방향을 입력하세요 (동, 서, 남, 북) 또는 '종료': ")
    
    if direction == "종료":
        print("이동을 마칩니다.\n")
        break
        

    next_x = player["x"]
    next_y = player["y"]
    
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
        player["x"] = next_x
        player["y"] = next_y
        player["위치"] = map_data[next_y][next_x]
        print(f"[{mc['위치']}] 으로 이동했습니다.\n")

# --------------------------------------------------------
# 여기까지 작성 후 두 번째 Commit & Push 진행
# --------------------------------------------------------

settings = {}

while True:
    level = input("난이도를 설정하세요 (쉬움, 보통, 어려움): ")
    

    if level == "쉬움" or level == "보통" or level == "어려움":
        settings["난이도"] = level
        print(f"\n게임 난이도가 '{level}'(으)로 설정되었습니다.")
        break
    else:
        print("정확한 난이도(쉬움, 보통, 어려움)를 입력해주세요.\n")

# --------------------------------------------------------
# 여기까지 작성 후 세 번째 Commit & Push 진행
# --------------------------------------------------------








