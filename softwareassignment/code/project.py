import os
import numpy as np
import pygame

audio_directory = "/home/saiteja/Desktop/soft project"
pygame.mixer.init()

audio_files = [os.path.join(audio_directory, f) for f in os.listdir(audio_directory) if f.endswith(".mp3")]

for _ in range(len(audio_files)):
    np.random.shuffle(audio_files)
    paused = False

    for audio_file in audio_files:
        pygame.mixer.music.load(audio_file)
        song_name = os.path.basename(audio_file)
        pygame.mixer.music.play()
        print("Now playing:", song_name)
        while pygame.mixer.music.get_busy() or paused:
            command = input("Enter command (Pause: 1, Resume: 2, Next: 3, Quit: 4): ")
            if command == "1":
                pygame.mixer.music.pause()
                paused = True
            elif command == "2":
                pygame.mixer.music.unpause()
                paused = False
            elif command == "3":
                pygame.mixer.music.stop()
                break
            elif command == "4":
                pygame.mixer.music.stop()
                pygame.quit()
                quit()

    np.random.shuffle(audio_files)

