mkdir tools
cd tools
git clone https://github.com/SpoonLabs/astor --branch release
cd astor
mvn package -DskipTests=true
