import pygame
import sys
import random


def load_words_from_file(filename):
    word_list = []
    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(":", maxsplit=1)
                word = parts[0].upper()
                explanation = parts[1] if len(parts) > 1 else ""
                word_list.append((word, explanation))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return word_list


pygame.init()
# Get current screen size
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
WINDOW = pygame.display.set_mode((WIDTH - 100, HEIGHT - 100), pygame.RESIZABLE)

pygame.display.set_caption("Poomis mäng / Hangman Game")
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont("comicsans", 40)
# Set up Button
RADIUS = 30
GAP = 20
ALL_LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÕÜ")
# Word setup
estonian_words = load_words_from_file("estonian_words.txt")
if not estonian_words:
    print("No words loaded! Check your file.")

guessed = set()
hangman_status = 0


def draw_hangman(status, center_x, top_y):
    base_y = top_y + 80  # Hangman 80px below letter buttons

    # Structure
    pygame.draw.line(
        WINDOW, BLACK, (center_x - 150, base_y), (center_x + 150, base_y), 5
    )  # Base
    pygame.draw.line(
        WINDOW, BLACK, (center_x, base_y), (center_x, base_y - 300), 5
    )  # Pole
    pygame.draw.line(
        WINDOW, BLACK, (center_x, base_y - 300), (center_x + 100, base_y - 300), 5
    )  # Top bar
    pygame.draw.line(
        WINDOW, BLACK, (center_x + 100, base_y - 300), (center_x + 100, base_y - 250), 5
    )  # Rope

    if status > 0:
        pygame.draw.circle(
            WINDOW, (0, 0, 0), (center_x + 100, base_y - 220), 30, 3
        )  # Head
    if status > 1:
        pygame.draw.line(
            WINDOW,
            (0, 0, 0),
            (center_x + 100, base_y - 190),
            (center_x + 100, base_y - 100),
            3,
        )  # Body
    if status > 2:
        pygame.draw.line(
            WINDOW,
            (0, 0, 0),
            (center_x + 100, base_y - 170),
            (center_x + 60, base_y - 130),
            3,
        )  # Left arm
    if status > 3:
        pygame.draw.line(
            WINDOW,
            (0, 0, 0),
            (center_x + 100, base_y - 170),
            (center_x + 140, base_y - 130),
            3,
        )  # Right arm
    if status > 4:
        pygame.draw.line(
            WINDOW,
            (0, 0, 0),
            (center_x + 100, base_y - 100),
            (center_x + 60, base_y - 40),
            3,
        )  # Left leg
    if status > 5:
        pygame.draw.line(
            WINDOW,
            (0, 0, 0),
            (center_x + 100, base_y - 100),
            (center_x + 140, base_y - 40),
            3,
        )  # Right leg


def generate_letter_positions(win_width):
    letters = []
    total_per_row = 13
    rows = [
        ALL_LETTERS[i : i + total_per_row]
        for i in range(0, len(ALL_LETTERS), total_per_row)
    ]
    starty = 300

    for row_index, row_letters in enumerate(rows):
        row_width = len(row_letters) * (RADIUS * 2 + GAP)
        startx = (win_width - row_width) // 2
        y = starty + ((GAP + RADIUS * 2) * row_index)
        for col_index, char in enumerate(row_letters):
            x = startx + (RADIUS * 2 + GAP) * col_index + RADIUS
            letters.append([x, y, char, True])

    bottom_y = starty + (len(rows) - 1) * (GAP + RADIUS * 2) + RADIUS
    return letters, bottom_y


def display_message(message, explanation=""):
    pygame.time.delay(500)
    WINDOW.fill(GRAY)
    font = pygame.font.SysFont("arial", 60)
    text = font.render(message, True, BLACK)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    WINDOW.blit(text, rect)

    if explanation:
        font_expl = pygame.font.SysFont("arial", 30)
        exp_text = font_expl.render(f"Sõna tähendus: {explanation}", True, BLACK)
        rect_exp = exp_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        WINDOW.blit(exp_text, rect_exp)

    font_small = pygame.font.SysFont("arial", 28)
    instructions = font_small.render(
        "Press [R] to play again or [ESC] to quit", True, BLACK
    )
    rect2 = instructions.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
    WINDOW.blit(instructions, rect2)

    pygame.display.update()
    wait_for_restart()


def wait_for_restart():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


def main():
    global guessed, hangman_status, word, WIDTH, HEIGHT, WINDOW

    word, explanation = random.choice(estonian_words)
    guessed = set()
    for char in word:
        if (
            not char.isalpha()
        ):  # Automatically reveal non-letter characters like '-' or spaces
            guessed.add(char)

    hangman_status = 0

    running = True
    letters, letter_bottom_y = generate_letter_positions(WINDOW.get_width())
    while running:
        WINDOW.fill(GRAY)
        window_width = WINDOW.get_width()

        # Draw word
        display_word = " ".join([ltr if ltr in guessed else "_" for ltr in word])
        text = FONT.render(display_word, True, BLACK)
        WINDOW.blit(text, (window_width // 2 - text.get_width() // 2, 100))

        # Draw buttons
        for x, y, ltr, visible in letters:
            if visible:
                pygame.draw.circle(WINDOW, WHITE, (x, y), RADIUS)
                pygame.draw.circle(WINDOW, BLACK, (x, y), RADIUS, 3)
                letter_text = FONT.render(ltr, True, BLACK)
                WINDOW.blit(
                    letter_text,
                    (
                        x - letter_text.get_width() // 2,
                        y - letter_text.get_height() // 2,
                    ),
                )

        # Draw hangman
        row_count = 3
        starty = (
            300  # Make sure this matches the value used in generate_letter_positions
        )
        letters_y_bottom = starty + (row_count - 1) * (GAP + RADIUS * 2)
        spacing = 350  # You can adjust this if needed
        hangman_y_top = letters_y_bottom + spacing
        center_x = WINDOW.get_width() // 2

        draw_hangman(hangman_status, center_x, hangman_y_top)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                letters, letter_bottom_y = generate_letter_positions(WINDOW.get_width())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dist = ((x - mx) ** 2 + (y - my) ** 2) ** 0.5
                        if dist < RADIUS:
                            guessed.add(ltr)
                            letter[3] = False  # set visible = False
                            if ltr not in word:
                                hangman_status += 1

        if all(letter in guessed for letter in word):
            display_message("You won!", explanation)
        elif hangman_status == 6:
            display_message(f"You lost! The word was: {word}", explanation)

    pygame.quit()
    sys.exit()


main()
