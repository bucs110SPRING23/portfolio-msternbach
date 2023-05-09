
def star_pyramid(rows):
    stars = "*"
    for row in range(rows):
        print(stars)
        stars = stars + "*"

def rstar_pyramid(rows):
    for i in range(rows,0,-1):
        print("*" * i)

rows = int(input("How many rows: "))
star_pyramid(rows)
rstar_pyramid(rows)