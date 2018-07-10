import heapq as hq
from sys import  getsizeof as gso
global cache

def read_in_chunks(file_object, file_size = 4*1024):
    while True:
        data = file_object.read(file_size)
        if not data:
            break
        yield data # say data is new line seprated ints

def sort_and_write_data(d, c):
    d = list(map(int, d.split('\n')))
    d = hq.heapify(d)
    for i in range(d):
        with open('temp_'+ c, 'ab+') as tf:  #temp file
            tf.write(hq.heappop(d)+'\n')

def merge(fl):
    '''
    At a time, Number of values in number_list would be available Cache/number
    of file. Try to make this count for each file.
    '''
    while True:
        '''
        WRONG LOGIC
        
        Modification:- Take bunch of elements from each file. Insert them in a 
        common heap. Also after fetching the elements, rewrite the file with the
        remaning element of the chuncked file.
        '''
        indiv_cache = int(cache/len(fl))
        numbers_list = []
        del_file = []
        for file in fl:
            # open each file
            with open(file, 'w+') as cf: #chunked file
                nums = cf.read().split('\n')
                count = 0
                temp = []
                # for each file fill temp till it reaches individual cache limit
                while gso(temp)< indiv_cache:
                    temp.extend(nums[count])
                numbers_list.extend(nums[count])
                if gso(temp) <= indiv_cache:    del_file.append(file);continue
                # write remaining elements back to file
                cf.write(nums[count:])
        hq.heapify(numbers_list)
        for i in range(len(numbers_list)):
            with open('output_file', 'ab+') as of: # output file, unless mode is 'r' whole file is not loaded
                of.write(hq.heappop(numbers_list))
        for df in del_file:
            files_list.remove(df)

        if files_list == []:
            break



if __name__=="__main__":
    file = open('input_file', 'rb')
    size = 1*1024 # see global cache
    count = 0
    files_list = []
    for data in read_in_chunks(file, file_size=size):
        count += 1
        files_list.append('temp_'+str(count))
        sort_and_write_data(data, str(count))

    merge(files_list)
    print ('output file with sorted data')

'''
https://www.geeksforgeeks.org/external-sorting/
https://github.com/Cbkhare/Codes/blob/master/Try_Sorting_Big_File.py

- divide the file into chunks and sort them
- take out fixed number of element from each file such that total count of each
  element is in the limit of cache
- Sort the list of elements and write in output file
- Append the outfile and donot load the whole file

'''