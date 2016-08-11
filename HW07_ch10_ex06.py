# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(lst):
    if lst == sorted(lst):
        print("Yayy!")
        return True
    else:
        print("Nayy")
        return False

def main():
#    print(is_sorted([1, 2, 3]))
    pass
if __name__ == '__main__':
        main()