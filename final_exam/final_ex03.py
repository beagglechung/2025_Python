import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("문제 3")

clock = pygame.time.Clock()
white = (255, 255, 255)

# 사과 이미지 로드
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

# ---------------- 플레이어 클래스 ----------------
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH // 2, HEIGHT // 2)
    self.speed = 3

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
    if keys[pygame.K_UP]:
      self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
      self.rect.y += self.speed

    self.rect.clamp_ip(screen.get_rect())

  # 총알 발사
  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)

# ---------------- 총알 클래스 ----------------
class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((5, 20))
    self.image.fill(white)
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.bottom = y
    self.speed_y = -7

  def update(self):
    self.rect.y += self.speed_y
    if self.rect.bottom < 0:
      self.kill()

# ---------------- 스프라이트 그룹 ----------------
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 사과 관리
apples = []
apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30  # 프레임 간격

score = 0
lives = 3
game_over = False

def spawn_apple():
  """위쪽에서만 아래로 떨어지는 사과 생성"""
  size = 40
  x = random.randint(0, WIDTH - size)
  y = -size
  vx = 0
  vy = random.randint(2, 4)  # 아래 방향 속도
  rect = pygame.Rect(x, y, size, size)
  apples.append({"rect": rect, "vx": vx, "vy": vy})


def reset_game():
  """게임 재시작 시 상태 초기화"""
  global score, lives, apples, apple_spawn_timer, game_over
  score = 0
  lives = 3
  apples.clear()
  apple_spawn_timer = 0
  game_over = False

  # 플레이어 위치 초기화
  player.rect.center = (WIDTH // 2, HEIGHT // 2)

  # 남아있는 총알 제거
  for b in bullets:
    b.kill()


# ---------------- 메인 루프 ----------------
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      # 게임 진행 중일 때만 총알 발사
      if not game_over and event.key == pygame.K_SPACE:
        player.shoot()

      # 게임 오버 상태에서 R 키로 재시작
      if game_over and event.key == pygame.K_r:
        reset_game()

  # ---------------- 업데이트 ----------------
  if not game_over:
    all_sprites.update()

    # 사과 생성
    apple_spawn_timer += 1
    if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
      apple_spawn_timer = 0
      spawn_apple()

    # 사과 이동 + 충돌 처리
    updated_apples = []
    for apple in apples:
      rect = apple["rect"]
      vx = apple["vx"]
      vy = apple["vy"]

      rect.x += vx
      rect.y += vy

      # 화면 밖 → 삭제
      if rect.top > HEIGHT:
        continue

      # 1) 플레이어와 사과 충돌 → 점수 감소 + 목숨 감소
      if player.rect.colliderect(rect):
        score = max(0, score - 1)  # 0점 밑으로 내려가지 않게
        lives -= 1
        # 이 사과는 제거하므로 리스트에 추가하지 않음
        if lives <= 0:
          game_over = True
        continue

      # 2) 총알과 사과 충돌 → 점수 증가
      hit = False
      for bullet in bullets:
        if bullet.rect.colliderect(rect):
          score += 1
          bullet.kill()
          hit = True
          break

      if not hit:
        updated_apples.append(apple)

    apples = updated_apples

  # ---------------- 그리기 ----------------
  screen.fill((170, 200, 255))
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

  # 사과 그리기
  for apple in apples:
    screen.blit(apple_img, apple["rect"])

  # 스프라이트(플레이어, 총알) 그리기
  all_sprites.draw(screen)

  # 점수 표시 (좌측 상단)
  font = pygame.font.SysFont(None, 24)
  text_score = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text_score, (10, 10))

  # 목숨 표시 (우측 상단)
  text_lives = font.render(f"Lives: {lives}", True, (0, 0, 0))
  screen.blit(text_lives, (WIDTH - text_lives.get_width() - 10, 10))

  # 게임 오버 메시지
  if game_over:
    over_text = font.render("GAME OVER (Press R to Restart)", True, (255, 0, 0))
    over_x = (WIDTH - over_text.get_width()) // 2
    over_y = (HEIGHT - over_text.get_height()) // 2
    screen.blit(over_text, (over_x, over_y))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()  