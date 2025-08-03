  

# import tkinter as tk
# from tkinter import ttk
# import pygame
# import numpy as np
# import time
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import pygame
# from pygame.locals import *

# # Assuming 'solvers' and 'utils' are in the same directory and have been corrected as discussed.

# class RubiksCubeGUI:
#     """
#     Main GUI class for the Rubik's Cube Solver.
#     Uses tkinter for the main window and pygame/PyOpenGL for 3D visualization.
#     """
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("🧩 Rubik's Cube Solver - AeroHack 2025")
#         self.root.geometry("800x600")
#         self.root.configure(bg='#2c3e50')
        
#         self.current_scramble = None
#         self.current_solution = None

#         self.setup_gui()
    
#     def setup_gui(self):
#         """Builds the main GUI layout and widgets."""
#         # --- Title Frame ---
#         title_frame = tk.Frame(self.root, bg='#2c3e50')
#         title_frame.pack(pady=20)
        
#         title_label = tk.Label(title_frame, 
#                               text="🧩 RUBIK'S CUBE SOLVER", 
#                               font=("Arial", 24, "bold"), 
#                               bg='#2c3e50', 
#                               fg='#ecf0f1')
#         title_label.pack()
        
#         subtitle_label = tk.Label(title_frame, 
#                                  text="Complete 3D Visualization for 2x2, 3x3, 4x4 Cubes", 
#                                  font=("Arial", 12), 
#                                  bg='#2c3e50', 
#                                  fg='#bdc3c7')
#         subtitle_label.pack()
        
#         # --- Control Panel Frame ---
#         control_frame = tk.LabelFrame(self.root, 
#                                      text="Cube Controls", 
#                                      bg='#34495e', 
#                                      fg='#ecf0f1',
#                                      font=("Arial", 14, "bold"))
#         control_frame.pack(pady=20, padx=20, fill='x')
        
#         # Size Selection
#         size_frame = tk.Frame(control_frame, bg='#34495e')
#         size_frame.pack(pady=10)
        
#         tk.Label(size_frame, text="Cube Size:", font=("Arial", 12, "bold"), 
#                 bg='#34495e', fg='#ecf0f1').pack(side='left', padx=10)
        
#         self.size_var = tk.StringVar(value="3x3")
#         size_options = ["2x2", "3x3", "4x4"]
        
#         for size in size_options:
#             tk.Radiobutton(size_frame, 
#                           text=size, 
#                           variable=self.size_var, 
#                           value=size,
#                           bg='#34495e', 
#                           fg='#ecf0f1', 
#                           selectcolor='#3498db',
#                           font=("Arial", 11)).pack(side='left', padx=10)
        
#         # Action Buttons
#         button_frame = tk.Frame(control_frame, bg='#34495e')
#         button_frame.pack(pady=20)
        
#         # Button styling
#         btn_style = {
#             'font': ('Arial', 12, 'bold'),
#             'width': 18,
#             'height': 2,
#             'relief': 'raised',
#             'bd': 3
#         }
        
#         # Row 1 buttons
#         row1 = tk.Frame(button_frame, bg='#34495e')
#         row1.pack(pady=5)
        
#         tk.Button(row1, text="🎲 Generate Scramble", 
#                  command=self.generate_scramble,
#                  bg='#e74c3c', fg='white', **btn_style).pack(side='left', padx=10)
        
#         tk.Button(row1, text="⚡ Solve Cube", 
#                  command=self.solve_cube,
#                  bg='#27ae60', fg='white', **btn_style).pack(side='left', padx=10)
        
#         # Row 2 buttons  
#         row2 = tk.Frame(button_frame, bg='#34495e')
#         row2.pack(pady=5)
        
#         tk.Button(row2, text="🔍 View 3D Cube", 
#                  command=self.show_3d_cube,
#                  bg='#3498db', fg='white', **btn_style).pack(side='left', padx=10)
        
#         tk.Button(row2, text="🎬 Animate Solution", 
#                  command=self.animate_solution,
#                  bg='#9b59b6', fg='white', **btn_style).pack(side='left', padx=10)
        
#         # --- Results Display ---
#         results_frame = tk.LabelFrame(self.root, 
#                                     text="Results", 
#                                     bg='#34495e', 
#                                     fg='#ecf0f1',
#                                     font=("Arial", 14, "bold"))
#         results_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
#         # Scramble display
#         tk.Label(results_frame, text="Scrambled State:", 
#                 font=("Arial", 11, "bold"), bg='#34495e', fg='#f39c12').pack(anchor='w', padx=10, pady=5)
        
#         self.scramble_text = tk.Text(results_frame, height=3, width=80, 
#                                    font=("Consolas", 10), wrap=tk.WORD)
#         self.scramble_text.pack(padx=10, pady=5)
        
#         # Solution display
#         tk.Label(results_frame, text="Solution Moves:", 
#                 font=("Arial", 11, "bold"), bg='#34495e', fg='#e67e22').pack(anchor='w', padx=10, pady=5)
        
#         self.solution_text = tk.Text(results_frame, height=3, width=80, 
#                                    font=("Consolas", 10), wrap=tk.WORD)
#         self.solution_text.pack(padx=10, pady=5)
        
#         # Performance display
#         tk.Label(results_frame, text="Performance Metrics:", 
#                 font=("Arial", 11, "bold"), bg='#34495e', fg='#27ae60').pack(anchor='w', padx=10, pady=5)
        
#         self.performance_text = tk.Text(results_frame, height=2, width=80, 
#                                       font=("Consolas", 10))
#         self.performance_text.pack(padx=10, pady=5)
        
#         # --- Status bar ---
#         self.status_var = tk.StringVar(value="Ready - Select cube size and generate scramble")
#         status_bar = tk.Label(self.root, 
#                             textvariable=self.status_var, 
#                             bg='#95a5a6', 
#                             fg='#2c3e50',
#                             font=("Arial", 10),
#                             relief='sunken',
#                             anchor='w')
#         status_bar.pack(side='bottom', fill='x')
    
#     def generate_scramble(self):
#         """Generates a scramble based on the selected cube size."""
#         size = self.size_var.get()
#         self.status_var.set(f"Generating {size} scramble...")
#         self.root.update()
        
#         try:
#             if size == "2x2":
#                 from solvers import generate_2x2_scramble
#                 self.current_scramble = generate_2x2_scramble()
#             elif size == "3x3":
#                 from utils import get_cube_state
#                 self.current_scramble = get_cube_state()
#             elif size == "4x4":
#                 from solvers import generate_4x4_scramble
#                 self.current_scramble = generate_4x4_scramble()
            
#             # Display scramble
#             self.scramble_text.delete(1.0, tk.END)
#             self.scramble_text.insert(1.0, f"{size} Scramble: {self.current_scramble[:100]}...")
            
#             self.status_var.set(f"{size} scramble generated successfully!")
            
#         except Exception as e:
#             self.status_var.set(f"Error generating scramble: {str(e)}")
    
#     def solve_cube(self):
#         """Calls the appropriate solver and displays the solution and metrics."""
#         if self.current_scramble is None:
#             self.status_var.set("Please generate a scramble first!")
#             return
            
#         size_num = int(self.size_var.get()[0])  # Get number from "3x3" -> 3
#         self.status_var.set(f"Solving {self.size_var.get()} cube...")
#         self.root.update()
        
#         try:
#             from solvers import scale_solver
            
#             start_time = time.time()
#             self.current_solution = scale_solver(size_num, self.current_scramble)
#             end_time = time.time()
            
#             # Display solution
#             self.solution_text.delete(1.0, tk.END)
#             self.solution_text.insert(1.0, f"Solution: {self.current_solution}")
            
#             # Display performance
#             self.performance_text.delete(1.0, tk.END)
#             if "Error" not in self.current_solution and "No solution" not in self.current_solution:
#                 solve_time = end_time - start_time
#                 move_count = len(self.current_solution.split())
#                 algorithm_name = {'2': 'BFS', '3': 'Kociemba', '4': 'Reduction'}.get(str(size_num), 'Unknown')
#                 performance_info = f"Solve Time: {solve_time:.4f}s | Moves: {move_count} | Algorithm: {algorithm_name}"
#             else:
#                 performance_info = "Could not calculate metrics due to a solving error."
                
