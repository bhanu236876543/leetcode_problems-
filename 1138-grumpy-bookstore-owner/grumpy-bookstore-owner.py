class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_happy = 0
        saved = 0

        # Count happy customers already.
        # Also count unhappy customers in the first magic window.
        for i in range(len(customers)):
            if grumpy[i] == 0:
                already_happy += customers[i]
            elif i < minutes:
                saved += customers[i]

        best_saved = saved

        # Move the magic window one step at a time
        for i in range(minutes, len(customers)):
            # A new minute enters the window
            if grumpy[i] == 1:
                saved += customers[i]

            # An old minute leaves the window
            if grumpy[i - minutes] == 1:
                saved -= customers[i - minutes]

            best_saved = max(best_saved, saved)

        return already_happy + best_saved