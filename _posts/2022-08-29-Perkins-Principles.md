---
title: "Making Learning Whole"
description: "Applying Perkins' Seven Principles to Digital Engineering Content"
author: <a href='http://www.ucalgary.ca/~yves.pauchard'>Yves Pauchard<a/>
categories: [pedagogy]
layout: post
toc: true
---


# Introduction

In the Spring 2022 term, the Digital Engineering Fellowship Program supported students in Schulich School of Engineering at the University of Calgary to develop learning materials that would enhance courses in the Digital Engineering Minor. 

Fellows identified topics of interest that align with current Digital Engineering courses ranging from Software development, Machine Learning, Internt of Things, and Cyberphysical Systems. Subsequently, they researched the topic, build demonstrators and summarized their activity in a blog post available on this site.

To guide Fellows pedagogially, we studied Perkins *Seven Principles* explained in this article:
[Education at Bat: Seven Principles for Educators \| Harvard Graduate School of Education](https://www.gse.harvard.edu/news/uk/09/01/education-bat-seven-principles-educators)

Below are notes from our discussions and resarch highlighting possible applications to Digital Engineering for each of the seven principles.

# 1. Play the whole game

For a given topic, we find a junior version of the game that can be played, end-to-end.

In digital engineering, this can often mean to have software libraries that abstract away the nitty-gritty details and allow to implement the overall workflow with ease. For example, using sklearn to perform machine learning facilitates connecting individual steps without worrying about algorithm implementation.

Furthermore, data might be made available to skip the data collection step, maybe even cleaning the data boferhand so that the focus can be on training and evaluating a model.

# 2. Make the game worthwhile playing

This topic speaks to developing an intrinsic motivation for learning.

One approach is demonstrating how a practical skill will result from the learning activity. For example, building a website, or understanding a real world puzzle.

Another approach is to use *generative topics*:

From [Generative Topics - Learning Praxis](https://sites.google.com/site/learningpraxis/generative-topics)
> Generative topics propose ideas for discussion on a topic that invites students to relate it to other topics and aspects of their personal life.

From [Project Zero - Generative Topics](https://www.wis.edu/uploaded/Academics/Project_Zero/Generative_Topics_By_Ron_Ritchhart.pdf)

> Perkins (1992) puts forth three essential criteria by which the generativity of a topic can be judged: centrality to the discipline, richness of connections, and accessibility to the students. A generative topic, therefore, is the origin from which investigations are spawned, new concepts and understandings are produced, and connections are created. A generative topic is the parent idea pregnant with possibilities for explorations.

and:

> a generative topic is concerned first and foremost with the core ideas of the discipline, building disciplinary understanding by focusing on these central ideas.

In machine learning, the *hook* can be *learning*. All students are familiar with, well, proficient at learning. How would you teach a machine to learn? How does the machine learn? Furthermore, training and test sets are equivalent to practice exam questions (training) vs real exam (test) - the goal is not to memorize and do well on the training data, the goal is to generalize well on the test data.


# 3. Work on the hard parts

Drill/repetition/memory work on important topics. 

This could mean practicing loading/cleaning/inspecting data using Pandas: Get many csv files and practice the workflow.

Similarly, analyzing machine learning model evaluation results could be practiced: Given train-validation scores, what is the next step?

Memorizing certain programming language elements would fall under this category as well. Starting from a blank page, implement and run *Hello World* in the languages you know. Do the same for other common tasks: Read/write files, gradient descent algorithm, etc.

Finally, it might mean unpacking the *whole game* used in principle 1 and investigate what is under the hood. What are the algorithm details? How are these implemented? Etc.

# 4. Play out of town

Taking your knowledge and apply it to a different but related field.

For example: Implement a neural network going from fastai/pytorch to keras/tensorflow.

# 5. Uncover the hidden game

Use “What do you see going on? What do you see that makes you think so?” 

This is aiming at uncovering strategies, e.g. strategies of problem solving, "What do you do to solve problems". Perkins mentions that simply teaching strategies is not enough, and there needs to be an element of self-management on the part of the student. 

In Python programming for example, when do you use list comprehensions vs. regular loops? While there might be some clear-cut situations, you will develop your own strategies where you use tools.

Another example would be "How are introductions to programming languages structured?". It usually starts with explaning if it is a compiled or an interpreted language and what you need to do to run a program. Then *Hello World*, followed by variable type, operators, structural constructs (if-else, for, etc.), functions, objects, I/O, etc.

In that sense it is about discovering higher-level patterns in the topics you learn through reflection. It seems closely related to Principle 7. Learn the game of learning.

# 6. Learn from the team

This is probably the principle already in use often - Peer work, project-based learning, capstone projects, hackathons, etc. In a programming course it would be nice to add peer code review: Students review eachothers code and provide feedback. How well does this work with lower levels of proficiency?

# 7. Learn the game of learning

Students take charge of their leanring path. I read this as less structure and pulling through students, more self-dicovery. Does that work in a minor with a high workload?

Learning is life-long, especially in engineering. We have to become good at learning new technologies and methodologies.

# Summary

In our discussions, DE Fellows were excited to consider principles:
- *1. Play the whole game*
- *2. Make the game worthwhile playing*
- *4. Play out of town*

and you will find references to these topics at the start of many of the blog posts from the Spring 2022 edition. Enjoy!
