"""Pygame-based ship visualization module."""

import os
import sys
import subprocess
import threading
from importlib import resources

try:
    import pygame
except ImportError:
    raise ImportError("Pygame is required for visualization features")

# Ship configurations with colors and shapes
SHIP_CONFIGS = {
    "enterprise": {
        "color": (200, 200, 255),
        "shape": [
            "          ___----___          ",
            "    ___---           ---___   ",
            " __--                     --__",
            "/                           \\",
            "|============================ |",
            "\\___________________________/",
            "   |  |                 |  |  ",
            "   |  |                 |  |  ",
            "    --                   --   "
        ]
    },
    "voyager": {
        "color": (255, 200, 200),
        "shape": [
            "         /\\               ",
            "        /  \\              ",
            "       /    \\             ",
            "      /      \\            ",
            "     /========\\           ",
            "    /==========\\          ",
            "   /============\\         ",
            "  /==============\\        ",
            " /================\\       ",
            "/==================\\      ",
            "         ||              ",
            "         ||              ",
            "         ||              ",
            "        /  \\             ",
        ]
    },
    "defiant": {
        "color": (200, 255, 200),
        "shape": [
            "       ___       ",
            "     /     \\     ",
            "    /       \\    ",
            "   /         \\   ",
            "  /===========\\  ",
            " /=============\\ ",
            "/===============\\",
            "\\_______________/",
        ]
    },
    "django": {
        "color": (150, 255, 150),
        "shape": [
            "    ____              ",
            "   /    \\             ",
            "  /      \\____________",
            " /                    \\",
            "/======================\\",
            "\\______________________/",
        ]
    },
    "flask": {
        "color": (150, 150, 255),
        "shape": [
            "    ___     ",
            "   /   \\    ",
            "  /     \\___",
            " /         \\",
            "/===========\\",
            "\\___________/",
        ]
    },
    "react": {
        "color": (100, 200, 255),
        "shape": [
            "    /\\    ",
            "   /  \\   ",
            "  /    \\  ",
            " /======\\ ",
            "/========\\",
            "\\________/",
        ]
    },
}

def display_ship_visualization(ship_name):
    """Launch a Pygame window displaying the ship with interactive commands."""
    pygame.init()
    
    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f"Starship Agentic - {ship_name.capitalize()}")
    
    # Set up colors
    BACKGROUND = (10, 10, 40)
    TEXT_COLOR = (220, 220, 220)
    BUTTON_COLOR = (60, 60, 100)
    BUTTON_HOVER = (80, 80, 120)
    BUTTON_TEXT = (240, 240, 240)
    
    # Get ship configuration or use default
    ship_config = SHIP_CONFIGS.get(ship_name.lower(), SHIP_CONFIGS["enterprise"])
    ship_color = ship_config["color"]
    ship_shape = ship_config["shape"]
    
    # Create buttons for common commands
    buttons = [
        {"rect": pygame.Rect(50, 450, 150, 40), "text": "Tour Ship", "command": "tour"},
        {"rect": pygame.Rect(230, 450, 150, 40), "text": "Commission", "command": "commission"},
        {"rect": pygame.Rect(410, 450, 150, 40), "text": "Warp Speed", "command": "warp"},
        {"rect": pygame.Rect(590, 450, 150, 40), "text": "Exit", "command": "exit"}
    ]
    
    # Set up fonts
    pygame.font.init()
    title_font = pygame.font.SysFont("Arial", 36)
    button_font = pygame.font.SysFont("Arial", 20)
    ship_font = pygame.font.SysFont("Courier New", 16)  # Monospaced font for ASCII art
    info_font = pygame.font.SysFont("Arial", 14)
    
    # Command output area
    output_text = f"Visualizing {ship_name.capitalize()} - Ready for commands"
    command_running = False
    
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not command_running:
                # Check if a button was clicked
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button["rect"].collidepoint(pos):
                        if button["command"] == "exit":
                            running = False
                        else:
                            # Run the command in a separate thread
                            command_running = True
                            output_text = f"Running command: {button['command']}..."
                            threading.Thread(
                                target=run_command, 
                                args=(button["command"], ship_name, lambda msg: set_output(msg))
                            ).start()
        
        # Clear the screen
        screen.fill(BACKGROUND)
        
        # Draw title
        title_surface = title_font.render(f"Starship {ship_name.capitalize()}", True, TEXT_COLOR)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, 30))
        
        # Draw ship ASCII art
        y_offset = 120
        for line in ship_shape:
            text_surface = ship_font.render(line, True, ship_color)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, y_offset))
            y_offset += 20
        
        # Draw command output
        output_surface = info_font.render(output_text, True, TEXT_COLOR)
        screen.blit(output_surface, (width // 2 - output_surface.get_width() // 2, 400))
        
        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            # Change color if mouse is over button
            if button["rect"].collidepoint(mouse_pos) and not command_running:
                color = BUTTON_HOVER
            else:
                color = BUTTON_COLOR
            
            pygame.draw.rect(screen, color, button["rect"], border_radius=5)
            pygame.draw.rect(screen, (100, 100, 150), button["rect"], 2, border_radius=5)
            
            # Button text
            text_surface = button_font.render(button["text"], True, BUTTON_TEXT)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            screen.blit(text_surface, text_rect)
        
        # Update the display
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

def set_output(message):
    """Update the output text (called from command thread)."""
    global output_text, command_running
    output_text = message
    command_running = False

def run_command(command, ship_name, callback):
    """Run a CLI command and update the output."""
    try:
        if command == "tour":
            result = subprocess.run(
                ["starshipagentic", "vessel", "tour-ship"], 
                capture_output=True, 
                text=True
            )
            callback(f"Tour completed: {len(result.stdout.splitlines())} templates found")
        elif command == "commission":
            result = subprocess.run(
                ["starshipagentic", "vessel", "commission-ship", ship_name, "--name", f"{ship_name}_project"], 
                capture_output=True, 
                text=True
            )
            callback(f"Ship commissioned: {ship_name}_project")
        elif command == "warp":
            callback("Warp drive engaged! Executing at maximum speed...")
            # Simulate a delay for the warp command
            import time
            time.sleep(2)
            callback("Warp complete - Ready for next command")
        else:
            callback(f"Unknown command: {command}")
    except Exception as e:
        callback(f"Error executing command: {str(e)}")
