import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui import RubiksCubeGUI

def main():
    print("🚀 Starting Rubik's Cube Solver GUI...")
    print("📋 Features:")
    print("  • Visual interface with buttons")
    print("  • 3D cube visualization") 
    print("  • Support for 2x2, 3x3, 4x4 cubes")
    print("  • Real-time solving and animation")
    print("\n🎬 Launching GUI...")
    
    try:
        # Create and run the GUI
        app = RubiksCubeGUI()
        app.run()
    except Exception as e:
        print(f"❌ Error starting GUI: {e}")
        print("\n🔧 Make sure you have installed:")
        print("  pip3 install tkinter pygame PyOpenGL PyOpenGL_accelerate kociemba")

if __name__ == "__main__":
    main()
