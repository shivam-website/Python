def main():
    try:
        a = int(input("Enter a num:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return
        
    finally:
        print("Try block finally worked.")#always run  , even it is returned

main()