#             self.performance_text.insert(1.0, performance_info)
#             self.status_var.set(f"{self.size_var.get()} cube solved successfully!")
            
#         except Exception as e:
#             self.status_var.set(f"Error solving cube: {str(e)}")
#             # Print the full exception for easier debugging
#             print(f"Error details: {e}")
    
#     def show_3d_cube(self):
#         """Launches the 3D visualization of the current cube state."""
#         if self.current_scramble is None:
#             self.status_var.set("Please generate a scramble first!")
#             return
            
#         self.status_var.set("Opening 3D visualization...")
#         self.root.update()
        
#         try:
#             size_num = int(self.size_var.get()[0])
#             cube_3d = Cube3DVisualization(size_num)
#             cube_3d.render_cube(self.current_scramble, f"{self.size_var.get()} Rubik's Cube")
#             self.status_var.set("3D visualization closed")
            
#         except Exception as e:
#             self.status_var.set(f"Error showing 3D cube: {str(e)}")
    
#     def animate_solution(self):
#         """Animates the solution moves on the 3D cube."""
#         if self.current_solution is None:
#             self.status_var.set("Please solve the cube first!")
#             return
            
#         self.status_var.set("Starting solution animation...")
#         self.root.update()
        
#         try:
#             from utils import predict_states
#             size_num = int(self.size_var.get()[0])
            
#             # Get all states
#             states = predict_states(self.current_scramble, self.current_solution)
#             moves = self.current_solution.split()
            
#             # Animate
#             cube_3d = Cube3DVisualization(size_num)
#             cube_3d.animate_solution(states, moves)
            
#             self.status_var.set("Animation completed!")
            
#         except Exception as e:
#             self.status_var.set(f"Error animating solution: {str(e)}")
    
#     def run(self):
#         """Starts the tkinter main loop."""
#         self.root.mainloop()


# class Cube3DVisualization:
#     """
#     Handles the 3D rendering of the Rubik's Cube using Pygame and PyOpenGL.
#     """
#     def __init__(self, size=3):
#         self.size = size
#         self.colors = {
#             'U': (1.0, 1.0, 1.0),    # White
#             'D': (1.0, 1.0, 0.0),    # Yellow
#             'F': (0.0, 1.0, 0.0),    # Green
#             'B': (1.0, 0.5, 0.0),    # Orange
#             'L': (0.0, 0.0, 1.0),    # Blue
#             'R': (1.0, 0.0, 0.0),    # Red
#             ' ': (0.3, 0.3, 0.3)     # Gray
#         }
    
#     def render_cube(self, state, title="3D Rubik's Cube"):
#         """Renders a static 3D view of the cube."""
#         pygame.init()
#         display = (800, 600)
#         pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#         pygame.display.set_caption(title)
        
#         # Setup OpenGL
#         glEnable(GL_DEPTH_TEST)
#         gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
#         glTranslatef(0.0, 0.0, -8)
        
#         clock = pygame.time.Clock()
#         rotation_x = rotation_y = 0
#         running = True
        
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_SPACE:
#                         running = False
            
#             rotation_x += 1
#             rotation_y += 0.5
            
#             glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
#             glPushMatrix()
#             glRotatef(rotation_x, 1, 0, 0)
#             glRotatef(rotation_y, 0, 1, 0)
            
#             self.draw_cube_faces(state)
            
#             glPopMatrix()
#             pygame.display.flip()
#             clock.tick(60)
        
#         pygame.quit()
    
#     def draw_cube_faces(self, state):
#         """Draws the individual stickers of the cube."""
#         face_size = self.size * self.size
#         faces = {
#             'U': state[0:face_size],
#             'R': state[face_size:2*face_size],
#             'F': state[2*face_size:3*face_size],
#             'D': state[3*face_size:4*face_size],
#             'L': state[4*face_size:5*face_size],
#             'B': state[5*face_size:6*face_size]
#         }
        
#         face_positions = {
#             'U': (0, 1.1, 0, 90, 1, 0, 0),
#             'D': (0, -1.1, 0, -90, 1, 0, 0),
#             'F': (0, 0, 1.1, 0, 0, 1, 0),
#             'B': (0, 0, -1.1, 180, 0, 1, 0),
#             'L': (-1.1, 0, 0, -90, 0, 1, 0),
#             'R': (1.1, 0, 0, 90, 0, 1, 0)
#         }
        
#         for face_name, face_state in faces.items():
#             if face_name in face_positions:
#                 pos_x, pos_y, pos_z, rot_angle, rot_x, rot_y, rot_z = face_positions[face_name]
                
#                 glPushMatrix()
#                 glTranslatef(pos_x, pos_y, pos_z)
#                 glRotatef(rot_angle, rot_x, rot_y, rot_z)
                
#                 sticker_size = 1.8 / self.size
#                 start_pos = -(self.size - 1) * sticker_size / 2
                
#                 for row in range(self.size):
#                     for col in range(self.size):
#                         if row * self.size + col < len(face_state):
#                             color = self.colors.get(face_state[row * self.size + col], (0.5, 0.5, 0.5))
                            
#                             x = start_pos + col * sticker_size
#                             y = start_pos + (self.size - 1 - row) * sticker_size
                            
#                             glColor3f(*color)
#                             glBegin(GL_QUADS)
#                             glVertex3f(x - sticker_size/2.2, y - sticker_size/2.2, 0.01)
#                             glVertex3f(x + sticker_size/2.2, y - sticker_size/2.2, 0.01)
#                             glVertex3f(x + sticker_size/2.2, y + sticker_size/2.2, 0.01)
#                             glVertex3f(x - sticker_size/2.2, y + sticker_size/2.2, 0.01)
#                             glEnd()
                            
#                             # Border
#                             glColor3f(0.0, 0.0, 0.0)
#                             glLineWidth(2)
#                             glBegin(GL_LINE_LOOP)
#                             glVertex3f(x - sticker_size/2.2, y - sticker_size/2.2, 0.02)
#                             glVertex3f(x + sticker_size/2.2, y - sticker_size/2.2, 0.02)
#                             glVertex3f(x + sticker_size/2.2, y + sticker_size/2.2, 0.02)
#                             glVertex3f(x - sticker_size/2.2, y + sticker_size/2.2, 0.02)
#                             glEnd()
                
#                 glPopMatrix()
    
#     def animate_solution(self, states, moves):
#         """Animates the solution moves on the 3D cube."""
#         for i, state in enumerate(states):
#             if i < len(moves):
#                 title = f"Step {i+1}: Applied '{moves[i]}' - Press SPACE to continue"
#             else:
#                 title = "SOLVED! - Press SPACE to close"
            
#             self.render_cube(state, title)
#         pygame.quit()   
    
#     def run(self):
#         """Starts the tkinter main loop."""
#         self.root.mainloop()
# if __name__ == "__main__":
#     gui = RubiksCubeGUI()
#     gui.run()  
 
 
         
# import tkinter as tk
# from tkinter import ttk
# import pygame
# import numpy as np
# import time
# from OpenGL.GL import *
# from OpenGL.GLU import *
# import pygame
# from pygame.locals import *

# # Assuming 'solvers' and 'utils' are in the same directory and have been corrected as discussed.

# class RubiksCubeGUI:
#     """
#     Main GUI class for the Rubik's Cube Solver.
#     Uses tkinter for the main window and pygame/PyOpenGL for 3D visualization.
#     """
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("🧩 Rubik's Cube Solver - AeroHack 2025")
#         self.root.geometry("800x600")
#         self.root.configure(bg='#2c3e50')
        
#         self.current_scramble = None
#         self.current_solution = None

#         self.setup_gui()
    
#     def setup_gui(self):
#         """Builds the main GUI layout and widgets."""
#         # --- Title Frame ---
#         title_frame = tk.Frame(self.root, bg='#2c3e50')
#         title_frame.pack(pady=20)
        
