# VideoGameSalesAnalysis

## Introduction
The video game is loved by thousands of people as entertainment. Various types of games bring people different kinds of fun. The purpose of this project is to determine what type of game is people's favorite by analyzing the global game sale of games from different game genres. 

## Methods
This project tries to build a regression model based on sklearn using Python. It uses useful tools such as OneHotEncoder and PolynomialFeatures to better fit the model. This project analyzes game sales based on a game sale dataset. It tries to determine what types of games are more popular and what factors contribute the most. 

## Analysis
### Q1: What genres of games are more popular?
![image](https://user-images.githubusercontent.com/49095933/147861760-2899ca6c-c7d7-4ce5-a6a6-11b041d43c4b.png)

Based on the graph of game sales of different game genres, it is clear that action, sport, and shooter games are the most top-selling games. Meanwhile, puzzle, adventure, and strategy games have the lowest sale. The average game sale of all types of games is around 750, and action, sport, shooter. role-playing, platform, and misc games are above average.

### Q2: How do sales of different types of games change overtime?
![image](https://user-images.githubusercontent.com/49095933/147861778-ae80f199-df17-44e2-9e3b-eaf56983fafb.png)

According to the overtime game sale graph, the game sales of all games gradually increases and reached a peak around 2005 to 2010. Game sales of all genres of the game drastically decrease after that period.

### Q3: A linear regression model for sale prediction
Using sklearn and python, this project tries to build a regression model for sale prediction. Variables including genre, year, and platform are considered. Different models are created and tested based on these variables. The highest score generated from the models, however, is around 0.05. The model takes the genre, platform, and year into consideration and applies a polynomial feature of degree 2.

## Discussion
From the graphs, we can see people's preference on the type of games globally and how that preference changes over time. Action, sport, and shooter are three genres that most gamers love globally. However, the genre is not strongly related to game sales and is be a strong factor in predicting game sales, according to the linear regression model. Other variables such as the platform games are on and the game release year also do not contribute to the prediction of game sale. It seems reasonable to conclude that external factors such as game genre, game release platform, and the game release year are not important when it comes to game sales. Further research may look into whether other factors, including content quality, gamer feedbacks, social media comments, would affect game sales.
## Reference
The dataset is collected by Gregory Smith on Kaggle from https://www.kaggle.com/gregorut/videogamesales. 

