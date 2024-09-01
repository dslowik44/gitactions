import sys 

from io import StringIO

from pylint.lint import Run
from pylint.reporters.text import TextReporter

pylint_output = StringIO()  # Custom open stream
reporter = TextReporter(pylint_output)
Run(["factorial.py"], reporter=reporter, exit=False)
print(pylint_output.getvalue())  # Retrieve and print the text report

"""
from pylint import lint  

THRESHOLD = 9  

run = lint.Run("factorial.py", exit=False) 
print(run)
score = run.linter.stats["global_note"]  

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 
"""
