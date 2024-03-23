import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 25

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Choose Your Own Adventure')

background_image = pygame.image.load('dungeon.jpg')
background_image = pygame.transform.scale(background_image, (800, 600))

scene2 = pygame.image.load('scene2.jpg')
scene2 = pygame.transform.scale(scene2, (800, 600))
flipped_scene2 = pygame.transform.flip(scene2, True, False)  # Flip horizontally

prisonGuards = pygame.image.load('prisonGuards.jpg')
prisonGuards = pygame.transform.scale(prisonGuards, (800, 600))

prisoner = pygame.image.load('prisoner.jpg')
prisoner = pygame.transform.scale(prisoner, (800, 600))

map = pygame.image.load('map.jpg')
map = pygame.transform.scale(map, (800, 600))

storeroom = pygame.image.load('storeroom.jpg')
storeroom = pygame.transform.scale(storeroom, (800, 600))

music = pygame.mixer.music.load('bgm.mp3')


click = pygame.mixer.Sound('click.mp3')


pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.5)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to display text on screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function for the "start" screen
def start_screen():
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, BLACK, (250, 75, 300, 50))
    draw_text("Welcome to the Adventure!", pygame.font.Font(None, 30), WHITE, SCREEN_WIDTH // 2, 100)

    # Button for starting the game
    pygame.draw.rect(screen, BLACK, (300, 200, 200, 50))
    draw_text("Start Game", pygame.font.Font(None, 30), WHITE, 400, 225)

# Function for the "choose path" screen
def choose_path_screen():
    screen.blit(background_image, (0, 0))
    draw_text("You wake up in a dark and damp dungeon, your head throbbing.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("The last thing you remember is being captured by the king's guards.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 225)
    draw_text( "You must find a way to escape before it's too late!", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 250)

    pygame.draw.rect(screen, BLACK, (250, 75, 300, 50))
    draw_text("Choose Your Path", pygame.font.Font(None, 30), WHITE, SCREEN_WIDTH // 2, 100)

    # Button for prying open
    pygame.draw.rect(screen, WHITE, (200, 300, 150, 50))
    draw_text("Pry Open", pygame.font.Font(None, FONT_SIZE), BLACK, 275, 325)

    # Button for getting the key
    pygame.draw.rect(screen, WHITE, (400, 300, 150, 50))
    draw_text("Get Key", pygame.font.Font(None, FONT_SIZE), BLACK, 475, 325)


# Function for the "outcome 1" screen
def outcome_1_screen():
    screen.blit(flipped_scene2, (0, 0))
    draw_text("With all your strength, you manage to pry open the cell door.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("You step into a dimly lit corridor.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 225)
    draw_text("To your left, you see a staircase leading up.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 250)
    draw_text( "To your right, you see a hallway stretching into darkness.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 275)

    # Button for prying open
    pygame.draw.rect(screen, WHITE, (200, 300, 150, 50))
    draw_text("Left", pygame.font.Font(None, FONT_SIZE), BLACK, 275, 325)

    # Button for getting the key
    pygame.draw.rect(screen, WHITE, (400, 300, 150, 50))
    draw_text("Right", pygame.font.Font(None, FONT_SIZE), BLACK, 475, 325)

# Function for the "outcome 2" screen
def outcome_2_screen():
    screen.blit(prisonGuards, (0, 0))
    draw_text("GAME OVER", pygame.font.Font(None, 40), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("You have been caught by the guard.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 235)
    pygame.draw.rect(screen, WHITE, (320, 300, 150, 50))
    draw_text("Exit", pygame.font.Font(None, 40), BLACK, 390, 325)

# Function for the "Left" screen
def outcome_3_screen_left():
    screen.blit(storeroom, (0, 0))
    draw_text("You climb the staircase and find yourself in a storeroom filled with crates and barrels.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("At the far end of the room, you see a ladder leading up to a trapdoor.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 225)
    draw_text("Do you search the room for useful items or climb the ladder to the trapdoor?", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 250)

    # Button for prying open
    pygame.draw.rect(screen, WHITE, (200, 300, 150, 50))
    draw_text("Search", pygame.font.Font(None, FONT_SIZE), BLACK, 275, 325)

    # Button for getting the key
    pygame.draw.rect(screen, WHITE, (400, 300, 150, 50))
    draw_text("Climb", pygame.font.Font(None, FONT_SIZE), BLACK, 475, 325)


def outcome_4_screen_right():
    screen.blit(background_image, (0, 0))
    draw_text("You make your way down the dark hallway, feeling your way along the", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("rough stone walls. Suddenly you hear footsteps approaching.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 225)
    draw_text("Do you hide in a room or confront the noise?", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 250)

    # Button for prying open
    pygame.draw.rect(screen, WHITE, (200, 300, 150, 50))
    draw_text("Hide", pygame.font.Font(None, FONT_SIZE), BLACK, 275, 325)

    # Button for getting the key
    pygame.draw.rect(screen, WHITE, (400, 300, 150, 50))
    draw_text("Confront", pygame.font.Font(None, FONT_SIZE), BLACK, 475, 325)

def outcome_5_screen_search():
    screen.blit(map, (0, 0))
    pygame.draw.rect(screen, BLACK, (120, 170, 550, 90))
    draw_text("CONGRATULATIONS", pygame.font.Font(None, 40), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("You find a map of the dungeon and find a secret passageway out!", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 235)
    # Button for exit
    pygame.draw.rect(screen, WHITE, (320, 300, 150, 50))
    draw_text("Exit", pygame.font.Font(None, 40), BLACK, 390, 325)

def outcome_6_screen_climb():
    screen.blit(prisonGuards, (0, 0))
    draw_text("GAME OVER", pygame.font.Font(None, 40), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("You climb up the trapdoor that led into the guard's room. You were caught.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 235)
    # Button for exit
    pygame.draw.rect(screen, WHITE, (320, 300, 150, 50))
    draw_text("Exit", pygame.font.Font(None, 40), BLACK, 390, 325)

def outcome_7_screen_hide():
    screen.blit(prisonGuards, (0, 0))
    draw_text("GAME OVER", pygame.font.Font(None, 40), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("You run into another room, but a guard was in there", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 235)
    draw_text("You were caught by the guard.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 255)
    # Button for exit
    pygame.draw.rect(screen, WHITE, (320, 300, 150, 50))
    draw_text("Exit", pygame.font.Font(None, 40), BLACK, 390, 325)

def outcome_8_screen_hide():
    screen.blit(prisoner, (0, 0))
    draw_text("CONGRATULATIONS", pygame.font.Font(None, 40), WHITE, SCREEN_WIDTH // 2, 200)
    draw_text("It was a fellow prisoner who knows the secret way out. Together you manage to escape.", pygame.font.Font(None, FONT_SIZE), WHITE, SCREEN_WIDTH // 2, 235)
    # Button for exit
    pygame.draw.rect(screen, WHITE, (320, 300, 150, 50))
    draw_text("Exit", pygame.font.Font(None, 40), BLACK, 390, 325)

# Main game loop
def main():
    current_screen = "start"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("Mouse position:", mouse_x, mouse_y)  # Debug: Print mouse coordinates

                if current_screen == "start":
                    if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:
                        click.play()
                        click.set_volume(0.2)
                        print("Start button clicked")  # Debug: Print button click
                        current_screen = "choose_path"
                elif current_screen == "choose_path":
                    if 200 <= mouse_x <= 350 and 300 <= mouse_y <= 350:  # Pry Open button coordinates
                        click.play()
                        print("Pry Open button clicked")  # Debug: Print button click
                        current_screen = "outcome_1"
                    elif 400 <= mouse_x <= 550 and 300 <= mouse_y <= 350:  # Get Key button coordinates
                        click.play()
                        print("Get Key button clicked")  # Debug: Print button click
                        current_screen = "outcome_2"
                elif current_screen == "outcome_2":
                    if 320 <= mouse_x <= 400 and 300 <= mouse_y <= 400:
                        click.play()
                        pygame.quit()
                        sys.exit()
                elif current_screen == "outcome_1":
                    if 200 <= mouse_x <= 300 and 300 <= mouse_y <= 350:  # Left Open button coordinates
                        click.play()
                        print("Left button clicked")  # Debug: Print button click
                        current_screen = "outcome_3"
                    elif 400 <= mouse_x <= 550 and 300 <= mouse_y <= 350:  # Get Right button coordinates
                        click.play()
                        print("Right button clicked")  # Debug: Print button click
                        current_screen = "outcome_4"
                elif current_screen == "outcome_3":
                    if 200 <= mouse_x <= 300 and 300 <= mouse_y <= 350:  # Left Open button coordinates
                        click.play()
                        print("Search button clicked")  # Debug: Print button click
                        current_screen = "outcome_5"
                    elif 400 <= mouse_x <= 550 and 300 <= mouse_y <= 350:  # Get Right button coordinates
                        click.play()
                        print("Climb button clicked")  # Debug: Print button click
                        current_screen = "outcome_6"
                elif current_screen == "outcome_5":
                    if 320 <= mouse_x <= 400 and 300 <= mouse_y <= 400:
                        click.play()
                        pygame.quit()
                        sys.exit()
                elif current_screen == "outcome_6":
                    if 320 <= mouse_x <= 400 and 300 <= mouse_y <= 400:
                        click.play()
                        pygame.quit()
                        sys.exit()
                elif current_screen == "outcome_4":
                    if 200 <= mouse_x <= 300 and 300 <= mouse_y <= 350:  # Left Open button coordinates
                        click.play()
                        print("Hide button clicked")  # Debug: Print button click
                        current_screen = "outcome_7"
                    elif 400 <= mouse_x <= 550 and 300 <= mouse_y <= 350:  # Get Right button coordinates
                        click.play()
                        print("Confront button clicked")  # Debug: Print button click
                        current_screen = "outcome_8"
                elif current_screen == "outcome_7":
                    if 320 <= mouse_x <= 400 and 300 <= mouse_y <= 400:
                        click.play()
                        pygame.quit()
                        sys.exit()
                elif current_screen == "outcome_8":
                    if 320 <= mouse_x <= 400 and 300 <= mouse_y <= 400:
                        click.play()
                        pygame.quit()
                        sys.exit()



        if current_screen == "start":
            start_screen()
        elif current_screen == "choose_path":
            choose_path_screen()
        elif current_screen == "outcome_1":
            outcome_1_screen()
        elif current_screen == "outcome_2":
            outcome_2_screen()
        elif current_screen == "outcome_3":
            outcome_3_screen_left()
        elif current_screen == "outcome_4":
            outcome_4_screen_right()
        elif current_screen == "outcome_5":
            outcome_5_screen_search()
        elif current_screen == "outcome_6":
            outcome_6_screen_climb()
        elif current_screen == "outcome_7":
            outcome_7_screen_hide()
        elif current_screen == "outcome_8":
            outcome_8_screen_hide()

        pygame.display.flip()

if __name__ == "__main__":
    main()
