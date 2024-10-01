
# Msfvenom Console Application

This project is a Python script that uses `msfvenom` to infect files in the `upload` directory and saves the infected files in the `infected` directory. The script can either take a reverse shell address from the user or read it from a `config.fkn` file if available.

## Project Structure

```
msfvenom_infector_project/
    ├── infector.py          # The main Python script
    ├── config.fkn           # (Optional) File for reverse shell configuration
    ├── README.md            # Documentation of the project
    ├── upload/              # Directory where files to be infected are placed
    └── infected/            # Directory where infected files are saved
```

## Features

- **Infect files**: The script uses `msfvenom` to generate a payload and infect files located in the `upload` directory.
- **Customizable reverse shell**: You can provide the reverse shell IP and port via a `config.fkn` file, or the script will prompt you for the values.
- **Automatic infected file management**: Infected files are automatically saved in the `infected` directory with a prefixed filename.

## Requirements

- **Kali Linux**: This script is designed to run on Kali Linux.
- **Python 3.x**: The script is written in Python 3.
- **Metasploit Framework**: Required to use the `msfvenom` command.

### Installation on Kali Linux

If you haven't already installed Python 3 or Metasploit, you can install them using the following commands:

```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install metasploit-framework
```

## Usage

1. **Prepare the `upload` directory**:
   Place the files you want to infect into the `upload/` directory. You can create the directory with the following command if it doesn't exist:
   ```bash
   mkdir upload
   ```

2. **Set the reverse shell address**:
   You can either:
   - Create a `config.fkn` file with the reverse shell IP and port in the format `LHOST:LPORT`.
   - OR, the script will prompt you to enter the reverse shell address manually.

3. **Run the Python script**:
   To run the script, simply use:
   ```bash
   python3 infector.py
   ```

4. **Check the `infected` directory**:
   The infected files will be saved in the `infected/` directory, which is created automatically if it doesn't exist.

## Example

To infect files using a reverse shell with IP `192.168.1.100` and port `4444`, create a `config.fkn` file with the following content:

```
192.168.1.100:4444
```

Then, simply run:

```bash
python3 infector.py
```

Infected files will be saved in the `infected` directory with the filename prefix `infected_`.

## Notes

- Ensure that `msfvenom` is correctly installed and configured on your system.
- Modify the payload type in the script if you want to infect non-Windows files or use different `msfvenom` options.