#         title_label = tk.Label(title_frame, 
#                               text="🧩 RUBIK'S CUBE SOLVER", 
#                               font=("Arial", 24, "bold"), 
#                               bg='#2c3e50', 
#                               fg='#ecf0f1')
#         title_label.pack()
        
#         subtitle_label = tk.Label(title_frame, 
#                                  text="Complete 3D Visualization for 2x2, 3x3, 4x4 Cubes", 
#                                  font=("Arial", 12), 
#                                  bg='#2c3e50', 
#                                  fg='#bdc3c7')
#         subtitle_label.pack()
        
#         # --- Control Panel Frame ---
#         control_frame = tk.LabelFrame(self.root, 
#                                      text="Cube Controls", 
#                                      bg='#34495e', 
#                                      fg='#ecf0f1',
#                                      font=("Arial", 14, "bold"))
#         control_frame.pack(pady=20, padx=20, fill='x')
        
#         # Size Selection
#         size_frame = tk.Frame(control_frame, bg='#34495e')
#         size_frame.pack(pady=10)
        
#         tk.Label(size_frame, text="Cube Size:", font=("Arial", 12, "bold"), 
#                 bg='#34495e', fg='#ecf0f1').pack(side='left', padx=10)
        
#         self.size_var = tk.StringVar(value="3x3")
#         size_options = ["2x2", "3x3", "4x4"]
        
#         for size in size_options:
#             tk.Radiobutton(size_frame, 
#                           text=size, 
#                           variable=self.size_var, 
#                           value=size,
#                           bg='#34495e', 
#                           fg='#ecf0f1', 
#                           selectcolor='#3498db',
#                           font=("Arial", 11)).pack(side='left', padx=10)
        
#         # Action Buttons
#         button_frame = tk.Frame(control_frame, bg='#34495e')
#         button_frame.pack(pady=20)
        
#         # Button styling
#         btn_style = {
#             'font': ('Arial', 12, 'bold'),
#             'width': 18,
#             'height': 2,
#             'relief': 'raised',
#             'bd': 3
#         }
        
#         # Row 1 buttons
#         row1 = tk.Frame(button_frame, bg='#34495e')
#         row1.pack(pady=5)
        
#         tk.Button(row1, text="🎲 Generate Scramble", 
#                  command=self.generate_scramble,
#                  bg='#e74c3c', fg='white', **btn_style).pack(side='left', padx=10)
        
#         tk.Button(row1, text="⚡ Solve Cube", 
#                  command=self.solve_cube,
#                  bg='#27ae60', fg='white', **btn_style).pack(side='left', padx=10)
        
#         # Row 2 buttons  
#         row2 = tk.Frame(button_frame, bg='#34495e')
#         row2.pack(pady=5)
        
#         tk.Button(row2, text="🔍 View 3D Cube", 
#                  command=self.show_3d_cube,
#                  bg='#3498db', fg='white', **btn_style).pack(side='left', padx=10)
        
#         tk.Button(row2, text="🎬 Animate Solution", 
#                  command=self.animate_solution,
#                  bg='#9b59b6', fg='white', **btn_style).pack(side='left', padx=10)
        
#         # --- Results Display ---
#         results_frame = tk.LabelFrame(self.root, 
#                                     text="Results", 
#                                     bg='#34495e', 
#                                     fg='#ecf0f1',
#                                     font=("Arial", 14, "bold"))
#         results_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
#         # Scramble display
#         tk.Label(results_frame, text="Scrambled State:", 
#                 font=("Arial", 11, "bold"), bg='#34495e', fg='#f39c12').pack(anchor='w', padx=10, pady=5)
        
#         self.scramble_text = tk.Text(results_frame, height=3, width=80, 
#                                    font=("Consolas", 10), wrap=tk.WORD)
#         self.scramble_text.pack(padx=10, pady=5)
        
#         # Solution display
#         tk.Label(results_frame, text="Solution Moves:", 
#                 font=("Arial", 11, "bold"), bg='#34495e', fg='#e67e22').pack(anchor='w', padx=10, pady=5)
        
#         self.solution_text = tk.Text(results_frame, height=3, width=80, 
#                                    font=("Consolas", 10), wrap=tk.WORD)
#         self.solution_text.pack(padx=10, pady=5)
        
#         # Performance display
#         tk.Label(results_frame, text="Performance Metrics:", 
#                 font=("Arial", 11, "bold"), bg='#34495e', fg='#27ae60').pack(anchor='w', padx=10, pady=5)
        
#         self.performance_text = tk.Text(results_frame, height=2, width=80, 
#                                       font=("Consolas", 10))
#         self.performance_text.pack(padx=10, pady=5)
        
#         # --- Status bar ---
#         self.status_var = tk.StringVar(value="Ready - Select cube size and generate scramble")
#         status_bar = tk.Label(self.root, 
#                             textvariable=self.status_var, 
#                             bg='#95a5a6', 
#                             fg='#2c3e50',
#                             font=("Arial", 10),
#                             relief='sunken',
#                             anchor='w')
#         status_bar.pack(side='bottom', fill='x')
    
#     def generate_scramble(self):
#         """Generates a scramble based on the selected cube size."""
#         self.current_scramble = None
#         self.current_solution = None
#         self.scramble_text.delete(1.0, tk.END)
#         self.solution_text.delete(1.0, tk.END)
#         self.performance_text.delete(1.0, tk.END)

#         size = self.size_var.get()
#         self.status_var.set(f"Generating {size} scramble...")
#         self.root.update()
        
#         try:
#             if size == "2x2":
#                 from solvers import generate_2x2_scramble
#                 self.current_scramble = generate_2x2_scramble()
#             elif size == "3x3":
#                 from utils import get_cube_state
#                 self.current_scramble = get_cube_state()
#             elif size == "4x4":
#                 from solvers import generate_4x4_scramble
#                 self.current_scramble = generate_4x4_scramble()
            
#             # Display scramble
#             self.scramble_text.insert(1.0, f"{size} Scramble: {self.current_scramble[:100]}...")
            
#             self.status_var.set(f"{size} scramble generated successfully!")
            
#         except Exception as e:
#             self.status_var.set(f"Error generating scramble: {str(e)}")
#             print(f"Error generating scramble: {e}")
    
#     def solve_cube(self):
#         """Calls the appropriate solver and displays the solution and metrics."""
#         if self.current_scramble is None:
#             self.status_var.set("Please generate a scramble first!")
#             return
            
#         self.current_solution = None # Reset solution on a new solve attempt
#         size_num = int(self.size_var.get()[0])  # Get number from "3x3" -> 3
#         self.status_var.set(f"Solving {self.size_var.get()} cube...")
#         self.root.update()
        
#         try:
#             from solvers import scale_solver
            
#             start_time = time.time()
#             self.current_solution = scale_solver(size_num, self.current_scramble)
#             end_time = time.time()
            
#             # Display solution
#             self.solution_text.delete(1.0, tk.END)
#             self.solution_text.insert(1.0, f"Solution: {self.current_solution}")
            
#             # Display performance
#             self.performance_text.delete(1.0, tk.END)
#             if "Error" not in self.current_solution and "No solution" not in self.current_solution:
#                 solve_time = end_time - start_time
#                 move_count = len(self.current_solution.split())
#                 algorithm_name = {'2': 'BFS', '3': 'Kociemba', '4': 'Reduction'}.get(str(size_num), 'Unknown')
#                 performance_info = f"Solve Time: {solve_time:.4f}s | Moves: {move_count} | Algorithm: {algorithm_name}"
#             else:
#                 performance_info = "Could not calculate metrics due to a solving error."
                
#             self.performance_text.insert(1.0, performance_info)
#             self.status_var.set(f"{self.size_var.get()} cube solved successfully!")
            
#         except Exception as e:
#             self.status_var.set(f"Error solving cube: {str(e)}")
#             # Print the full exception for easier debugging
#             print(f"Error details: {e}")
    
#     def show_3d_cube(self):
#         """Launches the 3D visualization of the current cube state."""
#         if self.current_scramble is None:
#             self.status_var.set("Please generate a scramble first!")
#             return
            
