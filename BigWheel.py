import pygame
import sys
import random
import ctypes
import win32api
import win32gui
import win32con
from PIL import Image

# Initialize Pygame
pygame.init()

# Updated paths to images
foreground_path = r'C:\Users\JSiefer\Desktop\PYTHON\BigWheel\BigWheelFG.png'
background_path = r'C:\Users\JSiefer\Desktop\PYTHON\BigWheel\BigWheelBG.png'

# Load images using PIL
try:
    fg_image_pil = Image.open(foreground_path).convert('RGBA')
    bg_image_pil = Image.open(background_path).convert('RGBA')
except IOError as e:
    print(f"Unable to load image: {e}")
    sys.exit(1)

# Resize images to 50%
new_size = (fg_image_pil.width // 2, fg_image_pil.height // 2)
fg_image_pil = fg_image_pil.resize(new_size, Image.LANCZOS)
bg_image_pil = bg_image_pil.resize(new_size, Image.LANCZOS)

# Convert images to Pygame surfaces
fg_image = pygame.image.fromstring(fg_image_pil.tobytes(), fg_image_pil.size, fg_image_pil.mode)
bg_image = pygame.image.fromstring(bg_image_pil.tobytes(), bg_image_pil.size, bg_image_pil.mode)

# Get image sizes
fg_rect = fg_image.get_rect()
bg_rect = bg_image.get_rect()
size = fg_rect.size

# Set up the display
screen = pygame.display.set_mode(size, pygame.NOFRAME | pygame.SRCALPHA)
pygame.display.set_caption('Decision Wheel')
hwnd = pygame.display.get_wm_info()['window']

# Set the window to be layered and transparent
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def get_window_rect(hwnd):
    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long)]
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top, rect.right, rect.bottom

def move_window(hwnd, x, y, width, height):
    ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)

def main():
    running = True
    spinning = False
    angle = 0
    spin_speed = 20  # Initial spin speed
    min_speed = 0.1
    deceleration = 0.98  # Exponential decay factor

    clock = pygame.time.Clock()
    is_dragging = False
    offset_x = 0
    offset_y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if not spinning:
                        spinning = True
                        spin_speed = random.uniform(15, 30)  # Random initial speed
                    is_dragging = True
                    mouse_x, mouse_y = event.pos
                    window_x, window_y, _, _ = get_window_rect(hwnd)
                    offset_x = window_x - mouse_x
                    offset_y = window_y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    is_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if is_dragging:
                    mouse_x, mouse_y = event.pos
                    move_window(hwnd, mouse_x + offset_x, mouse_y + offset_y, size[0], size[1])

        if spinning:
            angle += spin_speed
            spin_speed *= deceleration

            if spin_speed <= min_speed:
                spinning = False
                spin_speed = 0

        rotated_bg = rotate_image(bg_image, angle)
        rotated_rect = rotated_bg.get_rect(center=bg_rect.center)

        screen.fill((0, 0, 0, 0))  # Fill with transparent color
        screen.blit(rotated_bg, rotated_rect.topleft)
        screen.blit(fg_image, fg_rect.topleft)
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
