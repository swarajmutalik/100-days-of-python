def func1():
    try:
        l = [1,6,7,8]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")

x = func1()
print(x)