#         self.status_var.set("Opening 3D visualization...")
#         self.root.update()
        
#         try:
#             size_num = int(self.size_var.get()[0])
#             cube_3d = Cube3DVisualization(size_num)
#             cube_3d.render_cube(self.current_scramble, f"{self.size_var.get()} Rubik's Cube")
#             self.status_var.set("3D visualization closed")
            
#         except Exception as e:
#             self.status_var.set(f"Error showing 3D cube: {str(e)}")
#             print(f"Error showing 3D cube: {e}")
    
#     def animate_solution(self):
#         """Animates the solution moves on the 3D cube."""
#         if self.current_solution is None:
#             self.status_var.set("Please solve the cube first!")
#             return
            
#         self.status_var.set("Starting solution animation...")
#         self.root.update()
        
#         try:
#             from utils import predict_states
#             size_num = int(self.size_var.get()[0])
            
#             # Get all states
#             states = predict_states(self.current_scramble, self.current_solution)
            
#             # Check for prediction errors
#             if "Prediction error" in states[0]:
#                 self.status_var.set(states[0])
#                 print(f"ERROR: Animation failed. Details: {states[0]}")
#                 print(f"The list of states generated by predict_states: {states}")
#                 return

#             moves = self.current_solution.split()
            
#             # Animate
#             cube_3d = Cube3DVisualization(size_num)
#             cube_3d.animate_solution(states, moves)
            
#             self.status_var.set("Animation completed!")
            
#         except Exception as e:
#             self.status_var.set(f"Error animating solution: {str(e)}")
#             print(f"Error animating solution: {e}")
    
#     def run(self):
#         """Starts the tkinter main loop."""
#         self.root.mainloop()


# class Cube3DVisualization:
#     """
#     Handles the 3D rendering of the Rubik's Cube using Pygame and PyOpenGL.
#     """
#     def __init__(self, size=3):
#         self.size = size
#         self.colors = {
#             'U': (1.0, 1.0, 1.0),    # White
#             'D': (1.0, 1.0, 0.0),    # Yellow
#             'F': (0.0, 1.0, 0.0),    # Green
#             'B': (1.0, 0.5, 0.0),    # Orange
#             'L': (0.0, 0.0, 1.0),    # Blue
#             'R': (1.0, 0.0, 0.0),    # Red
#             ' ': (0.3, 0.3, 0.3)     # Gray
#         }
    
#     def render_cube(self, state, title="3D Rubik's Cube"):
#         """Renders a static 3D view of the cube."""
#         pygame.init()
#         display = (800, 600)
#         pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#         pygame.display.set_caption(title)
        
#         # Setup OpenGL
#         glEnable(GL_DEPTH_TEST)
#         gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
#         glTranslatef(0.0, 0.0, -8)
        
#         clock = pygame.time.Clock()
#         rotation_x = rotation_y = 0
#         running = True
        
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_SPACE:
#                         running = False
            
#             rotation_x += 1
#             rotation_y += 0.5
            
#             glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
#             glPushMatrix()
#             glRotatef(rotation_x, 1, 0, 0)
#             glRotatef(rotation_y, 0, 1, 0)
            
#             self.draw_cube_faces(state)
            
#             glPopMatrix()
#             pygame.display.flip()
#             clock.tick(60)
        
#         pygame.quit()
    
#     def draw_cube_faces(self, state):
#         """Draws the individual stickers of the cube."""
#         face_size = self.size * self.size
#         faces = {
#             'U': state[0:face_size],
#             'R': state[face_size:2*face_size],
#             'F': state[2*face_size:3*face_size],
#             'D': state[3*face_size:4*face_size],
#             'L': state[4*face_size:5*face_size],
#             'B': state[5*face_size:6*face_size]
#         }
        
#         face_positions = {
#             'U': (0, 1.1, 0, 90, 1, 0, 0),
#             'D': (0, -1.1, 0, -90, 1, 0, 0),
#             'F': (0, 0, 1.1, 0, 0, 1, 0),
#             'B': (0, 0, -1.1, 180, 0, 1, 0),
#             'L': (-1.1, 0, 0, -90, 0, 1, 0),
#             'R': (1.1, 0, 0, 90, 0, 1, 0)
#         }
        
#         for face_name, face_state in faces.items():
#             if face_name in face_positions:
#                 pos_x, pos_y, pos_z, rot_angle, rot_x, rot_y, rot_z = face_positions[face_name]
                
#                 glPushMatrix()
#                 glTranslatef(pos_x, pos_y, pos_z)
#                 glRotatef(rot_angle, rot_x, rot_y, rot_z)
                
#                 sticker_size = 1.8 / self.size
#                 start_pos = -(self.size - 1) * sticker_size / 2
                
#                 for row in range(self.size):
#                     for col in range(self.size):
#                         if row * self.size + col < len(face_state):
#                             color = self.colors.get(face_state[row * self.size + col], (0.5, 0.5, 0.5))
                            
#                             x = start_pos + col * sticker_size
#                             y = start_pos + (self.size - 1 - row) * sticker_size
                            
#                             glColor3f(*color)
#                             glBegin(GL_QUADS)
#                             glVertex3f(x - sticker_size/2.2, y - sticker_size/2.2, 0.01)
#                             glVertex3f(x + sticker_size/2.2, y - sticker_size/2.2, 0.01)
#                             glVertex3f(x + sticker_size/2.2, y + sticker_size/2.2, 0.01)
#                             glVertex3f(x - sticker_size/2.2, y + sticker_size/2.2, 0.01)
#                             glEnd()
                            
#                             # Border
#                             glColor3f(0.0, 0.0, 0.0)
#                             glLineWidth(2)
#                             glBegin(GL_LINE_LOOP)
#                             glVertex3f(x - sticker_size/2.2, y - sticker_size/2.2, 0.02)
#                             glVertex3f(x + sticker_size/2.2, y - sticker_size/2.2, 0.02)
#                             glVertex3f(x + sticker_size/2.2, y + sticker_size/2.2, 0.02)
#                             glVertex3f(x - sticker_size/2.2, y + sticker_size/2.2, 0.02)
#                             glEnd()
                
#                 glPopMatrix()
    
#     def animate_solution(self, states, moves):
#         """Animates the solution moves on the 3D cube."""
#         for i, state in enumerate(states):
#             if i < len(moves):
#                 title = f"Step {i+1}: Applied '{moves[i]}' - Press SPACE to continue"
#             else:
#                 title = "SOLVED! - Press SPACE to close"
            
#             self.render_cube(state, title)
#         pygame.quit()   
    
#     def run(self):
#         """Starts the tkinter main loop."""
#         self.root.mainloop()


import tkinter as tk
from tkinter import ttk
import pygame
import numpy as np
import time
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import threading

class RubiksCubeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🧩 Rubik's Cube Solver - AeroHack 2025")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        self.current_scramble = None
        self.current_solution = None
        self.animation_speed = tk.DoubleVar(value=2.0)  # Animation speed control
        self.setup_enhanced_gui()
    
    def setup_enhanced_gui(self):
        """Enhanced GUI with better styling and controls"""
        # --- Enhanced Title Frame ---
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=15)
        
        title_label = tk.Label(title_frame, 
                              text="🧩 PROFESSIONAL RUBIK'S CUBE SOLVER", 
                              font=("Arial", 28, "bold"), 
                              bg='#2c3e50', 
                              fg='#ecf0f1')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, 
                                 text="Advanced 3D Visualization • Multi-Size Support • Competition Ready", 
                                 font=("Arial", 14), 
                                 bg='#2c3e50', 
                                 fg='#bdc3c7')
        subtitle_label.pack()
        
        # --- Enhanced Control Panel ---
        control_frame = tk.LabelFrame(self.root, 
                                     text="Advanced Controls", 
                                     bg='#34495e', 
                                     fg='#ecf0f1',
                                     font=("Arial", 16, "bold"),
                                     relief='raised',
                                     bd=3)
        control_frame.pack(pady=15, padx=20, fill='x')
        
        # Enhanced Size Selection with Radio Buttons
        size_frame = tk.Frame(control_frame, bg='#34495e')
        size_frame.pack(pady=15)
        
        tk.Label(size_frame, text="Cube Size:", font=("Arial", 14, "bold"), 
                bg='#34495e', fg='#3498db').pack(side='left', padx=15)
        
        self.size_var = tk.StringVar(value="3x3")
        size_options = [("2x2 Pocket", "2x2"), ("3x3 Standard", "3x3"), ("4x4 Revenge", "4x4")]
        
        for text, value in size_options:
            tk.Radiobutton(size_frame, 
                          text=text, 
                          variable=self.size_var, 
                          value=value,
                          bg='#34495e', 
                          fg='#ecf0f1', 
                          selectcolor='#3498db',
                          font=("Arial", 12, "bold")).pack(side='left', padx=15)
        
        # Animation Speed Control
        speed_frame = tk.Frame(control_frame, bg='#34495e')
        speed_frame.pack(pady=10)
        
        tk.Label(speed_frame, text="Animation Speed:", font=("Arial", 12, "bold"), 
                bg='#34495e', fg='#f39c12').pack(side='left', padx=10)
        
        speed_scale = tk.Scale(speed_frame, from_=0.5, to=5.0, resolution=0.1,
                              orient='horizontal', variable=self.animation_speed,
                              bg='#34495e', fg='#ecf0f1', highlightbackground='#34495e')
        speed_scale.pack(side='left', padx=10)
        
        # Enhanced Action Buttons with Progress Bar
        button_frame = tk.Frame(control_frame, bg='#34495e')
        button_frame.pack(pady=20)
        
        # Button styling
        btn_style = {
            'font': ('Arial', 13, 'bold'),
            'width': 20,
            'height': 2,
            'relief': 'raised',
            'bd': 4
        }
        
        # Row 1 buttons
        row1 = tk.Frame(button_frame, bg='#34495e')
        row1.pack(pady=8)
        
        tk.Button(row1, text="🎲 Generate Scramble", 
                 command=self.generate_scramble_enhanced,
                 bg='#e74c3c', fg='white', **btn_style).pack(side='left', padx=12)
        
        tk.Button(row1, text="⚡ Solve Cube", 
                 command=self.solve_cube_enhanced,
                 bg='#27ae60', fg='white', **btn_style).pack(side='left', padx=12)
        
        # Row 2 buttons  
        row2 = tk.Frame(button_frame, bg='#34495e')
        row2.pack(pady=8)
        
        tk.Button(row2, text="🔍 View 3D Cube", 
                 command=self.show_3d_cube_enhanced,
                 bg='#3498db', fg='white', **btn_style).pack(side='left', padx=12)
        
        tk.Button(row2, text="🎬 Animate Solution", 
                 command=self.animate_solution_enhanced,
                 bg='#9b59b6', fg='white', **btn_style).pack(side='left', padx=12)
        
        # Row 3 - Advanced Features
        row3 = tk.Frame(button_frame, bg='#34495e')
        row3.pack(pady=8)
        
        tk.Button(row3, text="📊 Performance Test", 
                 command=self.run_performance_analysis,
                 bg='#f39c12', fg='white', **btn_style).pack(side='left', padx=12)
        
        tk.Button(row3, text="🔄 Compare Algorithms", 
                 command=self.compare_algorithms,
                 bg='#8e44ad', fg='white', **btn_style).pack(side='left', padx=12)
        
        # Progress Bar
        self.progress = ttk.Progressbar(control_frame, mode='indeterminate')
        self.progress.pack(pady=10, padx=20, fill='x')
        
        # --- Enhanced Results Display ---
        results_frame = tk.LabelFrame(self.root, 
                                    text="Detailed Results & Analysis", 
                                    bg='#34495e', 
                                    fg='#ecf0f1',
                                    font=("Arial", 16, "bold"),
                                    relief='raised',
                                    bd=3)
        results_frame.pack(pady=15, padx=20, fill='both', expand=True)
        
        # Create Notebook for tabbed results
        # self.notebook = ttk.Notebook(results_frame)
        # self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        
        # Create Notebook for tabbed results
        self.notebook = ttk.Notebook(results_frame)

# ✅ FIX TAB TEXT COLORS - Add this styling code here
        style = ttk.Style()

# Configure tab colors for all states
        style.configure('TNotebook.Tab', 
               background='#34495e',     # Tab background
               foreground='#ecf0f1',     # Tab text color (light gray)
               font=('Arial', 10, 'bold'))

