# Scrabble-Solver
Python program to detect scrabble blocks using Computer Vision and use my Word Finder algorithm to iteratively try all possible words on the game board using PyAutoGUI automation

My aim is to detect the boxes using OpenCV Computer Vision methods to find out the longest box group at the beginning of the game stage. The algorithm is going to iteratively try all the possible words that has the length with the consecutive boxes either vertical or horizontal and consist of the given letters located at the bottom of the game board.

## Stage 1: Detect all the required boxes to interact with. 
Most probably using computer vision is not the fastest way to solve this puzzle. However, I'm too far away from worrying about the fastest way. This project is a representative of a first step on my way to learn (and eventually master) Computer Vision.

![game_screen_result](https://user-images.githubusercontent.com/36932448/62078270-e6c24880-b254-11e9-8d14-ff0ad35b01ed.png)
