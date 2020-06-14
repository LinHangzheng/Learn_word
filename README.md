# Learn_word
An automatic way to learn word 

To use it, you need create a vocabulary.xlsx file and use each sheet as the different list of vocabulary.
Here I start with the list 7 so that you need to change the sheet offset.
The frist row is the title and the words will start from the second row and second column.
For more detail, you could see the vocabulary.xlsx file I uploaded.

In the dist file I also packed the code into a .exe file so you could run it directly if you want. Nonetheless, please pay attention to change path of you vocabulary.xlsx since the path in my code is E:\TOEFL\vocabulary.xlsx. You have to change the path in the code and repack it provided you don't want to use the same path as mine.

To pack the code, the convience way to achieve it is to use

pyinstaller -F YOUR_PATH/vocabulary.xlsx

Then there will be two folders created. Ignore the build folder, the .exe file will be in the dist.