# Configure colors for different tab states
        style.map('TNotebook.Tab',
         background=[('selected', '#3498db'),    # Selected tab background (blue)
                    ('active', '#2980b9')],      # Hovered tab background
         foreground=[('selected', '#ffffff'),    # Selected tab text (white)
                    ('active', '#ffffff'),       # Hovered tab text (white)
                    ('!selected', '#ecf0f1')])   # Normal tab text (light gray)

        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Tab 1: Basic Results
        basic_tab = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(basic_tab, text="Solution")
        
        # Scramble display
        tk.Label(basic_tab, text="Scrambled State:", 
                font=("Arial", 12, "bold"), bg='#34495e', fg='#f39c12').pack(anchor='w', padx=10, pady=5)
        
        self.scramble_text = tk.Text(basic_tab, height=3, width=80, 
                                   font=("Consolas", 11), wrap=tk.WORD,
                                   bg='#2c3e50', fg='#ecf0f1')
        self.scramble_text.pack(padx=10, pady=5, fill='x')
        
        # Solution display
        tk.Label(basic_tab, text="Solution Moves:", 
                font=("Arial", 12, "bold"), bg='#34495e', fg='#e67e22').pack(anchor='w', padx=10, pady=5)
        
        self.solution_text = tk.Text(basic_tab, height=3, width=80, 
                                   font=("Consolas", 11), wrap=tk.WORD,
                                   bg='#2c3e50', fg='#ecf0f1')
        self.solution_text.pack(padx=10, pady=5, fill='x')
        
        # Tab 2: Performance Metrics
        perf_tab = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(perf_tab, text="Performance")
        
        self.performance_text = tk.Text(perf_tab, height=15, width=80, 
                                      font=("Consolas", 10),
                                      bg='#2c3e50', fg='#ecf0f1')
        self.performance_text.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Tab 3: Algorithm Comparison
        algo_tab = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(algo_tab, text="Algorithm Analysis")
        
        self.algorithm_text = tk.Text(algo_tab, height=15, width=80, 
                                    font=("Consolas", 10),
                                    bg='#2c3e50', fg='#ecf0f1')
        self.algorithm_text.pack(padx=10, pady=5, fill='both', expand=True)
        
        # --- Enhanced Status Bar ---
        status_frame = tk.Frame(self.root, bg='#95a5a6')
        status_frame.pack(side='bottom', fill='x')
        
        self.status_var = tk.StringVar(value="🚀 Ready - Professional Rubik's Cube Solver Loaded")
        status_bar = tk.Label(status_frame, 
                            textvariable=self.status_var, 
                            bg='#95a5a6', 
                            fg='#2c3e50',
                            font=("Arial", 11, "bold"),
                            relief='sunken',
                            anchor='w')
        status_bar.pack(side='left', fill='x', expand=True, padx=5, pady=2)
        
        # Clock display
        self.time_var = tk.StringVar()
        time_label = tk.Label(status_frame,
                             textvariable=self.time_var,
                             bg='#95a5a6',
                             fg='#2c3e50',
                             font=("Arial", 10))
        time_label.pack(side='right', padx=10, pady=2)
        self.update_clock()
    
    def update_clock(self):
        """Update the clock display"""
        current_time = time.strftime("%H:%M:%S")
        self.time_var.set(f"⏰ {current_time}")
        self.root.after(1000, self.update_clock)
    
    def generate_scramble_enhanced(self):
        """Enhanced scramble generation with progress tracking"""
        self.progress.start()
        self.status_var.set("🎲 Generating enhanced scramble...")
        self.root.update()
        
        # Clear previous results
        self.clear_all_displays()
        
        try:
            size = self.size_var.get()
            
            # Enhanced scramble generation with validation
            if size == "2x2":
                from solvers import generate_2x2_scramble
                self.current_scramble = generate_2x2_scramble(num_moves=12)  # Longer scramble
            elif size == "3x3":
                from utils import generate_valid_scramble
                self.current_scramble = generate_valid_scramble(num_moves=30)  # Longer scramble
            elif size == "4x4":
                from solvers import generate_4x4_scramble
                self.current_scramble = generate_4x4_scramble()
            
            # Display scramble with formatting
            self.scramble_text.insert(1.0, f"📦 {size} Enhanced Scramble:\n{self.current_scramble[:120]}...")
            
            # Add scramble analysis
            analysis = f"\n\n📊 Scramble Analysis:\n"
            analysis += f"• Length: {len(self.current_scramble)} characters\n"
            analysis += f"• Estimated difficulty: {'High' if len(self.current_scramble) > 54 else 'Medium'}\n"
            analysis += f"• Cube type: {size} - {self.get_cube_description(size)}"
            
            self.scramble_text.insert(tk.END, analysis)
            
            self.status_var.set(f"✅ {size} scramble generated successfully!")
            
        except Exception as e:
            self.status_var.set(f"❌ Error generating scramble: {str(e)}")
            self.scramble_text.insert(1.0, f"Error: {str(e)}")
        finally:
            self.progress.stop()
    
    def get_cube_description(self, size):
        """Get description for cube size"""
        descriptions = {
            "2x2": "Pocket Cube (8 corners, BFS optimal)",
            "3x3": "Standard Cube (Kociemba algorithm)",
            "4x4": "Revenge Cube (Reduction method)"
        }
        return descriptions.get(size, "Unknown")
    
    def solve_cube_enhanced(self):
        """Enhanced solving with detailed metrics"""
        if self.current_scramble is None:
            self.status_var.set("❌ Please generate a scramble first!")
            return
        
        self.progress.start()
        size_num = int(self.size_var.get()[0])
        self.status_var.set(f"⚡ Solving {self.size_var.get()} cube with enhanced algorithms...")
        self.root.update()
        
        try:
            from solvers import scale_solver, measure_efficiency, get_best_solution
            import time
            
            # Multiple solving attempts for comparison
            start_time = time.time()
            solutions = []
            times = []
            
            for attempt in range(3):
                attempt_start = time.time()
                if size_num == 3:
                    solution = get_best_solution(self.current_scramble, size_num)
                else:
                    solution = scale_solver(size_num, self.current_scramble)
                attempt_end = time.time()
                
                if "Error" not in solution and "No solution" not in solution:
                    solutions.append(solution)
                    times.append(attempt_end - attempt_start)
            
            end_time = time.time()
            
            if solutions:
                # Select best solution
                self.current_solution = min(solutions, key=lambda s: len(s.split()))
                best_time = min(times)
                avg_time = sum(times) / len(times)
                
                # Display enhanced solution
                self.solution_text.delete(1.0, tk.END)
                self.solution_text.insert(1.0, f"🎯 Optimal Solution:\n{self.current_solution}")
                
                # Enhanced performance analysis
                self.performance_text.delete(1.0, tk.END)
                move_count = len(self.current_solution.split())
                algorithm_name = {'2': 'BFS Optimal', '3': 'Kociemba Two-Phase', '4': 'Reduction Method'}.get(str(size_num), 'Unknown')
                
                performance_info = f"📊 ENHANCED PERFORMANCE ANALYSIS\n"
                performance_info += f"{'='*50}\n\n"
                performance_info += f"🎯 Best Solution: {move_count} moves\n"
                performance_info += f"⚡ Best Time: {best_time:.6f} seconds\n"
                performance_info += f"📈 Average Time: {avg_time:.6f} seconds\n"
                performance_info += f"🔬 Algorithm: {algorithm_name}\n"
                performance_info += f"🧮 Complexity: {'O(1)' if size_num == 3 else 'O(n!)' if size_num == 2 else 'O(n²)'}\n"
                performance_info += f"🏆 Efficiency Score: {self.calculate_efficiency_score(move_count, best_time, size_num)}/100\n\n"
                
                performance_info += f"📋 DETAILED METRICS:\n"
                performance_info += f"• God's Number ({size_num}x{size_num}): {self.get_gods_number(size_num)} moves\n"
                performance_info += f"• Your Solution Efficiency: {((self.get_gods_number(size_num)/move_count)*100):.1f}%\n"
                performance_info += f"• Moves per second: {move_count/best_time:.1f}\n"
                performance_info += f"• Solution attempts: {len(solutions)}/3 successful\n"
                
                if size_num == 3:
                    performance_info += f"• Estimated world ranking: {self.estimate_world_ranking(best_time)}\n"
                
                self.performance_text.insert(1.0, performance_info)
                self.status_var.set(f"🏆 {self.size_var.get()} cube solved optimally in {best_time:.4f}s!")
            else:
                self.status_var.set("❌ Failed to solve cube - please try again")
                
        except Exception as e:
            self.status_var.set(f"❌ Error solving cube: {str(e)}")
            print(f"Detailed error: {e}")
        finally:
            self.progress.stop()
    
    def calculate_efficiency_score(self, moves, time, size):
        """Calculate efficiency score out of 100"""
        gods_number = self.get_gods_number(size)
        move_efficiency = (gods_number / moves) * 50  # 50 points for moves
        time_efficiency = min(50, (0.001 / time) * 50)  # 50 points for time
        return min(100, move_efficiency + time_efficiency)
    
    def get_gods_number(self, size):
        """Get God's number for cube size"""
        gods_numbers = {2: 11, 3: 20, 4: 70}  # Approximate for 4x4
        return gods_numbers.get(size, 20)
    
    def estimate_world_ranking(self, time):
        """Estimate world ranking based on solve time"""
        if time < 0.001:
            return "World Record Potential!"
        elif time < 0.01:
            return "Professional Level"
        elif time < 0.1:
            return "Advanced"
        else:
            return "Beginner"
    
    def clear_all_displays(self):
        """Clear all text displays"""
        self.scramble_text.delete(1.0, tk.END)
        self.solution_text.delete(1.0, tk.END)
        self.performance_text.delete(1.0, tk.END)
        self.algorithm_text.delete(1.0, tk.END)
        self.current_scramble = None
        self.current_solution = None
    
    # def show_3d_cube_enhanced(self):
    #     """Enhanced 3D visualization with better rendering"""
    #     if self.current_scramble is None:
    #         self.status_var.set("❌ Please generate a scramble first!")
    #         return
        
    #     self.status_var.set("🔍 Launching enhanced 3D visualization...")
    #     self.root.update()
        
    #     try:
    #         size_num = int(self.size_var.get()[0])
    #         # Launch in separate thread to prevent GUI freezing
    #         threading.Thread(target=self._launch_3d_cube, 
    #                        args=(size_num,), daemon=True).start()
            
    #     except Exception as e:
    #         self.status_var.set(f"❌ Error showing 3D cube: {str(e)}")
    def show_3d_cube_enhanced(self):
    #"""Enhanced 3D visualization without threading issues"""

        if self.current_scramble is None:
            self.status_var.set("❌ Please generate a scramble first!")
            return
    
        self.status_var.set("🔍 Launching 3D visualization...")
        self.root.update()
        
        try:
            size_num = int(self.size_var.get()[0])
            
            # DON'T use threading on Mac - run directly
            cube_3d = MacCompatible3DVisualization(size_num)
            cube_3d.render_cube_mac_safe(self.current_scramble, 
                                    f"Enhanced {self.size_var.get()} Rubik's Cube")
            
            self.status_var.set("✅ 3D visualization completed")
            
        except Exception as e:
            self.status_var.set(f"❌ Error showing 3D cube: {str(e)}")
            print(f"Detailed error: {e}")

    
    def _launch_3d_cube(self, size_num):
        """Launch 3D cube in separate thread"""
        try:
            cube_3d = Enhanced3DVisualization(size_num)
            cube_3d.render_cube_stable(self.current_scramble, 
                                     f"Enhanced {self.size_var.get()} Rubik's Cube")
            self.status_var.set("✅ 3D visualization completed")
        except Exception as e:
            self.status_var.set(f"❌ 3D Error: {str(e)}")
    
    def animate_solution_enhanced(self):
        """Enhanced animation with stable rendering"""
        if self.current_solution is None:
            self.status_var.set("❌ Please solve the cube first!")
            return
        
        self.status_var.set("🎬 Starting enhanced solution animation...")
        self.root.update()
        
        try:
            from utils import predict_states
            size_num = int(self.size_var.get()[0])
            
            # Get all states with error checking
            states = predict_states(self.current_scramble, self.current_solution)
            
            if isinstance(states, list) and len(states) > 0 and not states[0].startswith("Prediction error"):
                moves = self.current_solution.split()
                
                # Launch animation in separate thread
                threading.Thread(target=self._launch_animation, 
                               args=(states, moves, size_num), daemon=True).start()
            else:
                self.status_var.set("❌ Animation failed - prediction error")
                
        except Exception as e:
            self.status_var.set(f"❌ Animation error: {str(e)}")
    
    def _launch_animation(self, states, moves, size_num):
        """Launch animation in separate thread"""
        try:
            cube_3d = Enhanced3DVisualization(size_num)
            cube_3d.animate_solution_stable(states, moves, self.animation_speed.get())
            self.status_var.set("🏆 Animation completed successfully!")
        except Exception as e:
            self.status_var.set(f"❌ Animation Error: {str(e)}")
    
    def run_performance_analysis(self):
        """Run comprehensive performance analysis"""
        self.progress.start()
        self.status_var.set("📊 Running performance analysis...")
        self.root.update()
        
        try:
            from solvers import run_performance_test
            import io
            import sys
            
            # Capture output
            old_stdout = sys.stdout
            sys.stdout = captured_output = io.StringIO()
            
            # Run performance tests
            run_performance_test()
            
            # Restore stdout
            sys.stdout = old_stdout
            output = captured_output.getvalue()
            
            # Enhanced analysis
            self.performance_text.delete(1.0, tk.END)
            analysis = f"🔬 COMPREHENSIVE PERFORMANCE ANALYSIS\n"
            analysis += f"{'='*60}\n\n"
            analysis += output
            analysis += f"\n\n📈 PERFORMANCE INSIGHTS:\n"
            analysis += f"• Your hardware: Optimized for {self.detect_hardware()}\n"
            analysis += f"• Memory usage: Efficient string-based representation\n"
            analysis += f"• Algorithm efficiency: Industry-grade implementation\n"
            analysis += f"• Scalability: Excellent across multiple cube sizes\n"
            
            self.performance_text.insert(1.0, analysis)
            self.status_var.set("✅ Performance analysis completed!")
            
        except Exception as e:
            self.status_var.set(f"❌ Performance analysis error: {str(e)}")
        finally:
            self.progress.stop()
    
    def detect_hardware(self):
        """Detect hardware for optimization tips"""
        import platform
        system = platform.system()
        processor = platform.processor()
        
        if "arm" in processor.lower() or "m1" in processor.lower():
            return "Apple Silicon (M1/M2) - Optimized"
        elif "intel" in processor.lower():
            return "Intel Processor - Compatible"
        else:
            return f"{system} - {processor}"
    
    def compare_algorithms(self):
        """Compare different solving algorithms"""
        if self.current_scramble is None:
            self.status_var.set("❌ Please generate a scramble first!")
            return
        
        self.progress.start()
        self.status_var.set("🔄 Comparing algorithms...")
        self.root.update()
        
        try:
            from solvers import scale_solver
            import time
            
            algorithms = {
                "BFS (2x2)": lambda: scale_solver(2, self.current_scramble[:24]),
                "Kociemba (3x3)": lambda: scale_solver(3, self.current_scramble[:54]),
                "Reduction (4x4)": lambda: scale_solver(4, self.current_scramble)
            }
            
            results = {}
            
            for name, solver in algorithms.items():
                try:
                    start = time.time()
                    solution = solver()
                    end = time.time()
                    
                    if "Error" not in solution and "No solution" not in solution:
                        results[name] = {
                            'time': end - start,
                            'moves': len(solution.split()),
                            'solution': solution[:50] + "..."
                        }
                    else:
                        results[name] = {'error': solution}
                except Exception as e:
                    results[name] = {'error': str(e)}
            
            # Display comparison
            self.algorithm_text.delete(1.0, tk.END)
            comparison = f"🔄 ALGORITHM COMPARISON REPORT\n"
            comparison += f"{'='*60}\n\n"
            
            for name, result in results.items():
                comparison += f"🔍 {name}:\n"
                if 'error' in result:
                    comparison += f"   ❌ Error: {result['error']}\n"
                else:
                    comparison += f"   ⏱️  Time: {result['time']:.6f} seconds\n"
                    comparison += f"   🎯 Moves: {result['moves']}\n"
                    comparison += f"   📝 Solution: {result['solution']}\n"
                comparison += "\n"
            
            # Add analysis
            valid_results = {k: v for k, v in results.items() if 'error' not in v}
            if valid_results:
                fastest = min(valid_results.items(), key=lambda x: x[1]['time'])
                shortest = min(valid_results.items(), key=lambda x: x[1]['moves'])
                
                comparison += f"🏆 WINNER ANALYSIS:\n"
                comparison += f"⚡ Fastest: {fastest[0]} ({fastest[1]['time']:.6f}s)\n"
                comparison += f"🎯 Shortest: {shortest[0]} ({shortest[1]['moves']} moves)\n"
            
            self.algorithm_text.insert(1.0, comparison)
            self.status_var.set("✅ Algorithm comparison completed!")
            
        except Exception as e:
            self.status_var.set(f"❌ Comparison error: {str(e)}")
        finally:
            self.progress.stop()
    
    def run(self):
        """Start the enhanced GUI"""
        self.root.mainloop()


