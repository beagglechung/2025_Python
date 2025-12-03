import pygame
import sys
import random

pygame.init()

# 게임 화면 크기
screen_width = 800
screen_height = 600

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#(추가) 폭발 사운드 준비
explosion_sound = pygame.mixer.Sound("explosion.wav")

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(green)
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# 외계인 클래스
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface((30, 30))
        #self.image.fill(red)
        
        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)
            
    def explode(self):
        explosion_sound.play()  #(추가) 폭발 사운드 재생
        #self.kill()

# 레이저 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
            
# 게임 화면 생성
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 플레이어 생성
player = Player()
all_sprites.add(player)

# 외계인 생성
for _ in range(10):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

# 게임 루프
clock = pygame.time.Clock()
# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # 화면 업데이트
    all_sprites.update()
    # 외계인과 레이저의 충돌 검사
    hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
    for hit in hits:
        alien = Alien()
        alien.explode()
        all_sprites.add(alien)
        aliens.add(alien)

    # 충돌 검사
    if pygame.sprite.spritecollide(player, aliens, False):
        print("게임 오버!")
        #pygame.quit()
        #sys.exit()

    # 배경 화면 채우기
    screen.fill(black)

    # 스프라이트 그룹을 화면에 그리기
    all_sprites.draw(screen)

    # 화면 업데이트
    pygame.display.flip()
        # FPS 설정 (60FPS)
    clock.tick(60)
