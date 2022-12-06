""" COP 3502c -- Project 4: Sudoku
---> GROUP 102 <---
Created by: Harper Fuchs, Blake Wood, Devin Wylde, and Maddy Wirbel
Due Date: December 6th, 2022 """

import pygame, sys
from pygame.locals import QUIT

from color import ColorClass
from button import Button

from board import Board
from sudoku_generator import SudokuGenerator, generate_sudoku

Color = ColorClass()
# creates an instance of ColorClass, allowing presaved colors to be used
leaderboard = []
# creates an empty list to be filled and displayed as a leaderboard

if __name__ == '__main__':
    pygame.init()

    WIDTH, HEIGHT = 630, 580
  # WIDTH, HEIGHT are the dimensions of the board
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    difficulty = 1
    font_sm = pygame.font.Font('fonts/freesansbold.ttf', 24)
    font = pygame.font.Font('fonts/freesansbold.ttf', 32)
    font_lg = pygame.font.Font('fonts/freesansbold.ttf', 48)
  # 3 font sizes are created

    title_text = font_lg.render("Sudoku", True, (20, 0, 0))

    menu_buttons = []
    menu_buttons.append(
        Button(Color.White, pygame.Rect(WIDTH / 2 - 150, 210, 300, 100), 5,
               font.render("Play", True, (0, 0, 0))))
    menu_buttons.append(
        Button(Color.Light_Gray, pygame.Rect(WIDTH / 2 - 150, 330, 300, 100),
               5, font.render("Leaderboard", True, (0, 0, 0))))
  # creates the buttons for the main menu

    difficulty_colors = [Color.Light_Green, Color.Light_Yellow, Color.Light_Red]
    
    mode_buttons = []
    mode_buttons.append(Button(Color.Light_Green, pygame.Rect(WIDTH/2-150, 170, 300, 100), 5, font.render("Easy", True, (0, 0, 0))))
    mode_buttons.append(Button(Color.Light_Yellow, pygame.Rect(WIDTH/2-150, 290, 300, 100), 5, font.render("Medium", True, (0, 0, 0))))
    mode_buttons.append(Button(Color.Light_Red, pygame.Rect(WIDTH/2-150, 410, 300, 100), 5, font.render("Hard", True, (0, 0, 0))))
  # makes the buttons for easy, medium, and hard game modes

    submit_button = Button(Color.Light_Green, pygame.Rect(WIDTH / 2 - 100, 400, 200, 100), 6, font.render('Submit', True, (0, 0, 0)))

    submit_button_gray = Button(Color.Light_Gray, pygame.Rect(WIDTH / 2 - 100, 400, 200, 100), 6, font.render('Submit', True, (0, 0, 0)))

    enter_name_font = font.render('Enter name', True, (40, 40, 40))
  # sets a font for the user to enter their name

    empty_font = font.render('Leaderboard is Empty', True, (0, 0, 0))
  # creates text to display when the leaderboard is empty

    font_nums = []
    font_set_nums = []
    font_ordinals = []
    for i in range(1, 11):
        if i < 10:
            font_nums.append(font_sm.render(str(i), True, Color.Dark_Gray))
            font_set_nums.append(font.render(str(i), True, Color.Black))
        font_ordinals.append(font_sm.render(str(i) + '.  ', True, Color.Black))

    back_button = Button(Color.Light_Orange, pygame.Rect(10, 10, 30, 30), 2, pygame.transform.scale(pygame.image.load('imgs/back.png').convert_alpha(), (20, 20)))
    reset_button = Button(Color.Light_Blue, pygame.Rect(WIDTH - 80, 10, 30, 30), 2, pygame.transform.scale(pygame.image.load('imgs/reset.png').convert_alpha(), (20, 20)))
    exit_button = Button(Color.Light_Red, pygame.Rect(WIDTH - 40, 10, 30, 30), 2, pygame.transform.scale(pygame.image.load('imgs/exit.png').convert_alpha(), (20, 20)))
  # sets the back button, reset button, and exit button

    win_font = font.render("You win!", True, (0, 40, 0))
    lose_font = font.render("You lose!", True, (40, 0, 0))
    
    play_again_button = Button(Color.White, pygame.Rect(WIDTH / 2 - 160, HEIGHT/2-50, 320, 100), 5, font.render("Play again?", True, (0, 0, 0)))

    mouse_pos = pygame.Vector2()
    mouse_up = False
    mouse_down = False
    click = False
    unclick = False
    run = True
    
    while run:
      # starts running the program... continues until the user stops it
        stage = 0
        menu_state = 0
        player_name = ''
    
        # sort leaderboard
        leaderboard.sort(key=lambda x: x[0])
    
        while stage == 0:
            # start menu loop
            mouse_pos.x, mouse_pos.y = pygame.mouse.get_pos()
    
            # resets click and unclick (should only last for 1 loop)
            if mouse_down:
                click = False
            elif mouse_up:
                unclick = False
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage = -1
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu_state = 0
                    elif menu_state == 1:
                        if event.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        elif len(player_name) <= 10 and event.unicode.isalnum():
                            player_name += event.unicode
                        player_name_font = font.render(player_name, True, Color.Black)
                elif event.type == pygame.MOUSEBUTTONDOWN and (not mouse_down):
                  # elif statement for if the user clicks the screen (when the mouse gets pressed)
                    click = True
                    mouse_down = True
                    mouse_up = False
                elif event.type == pygame.MOUSEBUTTONUP:
                  # elif statement for when the user releases the mouse (from clicking)
                    unclick = True
                    mouse_down = False
                    mouse_up = True
    
            # set screen background
            screen.fill(Color.Purple_Blue)
            # draw title
            screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 80))
    
            if menu_state == 0:
                # draw menu buttons
                for idx, button in enumerate(menu_buttons):
                    button.draw(screen, (mouse_down and button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
                    if unclick and button.rect.collidepoint(mouse_pos.x, mouse_pos.y):
                        menu_state = idx + 1
            elif menu_state == 1:
                if len(player_name) == 0:
                    submit_button_gray.draw(screen, False)
                    screen.blit(enter_name_font, (WIDTH/2 - enter_name_font.get_width()/2, HEIGHT/2 - enter_name_font.get_height()/2))
                else:
                    submit_button.draw(screen, (mouse_down and submit_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
                    screen.blit(player_name_font, (WIDTH/2 - player_name_font.get_width()/2, HEIGHT/2 - player_name_font.get_height()/2))
                  # writes the player's name in the leaderboard
                    if pygame.key.get_pressed()[pygame.K_RETURN] or (unclick and submit_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)):
                        menu_state = 3
            elif menu_state == 2:
                if len(leaderboard) == 0:
                    screen.blit(empty_font, (WIDTH/2 - empty_font.get_width()/2, HEIGHT/2 - empty_font.get_height()/2))
                for i in range(0, min(len(leaderboard), 10)):
                    screen.blit(font_ordinals[i], (40, i*32+160))
                    screen.blit(leaderboard[i][3], (80, i*32+160))
            elif menu_state == 3:
                for idx, button in enumerate(mode_buttons):
                    button.draw(screen, (mouse_down and button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
                    if unclick and button.rect.collidepoint(mouse_pos.x, mouse_pos.y):
                        difficulty = idx
                      # sets the difficulty of the game
                        stage = 1
                
    
            # "publish" screen
            pygame.display.flip()
    
        board, init_board = generate_sudoku(9, difficulty*10+30)
        filled = False
        win = False
        selected = [-1, -1]
        start_time = pygame.time.get_ticks()
    
        while stage == 1:
            mouse_pos.x, mouse_pos.y = pygame.mouse.get_pos()
    
            # resets click and unclick (should only last for 1 loop)
            if mouse_down:
                click = False
            elif mouse_up:
                unclick = False
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage = -1
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and (not mouse_down):
                    click = True
                    mouse_down = True
                    mouse_up = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    unclick = True
                    mouse_down = False
                    mouse_up = True
                elif event.type == pygame.KEYDOWN and not (-1 in selected):
                    # for arrow keys (move selection)
                    arrow_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
                    checks = [lambda a : a > 0, lambda a : a < 8]
                    for i in range(0, 4):
                        if event.key == arrow_keys[i]:
                            if 0 <= (selected[i//2] + (-1 if (i%2 == 0) else 1)) <= 8:
                                selected[i//2] += -1 if (i%2 == 0) else 1
                            else:
                                selected[i//2] = 8 if (i%2 == 0) else 0
    
                    # escape removes selected tile
                    if event.key == pygame.K_ESCAPE:
                        selected = [-1, -1]
                    # tab moves selection logically
                    elif event.key == pygame.K_TAB:
                        if selected == [8, 8]:
                            selected = [0, 0]
                        else:
                            board.iterate_by_box(selected)
                    
                    elif event.key == pygame.K_BACKSPACE:
                        if board.boxes[selected[0]][selected[1]].is_editable:
                            board.boxes[selected[0]][selected[1]].value = -1
                    elif event.key == pygame.K_RETURN:
                        if board.boxes[selected[0]][selected[1]].value != -1 and board.boxes[selected[0]][selected[1]].is_editable:
                            board.boxes[selected[0]][selected[1]].is_perm = True
                
                            filled = board.check_filled()
                            if filled:
                              # checks if the game has been won once the board is full
                                win = board.check_win(init_board)
                                stage = 2
                    else:
                        typed = event.unicode
                        if typed.isnumeric() and int(typed) != 0 and int(typed) != board.boxes[selected[0]][selected[1]].value and board.boxes[selected[0]][selected[1]].is_editable:
                            board.boxes[selected[0]][selected[1]].value = int(typed)
    
            screen.fill(Color.Purple_Blue)
        
            for row in board.boxes:
                for tile in row:
                    tile.draw(screen, font_set_nums if (tile.is_perm) else font_nums, mouse_pos, (selected == tile.loc))
                    
                    if tile.rect.collidepoint(mouse_pos.x, mouse_pos.y) and click:
                      # sets the selected cell based on the user's selection  
                      selected = tile.loc.copy()
    
            back_button.draw(screen, (mouse_down and back_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
    
            if (unclick and back_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)):
                stage = 0
            
            reset_button.draw(screen, (mouse_down and reset_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
    
            if (unclick and reset_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)):
                board.reset_to_original()
            
            exit_button.draw(screen, (mouse_down and exit_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
    
            if (unclick and exit_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)):
                stage = -1
                run = False
            
            # "publish" screen
            pygame.display.flip()
    
        # create a transparent green box to fade in when won
        game_end_gradient = pygame.Surface((WIDTH, HEIGHT))
        game_end_gradient.set_alpha(0)
    
        # saves score to leaderboard
        if win:
            time_elapsed = (pygame.time.get_ticks() - start_time) // 1000
            display_time, time_type = time_elapsed, ' secs'
            if display_time >= 100:
                display_time, time_type = round(time_elapsed / 60, 1), ' mins'
            if display_time >= 10:
                display_time //= 1
            leaderboard.append([time_elapsed, player_name, difficulty, font_sm.render(player_name + ' - ' + str(display_time) + time_type, True, difficulty_colors[difficulty])])
            print(leaderboard)
    
        while stage == 2:
            mouse_pos.x, mouse_pos.y = pygame.mouse.get_pos()
    
            # resets click and unclick (should only last for 1 loop)
            if mouse_down:
                click = False
            elif mouse_up:
                unclick = False
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage = -1
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN and (not mouse_down):
                    click = True
                    mouse_down = True
                    mouse_up = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    unclick = True
                    mouse_down = False
                    mouse_up = True
            
            if game_end_gradient.get_alpha() == 0:
                # fills the gradient with appropriate color
                game_end_gradient.fill((0, 255, 0) if (win) else (255, 0, 0))
    
            # draw background behind win/lose screen
            screen.fill(Color.Purple_Blue)
        
            for row in board.boxes:
                for tile in row:
                    tile.draw(screen, font_set_nums, mouse_pos, False)
    
            back_button.draw(screen, False)
            reset_button.draw(screen, False)
            exit_button.draw(screen, False)
    
            # draws fade-in color
            screen.blit(game_end_gradient, (0, 0))
                
            if game_end_gradient.get_alpha() < 128:
                # increase opacity of win background
                game_end_gradient.set_alpha(game_end_gradient.get_alpha() + 1)
            else:
                pygame.draw.rect(screen, (200, 255, 200) if (win) else (255, 200, 200), (WIDTH/2-120, 120, 240, 80), border_radius=20)
                screen.blit(win_font if (win) else lose_font, (WIDTH / 2 - win_font.get_width() / 2, 160 - win_font.get_height()/2))
                play_again_button.draw(screen, (mouse_down and play_again_button.rect.collidepoint(mouse_pos.x, mouse_pos.y)))
                if unclick and play_again_button.rect.collidepoint(mouse_pos.x, mouse_pos.y):
                    stage = 0
    
            # "publish" screen
            pygame.display.flip()
    
    pygame.quit()
    sys.exit()
