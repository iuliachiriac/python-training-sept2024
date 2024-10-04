# Python Training

## Project installation with PyCharm

1. Clone the repository inside `PycharmProjects` directory:

    ```shell
    cd ~/PycharmProjects/
    git clone https://github.com/iuliachiriac/python-training-sept2024
    ```
   
1. Open PyCharm, go to `File` -> `Open` and select the `python-training-sept2024` directory.
1. Select `Trust Project` in the dialog.
1. Next, PyCharm will advise you to create a Virtual Environment for your project. Leave the default options selected and click OK.
1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

## Project installation without PyCharm

1. Clone the repository:

    ```shell
    git clone https://github.com/iuliachiriac/python-training-sept2024
    ```

1. Move to project directory:
    ```shell
    cd python-training-sept2024
    ```

1. Create a virtual environment:

    ```shell
    virtualenv venv
    ```

1. Activate virtual environment:

    Linux/MacOS:
    ```shell
    source venv/bin/activate
    ```

    Windows:
    ```shell
    venv\Scripts\activate
    ```

1. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

## Getting solutions
After each day solutions will be submitted to this repo.
Since you've been working on your exercises and maybe altered files in the repo directory, use the following in a terminal, in the repo directory:

```shell
# forget unwanted changes in docs
git checkout -- docs/
# save your changes
git stash
# get the updates
git pull
# restore your changes
git stash pop
```

## Further practice

1. https://www.hackerrank.com/ - HackerRank offers a wide variety of coding challenges in Python, ranging from easy to difficult. It's a great resource for practicing coding skills and preparing for technical interviews.
1. http://www.pythonchallenge.com - Python Challenge is a series of puzzles that require the use of Python programming skills to solve. It's a fun way to practice Python and learn new programming concepts.
1. https://projecteuler.net - Project Euler is a series of challenging mathematical and computational problems that require the use of programming skills to solve. It's a great resource for practicing Python and learning new math concepts.
1. https://leetcode.com - LeetCode offers a large collection of coding problems in Python, many of which are commonly asked in coding interviews. It's a great resource for practicing coding skills and learning algorithms.
1. https://www.codewars.com - Codewars offers a variety of coding challenges in Python, ranging from easy to difficult. It's a great resource for practicing coding skills and improving problem-solving abilities.
1. https://www.coursera.org/specializations/python - Python for Everybody is a free online course offered by the University of Michigan that teaches the basics of Python programming. It's a great resource for beginners who want to learn Python programming.
1. https://www.codecademy.com - Interactive programming courses, some free and others paid. It features small modular courses to solve particular problems and a built-in code editor that gives you feedback on solutions. 
1. https://python.swaroopch.com - "A Byte of Python" is a free book on programming using the Python language. It serves as a tutorial or guide to the Python language for a beginner audience.
1. https://realpython.com - Tutorials and various Python-related subjects covered in depth.
1. https://docs.python-guide.org - Best practice handbook for the installation, configuration, and usage of Python on a daily basis.
1. https://github.com/satwikkansal/wtfpython - Surprising snippets in Python.
1. https://www.pythonanywhere.com - Online Python IDE. Allows you to write and execute code on any machine with a browser.
1. Contribute to an open source project. Find a project that you love and use. Some projects have a contributing guide (e.g. [Django](https://docs.djangoproject.com/en/dev/internals/contributing/)), for the other you can simply go to their GirHub page and search for unassigned issues. The other contributors will be happy to help you understand the requirements, review your code and guide you towards a solution. 

## Contact
Iulia Chiriac <iulia.chiriac.a@gmail.com>

## Feedback form
https://forms.gle/5jfT7kcL2fbPJ7vLA
