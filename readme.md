This script can be used to add or delete the files related to test case with sample template if any.

To add test cases
* Add abs base path for test case. ex: "/Users/username/go/src/github.com/razorpay/mozart/app/testdata/service/gateway/v1"
* Add the test case names in addActionMap.
* Add the test case names in deleteActionMap for any test case files to be deleted and run with -d argument.
* Templates for each extension can be added like for golden in goldenTemplate.

Command line arguments:
* -o overides file with same testcase name if present
* -d deletes the test case files mentioned in deleteActionMap