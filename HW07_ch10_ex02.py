# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(lst):
    new_list = []
    for item in lst:
        if isinstance(item, list):
            #capitalize and append
            new_list.append(capitalize_nested(item))

        else:
            new_list.append(item.capitalize())


    return new_list


def main():
#    print(capitalize_nested(['apple', ['bear'], 'cat']))
    pass
if __name__ == '__main__':
        main()