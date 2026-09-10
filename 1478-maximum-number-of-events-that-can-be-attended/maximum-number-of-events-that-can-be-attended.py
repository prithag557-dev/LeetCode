import heapq

class Solution:
    def maxEvents(self, events):
        # Sort events by starting day
        events.sort()

        min_heap = []
        day = 0
        i = 0
        count = 0
        n = len(events)

        while i < n or min_heap:

            # If there are no active events,
            # jump directly to the next event's start day
            if not min_heap:
                day = events[i][0]

            # Add all events that have started
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                count += 1
                day += 1

        return count