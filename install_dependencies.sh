mkdir tools
cd tools
git clone https://github.com/SpoonLabs/astor --branch deploy
cd astor
mvn package -DskipTests=true