import pygame
import random

# 화면 크기 및 색상 정의
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 패들 클래스 정의
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2
        self.rect.y = SCREEN_HEIGHT - 20

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

# 공 클래스 정의
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-5, 5]), -5]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

# 블록 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("블록 깨기 게임")
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()

# 블록 생성
for i in range(10):
    block = Block(BLACK, 80, 30)
    block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
    block.rect.y = random.randrange(250)
    block_list.add(block)
    all_sprites_list.add(block)

# 패들과 공 생성
paddle = Paddle(BLACK, 100, 10)
all_sprites_list.add(paddle)
ball = Ball(BLACK, 10, 10)
all_sprites_list.add(ball)

# 게임 루프
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 게임 로직 업데이트
    all_sprites_list.update()

    # 공과 패들 충돌 감지
    if pygame.sprite.collide_rect(ball, paddle):
        ball.velocity[1] = -ball.velocity[1]

    # 공과 블록 충돌 감지
    block_hit_list = pygame.sprite.spritecollide(ball, block_list, True)
    if len(block_list) == 0:
        print("You win!")
        done = True

    # 화면 그리기
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()

    # 초당 프레임 제한
    clock.tick(60)

pygame.quit()
