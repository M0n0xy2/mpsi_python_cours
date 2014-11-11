if __name__ == "__main__":
    print(("{} "*8).format(*[chr(c) for c in range(65, 65+8)]))
