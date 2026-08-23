from operations import add, subtract
import utils as u

def main():
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print(u.banner("Finished"))

if __name__ == "__main__":
    main()
