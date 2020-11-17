# lubrizol-data-selection
## Group 10
### SCC461 MSc Data Science - Lancaster University



# Introduction
Lubrizol are speciality chemicals experts. Their chemistry enhances
practically every facet of life, from the way you move, to how you
take care of yourself, to how you work. The Statistics and Data
Analytics team builds models to help predict how our chemistry will
perform and builds tools to speed up the product development
process. 

This project will examine how our products, and as a result our
different types of chemistry, perform within a test. 

Questions which will be addressed include:
- What chemistry groups are influential on a test? And which
are not?
- Within chemistry groups, which predictor variables best
describe the effect?
- Are there any outliers in the data? How do these influence
the results?
- Building a robust model which predicts how their
chemistry performs for new formulations?

# How to contribute

If you use windows, and are unfamiliar with git, this provides a quick guide:

Download git : https://git-scm.com/

Other options are availble, but this will be command line based

## Clone this repo

Go to where you plan to keep this project, and right click, select "Git Bash Here" and then run the following command

``` 
git clone https://github.com/K-Molloy/lubrizol-variable-selection.git 
```

## Create a branch

Go into the folder you just created, either with `cd` or by creating a new terminal. And create a branch using the `git checkout command` and replace 'your-name' with your first name.

```
git checkout -b <your-name>
```
## Make changes and commit

If you add, delete or change any file in the project then run 
```
git status
```
you can see the changes you have made. Add those changes by running
```
git add README.md
```
for each file, you can use the flag `-A` but I would avoid this at first. You then commit using, the `-m` indicated adding a message to your commit, this can be helpful when looking at previous work you have done
```
git commit -m "Adding README.md"
```

## Push changes to github

Push your changes to github using `git push`, with the branch name you created earlier

```
git push origin -u <your-name>
```
## Submit changes for review

If you go to the github repo and find your branch, there will be a `compare and pull request` button. Click that and add a few comments about what changes have been made in your branch, then submit the pull request. Soon the changes will be merged into the main branch


## Further Reading

https://www.atlassian.com/git/tutorials/syncing
