"""Algorithm shunting yard implementation on Python."""

import data.stack as st

# Initializate a new dictionary in order to separate operators.
data_types = {
    'sin': 1,
    'cos': 1,
    '+': 2,
    '−': 2,
    '*': 3,
    '/': 3,
    'x': 3,
    '×': 3,
    '÷': 3,
    '^': 4,
    ')': 0,
    '(': 0,
}


def shunting_yard(ejemploCatch):
    """From a string, do a implementation of shunting yard algorithm."""
    ejemploCatch = ejemploCatch.split(' ')
    # With the implementation of the Stack data type, is created the operator
    # stack and the output stack.
    output = st.stack()
    operator = st.stack()
    for i in range(len(ejemploCatch)):
        if ejemploCatch[0] == '(':
            operator.push_up(ejemploCatch[0])
        elif ejemploCatch[0] == ')':
            while operator.head() != '(':
                output.push_up(operator.head())
                operator.pop_up()
            operator.pop_up()
        else:
            # Try to convert the ejemploCatch[0] to integer, if is not able
            # them is a operator.
            try:
                int(ejemploCatch[0])
            except ValueError:
                if operator.isEmpty():
                    operator.push_up(ejemploCatch[0])
                else:
                    if(
                      data_types.get(operator.head()) >
                      data_types.get(ejemploCatch[0])):
                        output.push_up(operator.head())
                        operator.pop_up()
                        operator.push_up(ejemploCatch[0])
                    elif(
                         data_types.get(operator.head()) <
                         data_types.get(ejemploCatch[0])):
                        operator.push_up(ejemploCatch[0])
                    else:
                        if ejemploCatch[0] == '^':
                            operator.push_up(ejemploCatch[0])
                        else:
                            output.push_up(operator.head())
                            operator.pop_up()
                            operator.push_up(ejemploCatch[0])
            else:
                output.push_up(ejemploCatch[0])
        ejemploCatch.pop(0)

    # If there is any operator in the operator stack, so it push it to the
    # output and pop it from the stack, until the operator stack is empty

    while operator.isEmpty() is not True:
        output.push_up(operator.head())
        operator.pop_up()

    output.print()
