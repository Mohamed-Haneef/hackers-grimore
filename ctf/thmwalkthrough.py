import os
import argparse

def create_walkthrough(challenge_name):
    dir_name = "thm_" + challenge_name
    formatted_name = challenge_name.replace("_", " ").title()
    file_name = "walkthrough.md"
    
    file_content = f"""# Tryhackme | {formatted_name} Walkthrough

Welcome to this walkthrough for the TryHackMe challenge "{formatted_name}". In this guide, I will take you through the steps to solve the challenge, explain key concepts, and provide hints along the way.

## About Me

I am Mohamed Haneef, a cybersecurity enthusiast with a passion for solving Capture The Flag (CTF) challenges. I enjoy exploring new vulnerabilities, learning security techniques, and applying them in real-world scenarios. You can connect with me on [LinkedIn](https://linkedin.com/MohamedHaneef22).

*** written by [@mohamedhaneef](https://linkedin.com/MohamedHaneef22) ***
"""
    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    file_path = os.path.join(dir_name, file_name)
    
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    print(f"Walkthrough file created successfully in {dir_name}/{file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a detailed walkthrough file for a TryHackMe challenge.")
    parser.add_argument("challenge_name", help="The challenge name (in the format 'challenge_name').")
    
    args = parser.parse_args()
    
    create_walkthrough(args.challenge_name)
