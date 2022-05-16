# IDEfix

## Prerequisites
*Note: Developed for Unix-based operating systems*

- Git
- JDK 8
- Maven
- Python 3.9
- [The Visual Studio Code extension](https://github.com/RomainVacheret/idefix-vsc)

## Installation
```bash
git clone https://github.com/RomainVacheret/idefix
cd idefix
./install_dependencies.sh
python3 -m pip install -r requirements.txt

# Note: sudo priviledges are required for the FTP server
sudo -E python3 idefix.py
```