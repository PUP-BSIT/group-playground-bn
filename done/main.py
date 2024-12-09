from pack import delima, ynion, relente

def main():
    delima.get_username()
    relente.get_password()
    
    radius = int(input("Enter radius: "))
    result = ynion.calculate_circle_area(radius)
    print(f"Circle Area: {result}")
    
main()