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
pygame.display.set_caption("Eat Yoat Combinationspany")
basic_Yeot = pygame.image.load("./basic_Yeot.png")
basic_Yeot = pygame.transform.scale(basic_Yeot, (150, 150))

text_font = pygame.font.Font("./main.ttf", 60)
how_to_font = pygame.font.Font("./main.ttf", 30)

pygame.mixer.music.load("./황금의 심연.mp3")
pygame.mixer.music.play(-1)

text_print = text_font.render(text[0][0], True, (255, 255, 255))
text_rect = text_print.get_rect(center=(width // 2, height - 100))

how_to_printation = how_to_font.render(how_to[0], True, (0, 0, 0))
how_to_rect = how_to_printation.get_rect(center=(width // 2, 50))

running = True

textidx = 0
howidx = 0

scene = 0

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if scene == 0:
        text_print = text_font.render(text[scene][textidx], True, (255, 255, 255))
        text_rect = text_print.get_rect(center=(width // 2, height - 100))

        how_to_printation = how_to_font.render(how_to[0], True, (0, 0, 0))
        how_to_rect = how_to_printation.get_rect(center=(width // 2, 50))

        screen.blit(how_to_printation, how_to_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if textidx < len(text[scene])-1:
                        textidx += 1
                    
                    else:
                        scene = 1
                        howidx = 1
                        textidx = 0
                        
    if scene == 1:
        pass