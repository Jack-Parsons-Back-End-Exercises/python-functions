def run(*kids):
    for kid in kids:
        print(f'{kid} ran like a fool!')

def swing(*kids):
    for kid in kids:
        print(f'{kid} swung so high!')

def slide(*kids):
    for kid in kids:
        print(f'{kid} slid down the slide.')

def hide(*kids):
    for kid in kids:
        print(f"I can't find {kid} anywhere...")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide("Henry", "Heather", "Haley", "Hugh")