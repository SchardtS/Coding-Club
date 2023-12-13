# Santas Little Sorting Problems

## Introduction

Santas little helpers had a little too much fun at their pre-christmas party. When he arrived at work the next day, he did not only find a lot of hungover elves but he also found out that not all of the gift priority lists have been sorted so far. The missing one is for the roughly one million children in Berlin. Since the reliability of his helpers was questionable at this point, he tried to do it himself. So his first instinct was to start a Python script and use `np.sort()` on the list only to find out that someone sabotaged this function. One elf with doubtful programming talent found it funny to mess with all the sorting libraries in this world by creating pull requests for each of them (and of course each version) which would only result in useless gibberish. With some christmas magic and the power of too much alcohol, they were able to enforce acceptance for their pull requests, thus destroying all the current sorting algorithms in the whole world.

At this point Santa was arguing to himself: "Ok Berlin... a city full of hipsters... recycled beer cans as christmas tree ornaments... christmas meals from heirloom vegetables with handcrafted tofu figurines... christmas songs from a record player because of course digital music is so mainstream..." Santa was almost at the point where his justification made sense for him, but luckily he realized: "Santa, you can't just skip the birthplace of the currywurst during the most wonderful time of the year! And think about the children!". Thus, the, not at all programming talented, Santa decided to get some help. Luckily, his Google search resulted in finding a reasearch institute which already had their christmas party on the 14. of December, meaning that everyone should be sober again. He quickly made contact to the resident Data Steward to find a solution to his problem who delightfully handed this task over to everyone else...

## Challenge

You have a file `christmas_gifts.txt` containing one million gifts and their priority number. Sort the list of gifts according to the priorities. Avoid the use of any sorting related packages and implement your own solution in two steps

1. Write a naive sorting algorithm in the most intuitive way you can imagine. Use this to sort only the first `10000` elements of the list.
2. Pick any sorting algorithm from [here](https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms) and try to implement it yourself. Use it again for the first `10000` elements and compare your runtimes.
3. If possible, use it to sort your list.

Try to understand the idea behind your sorting algorithm in order to explain it to you co-workers. If you are highly motivated, you can also try to visualize the runtime comparisons of both algorithms.
