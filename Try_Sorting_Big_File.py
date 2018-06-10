import heapq as hq

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
        count = cache/len(fl)
        numbers_list = []
        del_file = []
        for file in fl:
            with open(file, 'w+') as cf: #chunked file
                nums = cf.read().split('\n')
                numbers_list.extend(nums[:count])
                nums = str(nums[:count]).replace('[','').replace(']','').replace(', ','\n')
                if len(nums)==0:    del_file.append(file)
                cf.write(nums)
        hq.heapify(numbers_list)
        for i in range(len(numbers_list)):
            with open('output_file', 'ab+') as of: #output file
                of.write(hq.heappop(numbers_list))
        for df in del_file:
            files_list.remove(df)

        if files_list == []:
            break 



if __name__=="__main__":
    file = open('input_file', 'rb')
    count = 0
    files_list = []
    for data in read_in_chunks(file):
        count += 1
        files_list.append('temp_'+str(count))
        sort_and_write_data(data, str(count))

    merge(files_list)
