![Python Gif](https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif?cid=ecf05e47ijkcpnadfgcotlidmlq8gjpt2617awzmdn6qspm6&rid=giphy.gif&ct=g)

# Solved

- [x] [download tgz dataset from url](https://github.com/lakshikaparihar/Python-Scripts/blob/7a87ef557a0fa44def4f8479752bb604de578fcb/url-dataset-tgz-download.py)
- [x] [snakecase to camelcase conversion](https://github.com/lakshikaparihar/Python-Scripts/blob/7a87ef557a0fa44def4f8479752bb604de578fcb/snakecase_to_camelcase.py)
- [x] [chuck noris unary message](https://github.com/lakshikaparihar/Python-Scripts/blob/d2cb4a5dfccd69df5f5aeda9d6391c0197173f8b/chuck_noris_unary_message.py) 
- [x] [Separating Lowecase and Uppercase](https://github.com/lakshikaparihar/Python-Scripts/blob/db3f9eea03ea27bda4079bf3a25c5d3b7a1c0dff/separate_lower_uppercase.py)
- [x] [Concatenate two strings](https://github.com/lakshikaparihar/Python-Scripts/blob/0e1c771e65e887de624ec25db4df38868a839cc8/concatenate_two_strings.py) 

## To be solved ....

- [ ] [Who won the marble game?](https://github.com/lakshikaparihar/Python-Scripts/blob/74c3556080683dd19552f07baccfa64632ef6063/Marble_game.py)



<br>
<br>

# How to Contribute 

 1. Fork this Repository
 
 2. Clone the Repository in your local machine
```
$ git clone "https://github.com/lakshikaparihar/Python-Scripts.git"
```

 3. Solve any To be Solved question (Program description is written inside the file itself )
 
 4. Paste the Code into the same file as problem description

 5. If you want to add any new Problem desciption
       * Create a new .py file with the title name and add the Problem description in the file 
       * Add the title in the Readme.md and link it to the file

 6. add and commit the changes in your Repository
 ```
 $ git add <filename>
 ```
 ```
 $ git commit -m "(Your Name and File added)"
```

 7. push the changes to your repository
 ```
 $ git push -u origin branchname
 ```

 8. Generate a pull request (Make sure to add problem name in the title and url in the description)
 

# Synchronize forked repository with upstream repository

 1. Add this repository as an upstream repository
 ```
 $ git remote add upstream https://github.com/lakshikaparihar/Python-Scripts.git
 ```
 2. Fetch all the changes from the repository
 ```
 $ git fetch upstream
 ```
 3. Make sure you are on your working branch
 
 ```
 $ git checkout main
 ```
 4.  Merge the changes from upstream into your local machine
 
```
$ git merge upstream/main
```
 5. Now your local branch is synced with the upstream branch . Push the changes in your forked repository
 ```
 $ git push -f origin main
 ```
