import pygame
from pygame import mixer
import time
import os
pygame.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]
videofolder = os.path.join(main_dir, "video")

## Long spritesheet size ##
## Height: 277, Width: 498 ##
def main():
    def make_screen():
        global screen
        screen = pygame.display.set_mode((498, 277))
        pygame.display.set_caption('Test')

    def get_image(sheet, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        return image

    def compile_images(steps):
        global animation_list
        animation_list = []
        for x in range(steps):
            animation_list.append(get_image(sprite_sheet, x, 498, 277))


    make_screen()
    sprite_sheet = pygame.image.load(os.path.join(main_dir, 'dksprite long.png')).convert_alpha()
    animation_steps = 115
    compile_images(animation_steps)
    animation_cooldown = 50
    frame = 0
    last_update = pygame.time.get_ticks()

    mixer.music.load('galleon.wav')
    mixer.music.play(-1) ## music

    while True:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0
            screen.blit(animation_list[frame], (0, 0))
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return



if __name__ == '__main__': 
    main()