codes =[]

for a in range(10):
    for b in range(10):
        for c in range(10):
    
                codes.append(f"{a}{b}{c}")

for code in codes:
    print(code)

print(f"\nTotal codes: {len(codes)}")