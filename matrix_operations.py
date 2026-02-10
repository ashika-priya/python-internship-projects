import numpy as np

print("🧮 Matrix Operations Tool")

# Function to input a matrix
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row-wise:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)

    return np.array(matrix)

# Menu loop
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        print("\nResult (A + B):")
        print(A + B)

    elif choice == "2":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        print("\nResult (A - B):")
        print(A - B)

    elif choice == "3":
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        print("\nResult (A × B):")
        print(np.dot(A, B))

    elif choice == "4":
        A = input_matrix("Matrix")
        print("\nTranspose:")
        print(A.T)

    elif choice == "5":
        A = input_matrix("Matrix")
        print("\nDeterminant:")
        print(np.linalg.det(A))

    elif choice == "6":
        print("Exiting program. Bye 👋")
        break

    else:
        print("Invalid choice. Try again.")
