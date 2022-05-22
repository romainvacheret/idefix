# IDEfix

## Presentation
IDEfix is the integration of an [APR](https://program-repair.org/) tool ([Astor](https://github.com/SpoonLabs/astor)) into an IDE (Visual Studio Code).
It offers fixes for Java programs.
## Prerequisites
*Note: Developed for Unix-based operating systems*

- Git
- JDK 8
- Maven
- Python 3.9
- [IDEfix Visual Studio Code extension](https://github.com/RomainVacheret/idefix-vsc)

## Installation
```bash
git clone https://github.com/RomainVacheret/idefix
cd idefix
./install_dependencies.sh
python3 -m pip install -r requirements.txt

# Note: sudo priviledges are required for the FTP server
sudo -E python3 idefix.py
```

*Note:*
*As mentioned in Astor's documention, you may run into the `Exception in thread "main" java.lang.NullPointerException at com.gzoltar.core.GZoltar.run(GZoltar.java:51)` error when launching an analysis.*
*To fix it, run the following command in Astor's root directory: `mvn install:install-file -Dfile=lib/gzoltar/com.gzoltar-0.0.3.jar -DgroupId=com.gzoltar -DartifactId=gzoltar -Dversion=0.0.3 -Dpackaging=jar`*

