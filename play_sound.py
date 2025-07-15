import pygame

class Config:
    sound_played = False  # 音が再生されたかどうかのフラグ

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # 再生が終わるまで待機
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def play_sound_siren(file_path):
    play_sound(file_path)
    Config.sound_played = False
