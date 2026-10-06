import random

import pygame


BELTS = ["Hassas", "Ağır", "Standart"]


def create_package():
    return {
        "weight": random.randint(1, 15),
        "fragile": random.choice([True, False]),
    }


def choose_belt(package):
    if package["fragile"]:
        return "Hassas"
    elif package["weight"] >= 10:
        return "Ağır"
    else:
        return "Standart"


def draw_button(screen, belt, rectangle, font):
    color = (222, 234, 236)
    if rectangle.collidepoint(pygame.mouse.get_pos()):
        color = (199, 220, 223)

    pygame.draw.rect(screen, color, rectangle, border_radius=12)
    text = font.render(belt, True, (35, 65, 71))
    screen.blit(text, text.get_rect(center=rectangle.center))


def draw_screen(screen, fonts, buttons, package, score, message,
                message_color):
    title_font, text_font, small_font = fonts
    screen.fill((247, 249, 247))

    title = title_font.render("Parcel Planet", True, (35, 65, 71))
    screen.blit(title, (32, 22))
    score_text = text_font.render(f"Skor: {score}", True, (35, 65, 71))
    screen.blit(score_text, score_text.get_rect(topright=(808, 30)))
    instruction = small_font.render(
        "Etiketi oku, kuralları uygula ve doğru bandı seç.", True, (86, 106, 111)
    )
    screen.blit(instruction, (32, 75))

    pygame.draw.rect(screen, (232, 239, 235), (32, 115, 776, 110), border_radius=10)
    rules = [
        "1. Kırılgan paket: Hassas bant (ağır olsa bile).",
        "2. Kırılgan değilse ve en az 10 kg ise: Ağır bant.",
        "3. Diğer paketler: Standart bant.",
    ]
    for index, rule in enumerate(rules):
        rule_text = small_font.render(rule, True, (35, 65, 71))
        screen.blit(rule_text, (50, 128 + index * 30))

    package_rectangle = pygame.Rect(270, 250, 300, 200)
    pygame.draw.rect(screen, (216, 181, 134), package_rectangle, border_radius=8)
    pygame.draw.rect(screen, (239, 213, 177), (395, 250, 50, 200))
    pygame.draw.rect(screen, (176, 140, 96), package_rectangle, 2, border_radius=8)
    pygame.draw.rect(screen, (255, 252, 245), (290, 302, 260, 110), border_radius=5)
    weight = text_font.render(f"Ağırlık: {package['weight']} kg", True, (35, 65, 71))
    screen.blit(weight, weight.get_rect(center=(420, 334)))
    if package["fragile"]:
        fragile_label = "Kırılgan: Evet"
    else:
        fragile_label = "Kırılgan: Hayır"
    fragile_text = text_font.render(fragile_label, True, (35, 65, 71))
    screen.blit(fragile_text, fragile_text.get_rect(center=(420, 379)))

    feedback = small_font.render(message, True, message_color)
    screen.blit(feedback, feedback.get_rect(center=(420, 490)))
    for belt, rectangle in buttons:
        draw_button(screen, belt, rectangle, text_font)

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((840, 620))
    pygame.display.set_caption("Parcel Planet")
    fonts = (
        pygame.font.SysFont("arial", 36, bold=True),
        pygame.font.SysFont("arial", 27),
        pygame.font.SysFont("arial", 20),
    )
    buttons = []
    for index, belt in enumerate(BELTS):
        rectangle = pygame.Rect(32 + index * 264, 535, 248, 60)
        buttons.append((belt, rectangle))

    package = create_package()
    score = 0
    message = ""
    message_color = (35, 65, 71)
    message_until = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for selected_belt, rectangle in buttons:
                    if rectangle.collidepoint(event.pos):
                        if selected_belt == choose_belt(package):
                            score += 1
                            message = "Doğru! Yeni paket hazır."
                            message_color = (41, 115, 78)
                            package = create_package()
                        else:
                            message = "Tekrar dene: önce kırılganlığı, sonra ağırlığı kontrol et."
                            message_color = (160, 68, 48)
                        message_until = pygame.time.get_ticks() + 2500
                        break

        if pygame.time.get_ticks() >= message_until:
            message = ""

        draw_screen(
            screen, fonts, buttons, package, score, message,
            message_color
        )
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
