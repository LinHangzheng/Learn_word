# Learn_word
An automatic way to learn word 

To use it, you need create a vocabulary.xlsx file and use each sheet as the different list of vocabulary.
Here I proved my vocabulary.xlsx file. You can modify it as you want.
The frist row is the title and the words will start from the second row and second column.
For more detail, you could see the vocabulary.xls file I uploaded.

In the dist file I also packed the code into a .exe file so you could run it directly. Nonetheless, please pay attention to change path of you vocabulary.xls since the path in my code is E:\TOEFL\vocabulary.xls. You have to change the path in the code and repack it provided you don't want to use the same path as mine.

To pack the code, the convience way to achieve it is to use

pyinstaller -F YOUR_PATH/vocabulary.xls

Then there will be two folders created. Ignore the build folder, the .exe file will be in the dist.

## set mode
after you enter the List number to test, the window will ask you to set the mode about the test, then you need to enter 1 or 0  
0: Normal mode, you will be test all the words in the list in .xls file  
1: Unknown mode, you will only be test by the words you are not familiar with. The unfamiliar level will be recorded into the first column of .xls file. If you don't know the word, the value of the unfamiliar level will always be set to 1, otherwise it will decrease by 1. If the word has unfamiliar level < 1, this word will not be tested in the mode 1 anymore.


