Package name = TOPSIS-Aryan-101803035

# About the project

As the name suggests, this package implements TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) which is a multi-criteria decision analysis method (MCDA or MCDM), which is a technique based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS). 

This package hence provides with the TOPSIS score according to which a model's relative rank with  respect to other models with same number of entries is also provided.


### Installation

Install the package using pip as follows :

```sh
>> pip install TOPSIS-Aryan-101803035==0.0.2
```

### How to run in command prompt
First go to the directory (using cd following by your directory command) where it has been installed (prefreably the directory will be in main python folder -> Libs -> site-packages -> yourpackagename) then run the following commands : 
```sh
>> python TOPSIS.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```
Eg: 
```sh
>> python TOPSIS.py data.csv “1,1,1,2” “+,+,-,+” result.csv





[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
