from itertools import zip_longest
from typing import Iterable, Union, List

def bucket(size: int, water: int = 4, initial: bool = True) -> Iterable[str]:
    """
   Create bucket of specified sized.
   Params:
        size(int) -- size of the bucket to be built.
        water(int) -- amout of water.
        initial(bool) -- If first time create than it is in initial phase(True), which mean empty and hence vice-versa.
    Returns:
        This function return a list with bucket chuncks store as string, which can be built by looping on it.
   """ 
    length:int = size
    specified_index: List[int] = [n for n in range(1, length+1)]
    dummy_bucket: Union[str, List[str]] = f"""
 +------+
    {length}L   
    """
    # Typenarrowing
    if isinstance(dummy_bucket, str):
        dummy_bucket = dummy_bucket.splitlines()
    if initial:
        blockade = []
        for n in specified_index:
            value = "|      |"
            dummy_bucket.insert(n, f"{length}{value}")
            length -= 1
    else:
        blockade = [n for n in range(1, length + 1 - water)]
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

# Initial empty bucket display
for bucket_xl, bucket_md, bucket_sm in zip_longest(bucket(size=8), bucket(size=5), bucket(size=3), fillvalue=" "):
    print(bucket_xl, bucket_md, bucket_sm)

playing: bool = True
empty_bucket: bool = True
filled_bucket: List[int] = []
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

    # Fill the bucket. All logic related to filling the bucket is defined here.
    if user_input.upper() == "F":
        print("Select a bucket 8, 5, 3 or QUIT: ")
        user_input = int(input(">: "))
        if user_input in [8, 5, 3]:
            filled_bucket.clear()
            filled_bucket.append(user_input)
            f8 = bucket(size=8, initial=False) if user_input == 8 else bucket(8)
            f5 = bucket(size=5, initial=False) if user_input == 5 else bucket(5)
            f3 = bucket(size=3, initial=False) if user_input == 3 else bucket(3)
            for bucket_xl, bucket_md, bucket_sm in zip_longest(f8, f5, f3, fillvalue=" "):
                print(bucket_xl, bucket_md, bucket_sm)
            empty_bucket = False
        else:
            print("Invalid input.")
        
    # Empty the bucket.
    elif user_input.upper() == "E":
        for bucket_xl, bucket_md, bucket_sm in zip_longest(bucket(8), bucket(5), bucket(3), fillvalue=" "):
            print(bucket_xl, bucket_md, bucket_sm)

    # Pouring one bucket to another.
    elif user_input.upper() == "P":
        if empty_bucket:
            print("\n   Bucket's are empty.")
        else:
            print("Select a bucket 8, 5, 3 or QUIT: ")
            user_input = int(input(">: "))
            if user_input in [8, 5, 3]:
                p8 = bucket(size=8, initial=False) if user_input == 8 else bucket(8)                    
                p5 = bucket(size=5, initial=False) if user_input == 5 else bucket(5)
                p3 = bucket(size=3, initial=False) if user_input == 3 else bucket(3)
                if filled_bucket[0] == 8:
                    p8 = bucket(size=8, water=1, initial=False)
                elif filled_bucket[0] == 5:
                    p5 = bucket(size=5, water=1, initial=False)

                for bucket_xl, bucket_md, bucket_sm in zip_longest(p8, p5, p3, fillvalue=" "):
                    print(bucket_xl, bucket_md, bucket_sm)

    # Quit the game
    elif user_input.upper() == "Q":
        playing = False
    else:
        print("Invalid Input")