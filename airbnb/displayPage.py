"""
Given an array of CSV strings representing search results, output results sorted
by a score initially. A given host may have several listings that show up in
these results. Suppose we want to show 12 results per page, but we don’t want
the same host to dominate the results.

Write a function that will reorder the list so that a host shows up at most once
on a page if possible, but otherwise preserves the ordering. Your program
should return the new array and print out the results in blocks representing
the pages.

Given an array of csv strings, output results separated by a blank line.
"""

from collections import deque


def paginate(results):
    pages = []
    current_page = []
    host_set = set()
    buffer_queue = deque([])
    for i in range(len(results)):
        vals = results[i].split(',')
        if vals[0] not in host_set and len(current_page) < 12:
            current_page.append(results[i])
            host_set.add(vals[0])
        else:
            buffer_queue.append(results[i])
        if len(current_page) == 12:
            pages.append(current_page)
            current_page = []
            host_set.clear()
            new_buf_queue = deque([])
            while len(buffer_queue) > 0:
                elt = buffer_queue.popleft()
                if elt.split(',')[0] not in host_set and len(current_page) < 12:
                    current_page.append(elt)
                    host_set.add(elt.split(',')[0])
                else:
                    new_buf_queue.append(elt)
            buffer_queue = new_buf_queue

    buffer_queue = list(buffer_queue)
    if len(current_page) < 12:
        rem = int(12 - len(current_page))
        current_page = current_page + buffer_queue[0:rem]
    pages.append(current_page)
    if rem < len(buffer_queue):
        pages.append(buffer_queue[rem:])
    return pages


if __name__ == "__main__":
    A = [
        "1,28,300.1,SanFrancisco",
        "4,5,209.1,SanFrancisco",
        "20,7,208.1,SanFrancisco",
        "23,8,207.1,SanFrancisco",
        "16,10,206.1,Oakland",
        "1,16,205.1,SanFrancisco",
        "6,29,204.1,SanFrancisco",
        "7,20,203.1,SanFrancisco",
        "8,21,202.1,SanFrancisco",
        "2,18,201.1,SanFrancisco",
        "2,30,200.1,SanFrancisco",
        "15,27,109.1,Oakland",
        "10,13,108.1,Oakland",
        "11,26,107.1,Oakland",
        "12,9,106.1,Oakland",
        "13,1,105.1,Oakland",
        "22,17,104.1,Oakland",
        "1,2,103.1,Oakland",
        "28,24,102.1,Oakland",
        "18,14,11.1,SanJose",
        "6,25,10.1,Oakland",
        "19,15,9.1,SanJose",
        "3,19,8.1,SanJose",
        "3,11,7.1,Oakland",
        "27,12,6.1,Oakland",
        "1,3,5.1,Oakland",
        "25,4,4.1,SanJose",
        "5,6,3.1,SanJose",
        "29,22,2.1,SanJose",
        "30,23,1.1,SanJose"
    ]
    pages = paginate(A)
    for page in pages:
        for listing in page:
            print(listing)
        print()
