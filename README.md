# Python Flask Dashboard to demonstrate an Agile workflow

This repo is created from the following template: https://github.com/IAM-lab/HIE-skeleton as part of a HDR UK workshop.

## Set up and use
* Clone the repo
* `python run.py` to launch the Flask app connection
* Go to "http://127.0.0.1:5000/dashboard/home" in your browser to view the dashboard.

## Sprint tasks
### Sprint 1:
* Add data for the 3 remaining tiles across the top of the dashboard screen. This is to include:
    * The average ACT cost
    * The description of the item with the max quantity, and a percentage bar showing what % of all prescriptions this is
    * The number of unique items in the dataset
* Add some information to the “About” popup to detail the purpose of the dashboard and details of your team
* Add some unit tests to the dashboard to test the new functionality that you have added so far
* Add some form of documentation for example a readme file in your repositories.

### Sprint 2:
* Add percentage bars to the “Infection treatment drug % of all infection treatments” section. This should include the % of the following out of the total of these drug groups:
  * Antibacterials
  * Antifungal
  * Antiviral
  * Antiprotozoal
  * Anthelminics
* Add some unit tests to the dashboard to test the new functionality that you have added so far
* Add a menu item called “Generate report” which adds functionality to generate a downloadable/printable summary of the information represented in the dashboard
* Add functionality to the “Creatinine clearance calculator” using the "Cockroft Gault Equation"

## Notes on unit testing
* Install [`nose2`](https://docs.nose2.io/en/latest/)
* Go to project directory and execute `nose2 -v`
* Note: that each test file must start test_filename e.g. test_databases.py and each test within should also start with test_ e.g.
```python
def test_my_test_name(self):
    self.assertEqual ....
```
