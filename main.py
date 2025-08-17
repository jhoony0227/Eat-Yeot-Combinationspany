import pygame

pygame.init()
pygame.font.init()

text = [["아주 먼 옛날에.."
        , "한 남자가 있었습니다."
        , "그는 찢어지게 가난했죠."
        , "그래서 그는 열심히 일했습니다."
        , "그러다 결국 죽었습니다.."
        , "그래서 저승에서도 난리를 쳤습니다."
        , "마침내 신들이 그를 포기하고.."
        , "이승으로 돌아오게 됐습니다."
        , "돈을 벌어 신이 되세요!"]
        ,['next scene']]

how_to = ["space바를 눌러 다음으로 넘어가기", " "]
width = 1536
height = 1000
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Eat Yeot Combinationspany(by DMC)")

basic_Yeot = pygame.image.load("./basic_Yeot.png")
basic_Yeot = pygame.transform.scale(basic_Yeot, (150, 150))

cottage_bg = pygame.image.load("./초가집.png")
cottage_bg = pygame.transform.scale(cottage_bg, (width, height))

text_font = pygame.font.Font("./main.ttf", 60)
how_to_font = pygame.font.Font("./main.ttf", 30)

pygame.mixer.music.load("./황금의 심연.mp3")
pygame.mixer.music.play(-1)

running = True
textidx = 0
howidx = 0
scene = 0
clock = pygame.time.Clock()

char_index = 0
typing_speed = 100
last_char_time = 0
typing_complete = False

fade_state = "none"
fade_alpha = 0
fade_speed = 2.55
transition_complete = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if scene == 0 and fade_state == "none":
                    if not typing_complete:
                        char_index = len(text[scene][textidx])
                        typing_complete = True

                    else:
                        if textidx < len(text[scene]) - 1:
                            textidx += 1
                            char_index = 0
                            typing_complete = False

                        else:
                            fade_state = "out"

    if fade_state == "out":
        fade_alpha += fade_speed
        music_volume = max(0, (255 - fade_alpha) / 255)
        pygame.mixer.music.set_volume(music_volume)

        if fade_alpha >= 255:
            fade_alpha = 255
            pygame.mixer.music.set_volume(0)
            scene = 1
            howidx = 1
            textidx = 0
            fade_state = "in"
            transition_complete = False

    elif fade_state == "in":
        fade_alpha -= fade_speed

        if fade_alpha <= 0:
            fade_alpha = 0
            fade_state = "none"
            transition_complete = True

    current_time = pygame.time.get_ticks()
    
    if scene == 0:
        if not typing_complete and current_time - last_char_time > typing_speed:
            if char_index < len(text[scene][textidx]):
                char_index += 1
                last_char_time = current_time

            else:
                typing_complete = True
        
        screen.blit(cottage_bg, (0, 0))
        
        text_bg = pygame.Surface((width, 200))
        text_bg.set_alpha(150)
        text_bg.fill((0, 0, 0))
        screen.blit(text_bg, (0, height - 200))
        
        current_text = text[scene][textidx][:char_index]
        text_print = text_font.render(current_text, True, (255, 255, 255))
        text_rect = text_print.get_rect(center=(width // 2, height - 100))
        screen.blit(text_print, text_rect)
        
        instruction_text = "space바를 눌러 다음으로 넘어가십시오."
        
        how_to_printation = how_to_font.render(instruction_text, True, (255, 255, 255))
        how_to_rect = how_to_printation.get_rect(center=(width // 2, height - 40))
        screen.blit(how_to_printation, how_to_rect)
        
    elif scene == 1:
        main = pygame.image.load("./main_page.png")
        screen.blit(main, (0,0))
        pygame.display.flip()

    
    if fade_state != "none":
        fade_surface = pygame.Surface((width, height))
        fade_surface.set_alpha(fade_alpha)
        fade_surface.fill((0, 0, 0))
        screen.blit(fade_surface, (0, 0))
    
    pygame.display.flip()
    clock.tick(60)



# from collections import deque

# h,w = map(int,input().split())
# c = [list(map(int,input().split())) for i in range(h)]
# y,x = map(int,input().split())

# def bfs(y,x):

#     visited = [[-1]*w for i in range(h)]
#     visited[y][x] = 0

#     q = deque()
#     q.append((y,x,0))

#     dy = (-1,1,0,0)
#     dx = (0,0,-1,1)

#     while q:
#         y,x,t = q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]

#             if 0 <= ny < h and 0 <= nx < w:
#                 if c[ny][nx] == 1 and visited[ny][nx] == -1:
#                     q.append((ny,nx,t+1))
#                     visited[ny][nx] = t+1
    
#     return visited

# print(bfs(0,0)[y][x])

# #입력:
# '''
# 5 7
# 1 1 1 1 0 0 0
# 1 0 0 1 0 0 0
# 1 1 1 1 0 0 0
# 1 0 1 1 0 1 0
# 1 1 1 1 1 1 1
# 4 6
# '''


# #출력:
# '''
# 10
# '''

# #설명: 높이와 너비 주어짐, 1은 길 0 은 벽, 어떠한 좌표로 가는데에 얼마나 걸리는지 구하는 코드