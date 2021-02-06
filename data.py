## API

# import requests
#
# parameters = {
#     "amount":10,
#     "type": "boolean"
# }
#
# response = requests.get("http://opentdb.com/api.php", params = parameters)
# response.raise_for_status()
# r = response.json()
#
# questions = r["results"]

## Data Science and stats questions

questions = [
    {
        "question": "Suppose, in a testing hypothesis for the population proportion, the p-value is computed to "
                    "be 0.043. The null hypothesis should be rejected if the chosen level of significance is .05",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "question": "In forming a 90% confidence interval for a population mean from a sample size of 22, the number"
                    " of degrees of freedom from a t-distribution equals 22.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "question": "The answer to the question 'what is your sleeping bag temperature rating'"
                    "? is an example of a ratio scaled variable.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "question": "The median of the values 3.4,4.7,1.9,7.6, and 6.5 is 1.9",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "question": "Linear Regression is a supervised machine learning algorithm",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "question": "Logarithmic Loss and RMSE is a method we use to find the best fit line for data in Linear "
                    "Regression ",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "question": "Lasso Regularization can be used for variable selection in Linear Regression",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "question": "The lower the residuals, the better.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "question": "Suppose Pearson correlation between V1 and V2 is zero. In such case, is it right to conclude that"
                    " V1 and V2 do not have any relation between them?",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "question": "If most students scored A's and B's on an exam, and few make D's and F's, then a skewed curve"
                    "(distribution) will result",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    }
]


# ## SQL
#
# questions = [
#     {
#         "question": "The condition in a WHERE clause can refer to only one value.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "question": "SQL is case sensitive",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "question": "The SELECT command with its various clauses, allows users to query they data contained in"
#                     "the tables",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "question": "The DISTINCT keyword allows a function to consider non-duplicate values",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "question": "All group functions ignore null values",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "question": "COUNT(*) returns the number of columns in a table",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "question": "INSERT statement does not allow copying rows from one table to another",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "question": "A view doesn't have data of its own",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "question": "A NULL value is the same as zero or a blank space",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "question": "A NULLIF function compares two expressions. If they are equal, the function returns NULL",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