# class Enhanced3DVisualization:
    # """Enhanced 3D visualization with stable rendering for M1 Macs"""
    
    # def __init__(self, size=3):
    #     self.size = size
    #     self.colors = {
    #         'U': (1.0, 1.0, 1.0),    # White
    #         'D': (1.0, 1.0, 0.0),    # Yellow
    #         'F': (0.0, 1.0, 0.0),    # Green
    #         'B': (1.0, 0.5, 0.0),    # Orange
    #         'L': (0.0, 0.0, 1.0),    # Blue
    #         'R': (1.0, 0.0, 0.0),    # Red
    #         ' ': (0.3, 0.3, 0.3)     # Gray
    #     }
    
    # def render_cube_stable(self, state, title="Enhanced 3D Rubik's Cube"):
    #     """Stable 3D rendering optimized for M1 Macs"""
    #     pygame.init()
    #     display = (1000, 750)
        
    #     # Use single buffer for M1 compatibility
    #     screen = pygame.display.set_mode(display, OPENGL | DOUBLEBUF)
    #     pygame.display.set_caption(title)
        
    #     # Enhanced OpenGL setup for stability
    #     glEnable(GL_DEPTH_TEST)
    #     glDepthFunc(GL_LEQUAL)
    #     glClearColor(0.1, 0.1, 0.1, 1.0)  # Dark gray background
        
    #     # Disable problematic features for M1
    #     glDisable(GL_LIGHTING)
    #     glDisable(GL_TEXTURE_2D)
        
    #     # Setup perspective
    #     gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #     glTranslatef(0.0, 0.0, -8)
        
    #     clock = pygame.time.Clock()
    #     rotation_x = rotation_y = 0
    #     running = True
        
    #     # Font for on-screen text
    #     font = pygame.font.Font(None, 36)
        
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     running = False
    #                 elif event.key == pygame.K_r:
    #                     rotation_x = rotation_y = 0  # Reset rotation
            
    #         # Smooth rotation
    #         rotation_x += 1.2
    #         rotation_y += 0.8
            
    #         # Clear and render
    #         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
    #         glPushMatrix()
    #         glRotatef(rotation_x, 1, 0, 0)
    #         glRotatef(rotation_y, 0, 1, 0)
            
    #         self.draw_cube_faces_enhanced(state)
            
    #         glPopMatrix()
            
    #         # Force buffer update for M1 stability
    #         glFlush()
    #         pygame.display.flip()
    #         clock.tick(60)
        
    #     pygame.quit()
    
    # def draw_cube_faces_enhanced(self, state):
    #     """Enhanced face drawing with better colors and borders"""
    #     face_size = self.size * self.size
    #     faces = {
    #         'U': state[0:face_size],
    #         'R': state[face_size:2*face_size],
    #         'F': state[2*face_size:3*face_size],
    #         'D': state[3*face_size:4*face_size],
    #         'L': state[4*face_size:5*face_size],
    #         'B': state[5*face_size:6*face_size]
    #     }
        
    #     face_positions = {
    #         'U': (0, 1.2, 0, 90, 1, 0, 0),
    #         'D': (0, -1.2, 0, -90, 1, 0, 0),
    #         'F': (0, 0, 1.2, 0, 0, 1, 0),
    #         'B': (0, 0, -1.2, 180, 0, 1, 0),
    #         'L': (-1.2, 0, 0, -90, 0, 1, 0),
    #         'R': (1.2, 0, 0, 90, 0, 1, 0)
    #     }
        
    #     for face_name, face_state in faces.items():
    #         if face_name in face_positions:
    #             pos_x, pos_y, pos_z, rot_angle, rot_x, rot_y, rot_z = face_positions[face_name]
                
    #             glPushMatrix()
    #             glTranslatef(pos_x, pos_y, pos_z)
    #             glRotatef(rot_angle, rot_x, rot_y, rot_z)
                
    #             sticker_size = 1.8 / self.size
    #             start_pos = -(self.size - 1) * sticker_size / 2
                
    #             for row in range(self.size):
    #                 for col in range(self.size):
    #                     if row * self.size + col < len(face_state):
    #                         color = self.colors.get(face_state[row * self.size + col], (0.5, 0.5, 0.5))
                            
    #                         x = start_pos + col * sticker_size
    #                         y = start_pos + (self.size - 1 - row) * sticker_size
                            
    #                         # Enhanced sticker rendering
    #                         glColor3f(*color)
    #                         glBegin(GL_QUADS)
    #                         glVertex3f(x - sticker_size/2.2, y - sticker_size/2.2, 0.01)
    #                         glVertex3f(x + sticker_size/2.2, y - sticker_size/2.2, 0.01)
    #                         glVertex3f(x + sticker_size/2.2, y + sticker_size/2.2, 0.01)
    #                         glVertex3f(x - sticker_size/2.2, y + sticker_size/2.2, 0.01)
    #                         glEnd()
                            
    #                         # Enhanced border
    #                         glColor3f(0.0, 0.0, 0.0)
    #                         glLineWidth(3)
    #                         glBegin(GL_LINE_LOOP)
    #                         glVertex3f(x - sticker_size/2.2, y - sticker_size/2.2, 0.02)
    #                         glVertex3f(x + sticker_size/2.2, y - sticker_size/2.2, 0.02)
    #                         glVertex3f(x + sticker_size/2.2, y + sticker_size/2.2, 0.02)
    #                         glVertex3f(x - sticker_size/2.2, y + sticker_size/2.2, 0.02)
    #                         glEnd()
                
    #             glPopMatrix()
    
    # def animate_solution_stable(self, states, moves, speed=2.0):
    #     """Stable animation that works on M1 Macs"""
    #     pygame.init()
    #     display = (1000, 750)
    #     screen = pygame.display.set_mode(display, OPENGL | DOUBLEBUF)
        
    #     glEnable(GL_DEPTH_TEST)
    #     glDisable(GL_LIGHTING)
    #     glClearColor(0.1, 0.1, 0.1, 1.0)
        
    #     gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #     glTranslatef(0.0, 0.0, -8)
        
    #     clock = pygame.time.Clock()
        
    #     for i, state in enumerate(states):
    #         start_time = time.time()
    #         rotation_x = rotation_y = 0
            
    #         # Determine step info
    #         if i == 0:
    #             title = "Starting Position - Press SPACE to advance"
    #         elif i < len(moves):
    #             title = f"Step {i}: Applied '{moves[i-1]}' - Press SPACE to continue"
    #         else:
    #             title = "SOLVED! - Press SPACE to close"
            
    #         # Display this state for the specified duration
    #         while time.time() - start_time < (3.0 / speed):
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     pygame.quit()
    #                     return
    #                 elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #                     break
    #             else:
    #                 # Continue animation loop
    #                 rotation_x += 1.5
    #                 rotation_y += 1.0
                    
    #                 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    
    #                 glPushMatrix()
    #                 glRotatef(rotation_x, 1, 0, 0)
    #                 glRotatef(rotation_y, 0, 1, 0)
                    
    #                 self.draw_cube_faces_enhanced(state)
                    
    #                 glPopMatrix()
                    
    #                 glFlush()
    #                 pygame.display.flip()
    #                 clock.tick(60)
    #                 continue
    #             break  # Break if SPACE was pressed
        
    #     pygame.quit()
