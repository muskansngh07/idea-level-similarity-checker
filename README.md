# idea-level-similarity-checker

A small tool to check whether two research ideas use the same underlying method which means that they run on the same idea but on different wordings. 

Here, there's no comparison made on the basis of full length of the papers but on their methodologies.

<h2>Steps for Paper 1</h2>

1. For a given input x, generate m response samples s1, . . . , sm.
2. Calculate the pairwise similarity scores a(sj1 , sj2 ) for these m responses.
3. Compute an uncertainty estimate U(x) or a confidence score C(x,sj) using the similarity values.
