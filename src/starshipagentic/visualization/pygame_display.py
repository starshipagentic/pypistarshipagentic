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

# Ship configurations with colors, shapes, and details
SHIP_CONFIGS = {
    "enterprise": {
        "color": (200, 200, 255),
        "details": "USS Enterprise NCC-1701-D\nClass: Galaxy\nCrew: 1,014\nMax Speed: Warp 9.8\nWeapons: Phasers, Photon Torpedoes\nCaptain: Jean-Luc Picard",
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
        "details": "USS Voyager NCC-74656\nClass: Intrepid\nCrew: 141\nMax Speed: Warp 9.975\nWeapons: Phasers, Photon & Quantum Torpedoes\nCaptain: Kathryn Janeway",
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
        "details": "USS Defiant NX-74205\nClass: Defiant\nCrew: 50\nMax Speed: Warp 9.5\nWeapons: Pulse Phasers, Quantum Torpedoes\nCaptain: Benjamin Sisko",
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
        "details": "Django Cruiser\nType: Web Framework\nLanguage: Python\nSpecialty: Full-stack development\nFeatures: ORM, Admin Interface, Authentication\nFounder: Adrian Holovaty & Simon Willison",
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
        "details": "Flask Scout\nType: Web Framework\nLanguage: Python\nSpecialty: Lightweight, Flexible\nFeatures: Routing, Templating, RESTful\nFounder: Armin Ronacher",
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
        "details": "React Interceptor\nType: Frontend Library\nLanguage: JavaScript\nSpecialty: UI Components\nFeatures: Virtual DOM, JSX, Component-based\nDeveloper: Facebook",
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

def display_ship_visualization(initial_ship_name):
    """Launch a Pygame window displaying the ship with interactive commands."""
    pygame.init()
    
    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    
    # Available ships and current selection
    available_ships = list(SHIP_CONFIGS.keys())
    current_ship_index = available_ships.index(initial_ship_name.lower()) if initial_ship_name.lower() in available_ships else 0
    ship_name = available_ships[current_ship_index]
    
    pygame.display.set_caption(f"Starship Agentic - {ship_name.capitalize()}")
    
    # Set up colors
    BACKGROUND = (10, 10, 40)
    TEXT_COLOR = (220, 220, 220)
    BUTTON_COLOR = (60, 60, 100)
    BUTTON_HOVER = (80, 80, 120)
    BUTTON_TEXT = (240, 240, 240)
    
    # Get ship configuration
    ship_config = SHIP_CONFIGS[ship_name]
    ship_color = ship_config["color"]
    ship_shape = ship_config["shape"]
    
    # Create buttons for common commands
    buttons = [
        {"rect": pygame.Rect(50, 450, 150, 40), "text": "Tour Ship", "command": "tour"},
        {"rect": pygame.Rect(230, 450, 150, 40), "text": "Commission", "command": "commission"},
        {"rect": pygame.Rect(410, 450, 150, 40), "text": "Warp Speed", "command": "warp"},
        {"rect": pygame.Rect(590, 450, 150, 40), "text": "Exit", "command": "exit"}
    ]
    
    # Navigation buttons
    nav_buttons = [
        {"rect": pygame.Rect(50, 250, 40, 40), "text": "<", "action": "prev_ship"},
        {"rect": pygame.Rect(710, 250, 40, 40), "text": ">", "action": "next_ship"}
    ]
    
    # Set up fonts
    pygame.font.init()
    title_font = pygame.font.SysFont("Arial", 36)
    button_font = pygame.font.SysFont("Arial", 20)
    ship_font = pygame.font.SysFont("Courier New", 16)  # Monospaced font for ASCII art
    info_font = pygame.font.SysFont("Arial", 14)
    
    # Display states
    output_text = f"Visualizing {ship_name.capitalize()} - Ready for commands"
    command_running = False
    showing_details = False
    
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                # Handle ship navigation
                for button in nav_buttons:
                    if button["rect"].collidepoint(pos):
                        if button["action"] == "prev_ship":
                            current_ship_index = (current_ship_index - 1) % len(available_ships)
                            ship_name = available_ships[current_ship_index]
                            ship_config = SHIP_CONFIGS[ship_name]
                            ship_color = ship_config["color"]
                            ship_shape = ship_config["shape"]
                            output_text = f"Switched to {ship_name.capitalize()}"
                            showing_details = False
                        elif button["action"] == "next_ship":
                            current_ship_index = (current_ship_index + 1) % len(available_ships)
                            ship_name = available_ships[current_ship_index]
                            ship_config = SHIP_CONFIGS[ship_name]
                            ship_color = ship_config["color"]
                            ship_shape = ship_config["shape"]
                            output_text = f"Switched to {ship_name.capitalize()}"
                            showing_details = False
                
                # Handle command buttons when not running a command
                if not command_running:
                    for button in buttons:
                        if button["rect"].collidepoint(pos):
                            if button["command"] == "exit":
                                running = False
                            elif button["command"] == "tour" and not showing_details:
                                # Show ship details instead of running tour command
                                showing_details = True
                                output_text = f"Showing details for {ship_name.capitalize()}"
                            else:
                                # Run the command in a separate thread
                                command_running = True
                                output_text = f"Running command: {button['command']}..."
                                threading.Thread(
                                    target=run_command, 
                                    args=(button["command"], ship_name, lambda msg: set_output(msg))
                                ).start()
                                showing_details = False
        
        # Clear the screen
        screen.fill(BACKGROUND)
        
        # Draw title
        title_surface = title_font.render(f"Starship {ship_name.capitalize()}", True, TEXT_COLOR)
        screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, 30))
        
        # Draw ship or ship details
        if showing_details:
            # Draw ship details
            detail_lines = ship_config["details"].split('\n')
            y_offset = 120
            for line in detail_lines:
                text_surface = ship_font.render(line, True, ship_color)
                screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, y_offset))
                y_offset += 30
        else:
            # Draw ship ASCII art
            y_offset = 120
            for line in ship_shape:
                text_surface = ship_font.render(line, True, ship_color)
                screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, y_offset))
                y_offset += 20
        
        # Draw command output
        output_surface = info_font.render(output_text, True, TEXT_COLOR)
        screen.blit(output_surface, (width // 2 - output_surface.get_width() // 2, 400))
        
        # Draw navigation buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in nav_buttons:
            if button["rect"].collidepoint(mouse_pos):
                color = BUTTON_HOVER
            else:
                color = BUTTON_COLOR
            
            pygame.draw.rect(screen, color, button["rect"], border_radius=5)
            pygame.draw.rect(screen, (100, 100, 150), button["rect"], 2, border_radius=5)
            
            text_surface = button_font.render(button["text"], True, BUTTON_TEXT)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            screen.blit(text_surface, text_rect)
        
        # Draw command buttons
        for button in buttons:
            # Change color if mouse is over button
            if button["rect"].collidepoint(mouse_pos) and not command_running:
                color = BUTTON_HOVER
            else:
                color = BUTTON_COLOR
            
            # Special handling for Tour button when showing details
            if button["command"] == "tour" and showing_details:
                text = "Back"
            else:
                text = button["text"]
            
            pygame.draw.rect(screen, color, button["rect"], border_radius=5)
            pygame.draw.rect(screen, (100, 100, 150), button["rect"], 2, border_radius=5)
            
            # Button text
            text_surface = button_font.render(text, True, BUTTON_TEXT)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            screen.blit(text_surface, text_rect)
        
        # Update the display
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

def set_output(message):
    """Update the output text (called from command thread)."""
    global output_text, command_running, showing_details
    output_text = message
    command_running = False
    showing_details = False  # Return to ship view after command completes

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
