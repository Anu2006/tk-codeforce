from setuptools import setup

setup(
    name = "codeforces-ranking",
    version = "2.0",
    author = "Anupama",
    author_email = "ranilcd@gmail.com",
    description = "shows the ratings of a user when the user name is entered",
    license = "BSD",
    packages=('tk_codeforce',),
    entry_points = {
        'gui_scripts' : ['tk-codeforce = tk_codeforce:tk_codeforce']
    },
    data_files = [
        ('/tk_codeforce', ['tk-codeforce.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
