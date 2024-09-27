from itertools import zip_longest

def bucket(size, initial = True):
    """
   Create bucket of specified sized.
   Params:
        size -- 
        initial -- 
    Returns:
        This return a list with bucket chuncks, which can be built by looping on it.
   """ 
    length = size
    AVAILABLE_WATER = 4
    specified_index = [n for n in range(1, length+1)]
    dummy_bucket = f"""
 +------+
    {length}L   
    """
    dummy_bucket = dummy_bucket.splitlines()
    if initial:
        blockade = []
        for n in specified_index:
            value = "|      |"
            dummy_bucket.insert(n, f"{length}{value}")
            length -= 1
    else:
        blockade = [n for n in range(1, length + 1 - AVAILABLE_WATER)]
        for n in specified_index:
            value = "|wwwwww|" if n not in blockade else "|      |"
            dummy_bucket.insert(n, f"{length}{value}")
            length -= 1

    # Add white space to align bucket horizontally from bottom
    if size < 8:
        white_space = 8 - size
        for n in range(white_space):
            dummy_bucket.insert(0, "  ")

    return dummy_bucket

for bucket_xl, bucket_md, bucket_sm in zip_longest(bucket(8), bucket(5), bucket(3), fillvalue=" "):
    print(bucket_xl, bucket_md, bucket_sm)


playing = True
while playing:

    option = """
You can:
  (F)ill the bucket
  (E)mpty the bucket
  (P)our one bucket into another
  (Q)uit
"""
    print(option)
    user_input = str(input(">: "))
    if user_input.upper() == "F":
        print("Select a bucket 8, 5, 3 or QUIT: ")
        user_input = int(input(">: "))
        if user_input in [8, 5, 3]:
            b8 = bucket(8, False) if user_input == 8 else bucket(8)
            b5 = bucket(5, False) if user_input == 5 else bucket(5)
            b3 = bucket(3, False) if user_input == 3 else bucket(3)
            for bucket_xl, bucket_md, bucket_sm in zip_longest(b8, b5, b3, fillvalue=" "):
                print(bucket_xl, bucket_md, bucket_sm)
        else:
            print("Invalid option.")
    elif user_input.upper() == "E":
        for bucket_xl, bucket_md, bucket_sm in zip_longest(bucket(8), bucket(5), bucket(3), fillvalue=" "):
            print(bucket_xl, bucket_md, bucket_sm)
    elif user_input.upper() == "P":
        user_input = int(input(">: "))
        if user_input in [8, 5, 3]:
            b8 = bucket(8, False) if user_input == 8 else bucket(8)
            b5 = bucket(5, False) if user_input == 5 else bucket(5)
            b3 = bucket(3, False) if user_input == 3 else bucket(3)
            for bucket_xl, bucket_md, bucket_sm in zip_longest(b8, b5, b3, fillvalue=" "):
                print(bucket_xl, bucket_md, bucket_sm)
    else:
        playing = False