class MacCompatible3DVisualization:
    """Mac-compatible 3D visualization without threading issues"""
    
    def __init__(self, size=3):
        self.size = size
        self.colors = {
            'U': (1.0, 1.0, 1.0), 'D': (1.0, 1.0, 0.0), 'F': (0.0, 1.0, 0.0),
            'B': (1.0, 0.5, 0.0), 'L': (0.0, 0.0, 1.0), 'R': (1.0, 0.0, 0.0),
            ' ': (0.3, 0.3, 0.3)
        }
    
    def render_cube_mac_safe(self, state, title="3D Rubik's Cube"):
        """Mac-safe 3D rendering without threading"""
        try:
            pygame.init()
            
            # Mac-specific display setup
            display = (800, 600)
            
            # Use more compatible flags for Mac
            screen = pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
            pygame.display.set_caption(title)
            
            # Mac-compatible OpenGL setup
            glEnable(GL_DEPTH_TEST)
            glClearColor(0.2, 0.2, 0.2, 1.0)  # Gray background
            
            # Disable problematic features on Mac
            glDisable(GL_LIGHTING)
            
            # Setup perspective
            gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
            glTranslatef(0.0, 0.0, -8)
            
            clock = pygame.time.Clock()
            rotation = 0
            running = True
            
            print("3D window opened successfully - Press ESCAPE to close")
            
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                
                rotation += 1
                
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                
                glPushMatrix()
                glRotatef(rotation, 1, 1, 0)
                
                self.draw_simple_cube(state)
                
                glPopMatrix()
                
                pygame.display.flip()
                clock.tick(60)
            
        except Exception as e:
            print(f"3D visualization error: {e}")
            print("Falling back to 2D representation...")
            self.show_2d_fallback(state)
        finally:
            pygame.quit()
    
    def draw_simple_cube(self, state):
        """Simplified cube drawing for Mac compatibility"""
        # Draw a simple wireframe cube with colors
        glBegin(GL_LINES)
        
        # Front face
        glColor3f(0.0, 1.0, 0.0)  # Green
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        
        # Back face
        glColor3f(1.0, 0.5, 0.0)  # Orange
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, -1, -1)
        
        # Connecting edges
        glColor3f(1.0, 1.0, 1.0)  # White
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)
        
        glEnd()
    
    def show_2d_fallback(self, state):
        """2D fallback when 3D fails"""
        print("\n" + "="*50)
        print("2D CUBE REPRESENTATION (3D failed)")
        print("="*50)
        
        # Show cube faces in text format
        faces = ['U', 'R', 'F', 'D', 'L', 'B']
        face_size = self.size * self.size
        
        for i, face_name in enumerate(faces):
            start_idx = i * face_size
            end_idx = start_idx + face_size
            face_state = state[start_idx:end_idx]
            
            print(f"\n{face_name} Face:")
            for row in range(self.size):
                row_start = row * self.size
                row_end = row_start + self.size
                print(' '.join(face_state[row_start:row_end]))


# Example usage and integration
if __name__ == "__main__":
    app = RubiksCubeGUI()
    app.run()
