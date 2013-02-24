si601_project
=============

Repository for code and documentation related to the Health Data Project for SI601.

This bundle includes all desired output in its final state.  However, you may re-create the entire output bundle including
./HealthDataMap/health.db and all tsv files in the output directory by running ./src/master_script.py.  Before running, please
ensure that you install the 'tldextract' Python module first.  If using pip, the command is 'pip install tldextract'.
Note that there is a portion of code in languages.py that pulls all redirect links from every HealthMap instance link.  This
takes an extremely long time to execute.  Uncomment at your own peril. 