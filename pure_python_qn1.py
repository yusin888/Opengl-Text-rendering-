import pygame
import sys

def draw_text(surface, font, color, text, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def main():
    pygame.init()

    global width
    width, height = 600, 300
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Text Rendering")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont("timesnewroman", 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((102, 51, 0))  # Brown background color

        # Calculate the center point for horizontal alignment
        center_x_jkuat = width // 4
        center_x_rocks = 100 + width // 4

        # Vertically center both texts
        center_y = height // 2

        # Draw text "JKUAT" in green
        draw_text(screen, font, (0, 255, 0), "JKUAT", center_x_jkuat, center_y)

        # Draw text "ROCKS" in red
        draw_text(screen, font, (255, 0, 0), "ROCKS", center_x_rocks, center_y)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
