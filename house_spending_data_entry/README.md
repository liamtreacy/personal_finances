Data Entry

The purpose of this project is to allow for the entry of household related income and expenses, into a csv format, for each month. The location of these files is a seperate git checkout ("household_spending") which must be checkout at at the same folder level as personal_finances.

The tests folder contains unit tests and one file based comparison test, against a known "good" standard.

The usage is intended as follows:
    git checkout household_spending
    git checkout personal_finances
    open a PyCharm project on the personal_finances/data_entry folder
    run run.py and enter your data
    The new file should be present in the household_spending repo and should be committed.

Todos:
    CLI option to run run.py
    CLI option to run the tests
    Maybe integrate the git commit/status at the end, to show the diff or at least that the file was successfully created?
