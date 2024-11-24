from pack import delima, ynion

def main():
    delima.get_username()
    
    radius = int(input("Enter radius: "))
    result = ynion.calculate_circle_area(radius)
    print(f"Circle Area: {result}")
    
main()