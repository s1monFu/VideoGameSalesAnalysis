# VideoGameSalesAnalysis
## Introduction
Video game is loved by thousands of people as an entertainment. Various types of games bring people different kinds of fun. The purpose for this project is to determine what type of game is people's favorite by analyzing global game sale of games from different game genres. 
## Methods
This project tries to build a regression model based on skleran using Python. It uses useful tools such as OneHotEncoder and PolynomialFeatures to better fit the model. This project analyzes game sales based on a game sale dataset. It tries to determine what types of games are more popular and what factors contribute the most. 
## Analysis
### Q1: What genres of games are more popular?
![image](https://user-images.githubusercontent.com/49095933/147861760-2899ca6c-c7d7-4ce5-a6a6-11b041d43c4b.png)

Based on the graph of game sales of different game genres, it is clear that action, sport, and shooter games are the most top-selling games. Meanwhile, puzzle, adventure, and strategy games have the lowest sale. The average game sale of all types of games is around 750, and action, sport, shooter. role-playing, platform, and misc games are above average.

### Q2: How do sales of different types of games change overtime?
![image](https://user-images.githubusercontent.com/49095933/147861778-ae80f199-df17-44e2-9e3b-eaf56983fafb.png)

According to the overtime game sale graph, the game sales of all game gradually increases and reached peak around 2005 to 2010. Game sales of all genres of game drastically decreases after that period.

### Q3: A linear regression model for sale prediction
Using sklearn and python, this project tries to build a regression model for sale prediction. Variables including genre, year, and platform are considered. Different models are created and tested based on these variables. The highest score generated from the models, however, is around 0.05. The model takes genre, platform, and year into consideration and applies a polynomial feature of degree 2.


## Discussion
TBD
## Reference
The dataset is collected by Gregory Smith on Kaggle from https://www.kaggle.com/gregorut/videogamesales. 

