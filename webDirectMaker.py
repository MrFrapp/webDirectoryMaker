import shutil
import os
import sys


def createIndexFile(name):
	baconFile = open(name, 'a')
	baconFile.write('<!doctype>')
	baconFile.write('\n')
	baconFile.write('<html>')
	baconFile.write('\n')
	baconFile.write('<head>')
	baconFile.write('\n')
	baconFile.write('<link type="text/css" rel="stylesheet" href="resources\\css\\style.css">')
	baconFile.write('\n')
	baconFile.write('</head>')
	baconFile.write('\n')
	baconFile.write('<body>')
	baconFile.write('\n')
	baconFile.write('<h1> This is a basic html skeleton file starter! </h1>')
	baconFile.write('\n')
	baconFile.write('</body>')
	baconFile.write('\n')
	baconFile.write('</html>')
	baconFile.close()








def  createCssFile(name):
	baconCss = open(name, 'a')
	baconCss.write('* {')
	baconCss.write('\n')
	baconCss.write('font-family: sans-sarif; color: #e74c3c ')
	baconCss.close()


def makeNewPath(name):
	os.makedirs(name)

def makeResourceFile():
	os.makedirs('NewDirectory\\Resources')
	os.makedirs('NewDirectory\\Resources\\css')
	os.makedirs('NewDirectory\\Resources\\img')
	os.makedirs('NewDirectory\\Resources\\font')
	os.makedirs('NewDirectory\\Resources\\info')

def makeInfoTxt():
	baconTxt = open('info1.txt', 'a')
	baconCred = open('info2.txt', 'a')
	baconCred.write('This directory was made by a program thought of, created, and developed by Ryan DeWolfe! Thank you for using it!!')
	baconTxt.write('This is the info file, in other words, its that READ ME! file that you can put needed info!')
	baconTxt.close()
	baconCred.close()
	


def moveToDirect():
	shutil.move('index.html', 'NewDirectory')
	shutil.move('style.css', 'NewDirectory\\Resources\\css')
	shutil.move('info1.txt', 'NewDirectory\\Resources\\info')
	shutil.move('info2.txt', 'NewDirectory\\Resources\\info')
	

makeNewPath('NewDirectory')
makeResourceFile()

createIndexFile('index.html')
createCssFile('style.css')
makeInfoTxt()
moveToDirect()
