
def chunk_generate(input_list, chunk_size):
    '''List Chunk Generate'''
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]
