
setup:
	sudo apt-get update
	sudo apt-get install npm nodejs-legacy
	sudo npm install -g grunt-cli
	npm install

mutara:
	#rm -rf mutara
	grunt swatch:mutara

vurple:
	#rm -rf vurple
	grunt swatch:vurple
