import os
import argparse

#Add Test Case Names to be added
addActionMap = {
    "pay_init":[
        "TestPayInitSuccess",
        "TestPayInitForMissingCardNumber",
        "TestPayInitForMissingPaymentId"
    ],
    "pay_verify":[
        "TestPayVerifySuccess",
        "TestPayVerifyForInvalidAmount",
    ]
}

#Add Test Case Names to be deleted
deleteActionMap = {
    "pay_init":[
        "TestPayInitSuccess",
        "TestPayInitForMissingCardNumber",
        "TestPayInitForMissingPaymentId"
    ],
    "pay_verify":[
        "TestPayVerifySuccess"
    ]
}

#Add the base path
base = "/Users/vishalashank/go/src/github.com/razorpay/mozart/app/testdata/payments/bajajfinserv/v2"

#Add the template if any for golden extension
goldenTemplate = '''
{
    "responseStatusCode": 200,
    "responseBody": {

    }
    "external_trace_id": "DUMMY_REQUEST_ID",
    "mozart_id": "DUMMY_MOZART_ID"
}
'''
#Add the template if any for gatewayResp extension
gatewayRespTemplate = ""
#Add the template if any for input extension
inputTemplate = ""

#Parser
parser = argparse.ArgumentParser(description='generate or delete test case files')
parser.add_argument("-d","--delete", help='delete test cases from delete action map', action="store_true")
parser.add_argument("-o","--override", help="override test case files if present", action="store_true")
args = parser.parse_args()

extensions = {
    "golden":goldenTemplate,
    "gatewayResp":gatewayRespTemplate,
    "input":inputTemplate
}

if args.delete :
    if os.path.exists(base):
        for action in deleteActionMap :
            actionPath = base + "/" + action
            if os.path.exists(actionPath):
                for extension in  extensions :
                    for test in deleteActionMap[action]:
                        desiredPath = base + "/" + action + "/" + test + "." + extension
                        if os.path.exists(desiredPath):
                            os.remove(desiredPath)
else :
    if not os.path.exists(base):
            os.mkdir(base)
    for action in addActionMap :
        actionPath = base + "/" + action
        if not os.path.exists(actionPath):
            os.mkdir(actionPath)
        for extension in  extensions :
            for test in addActionMap[action]:
                desiredPath = base + "/" + action + "/" + test + "." + extension
                if args.override or (not os.path.exists(desiredPath)):
                    f = open(desiredPath, "w+")
                    f.write(extensions[extension])
                    f.close()
