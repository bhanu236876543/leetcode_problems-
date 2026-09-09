class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        # Count vowels in the first window of k letters
        # vaka window lo mundhu anni vowles ni count cayali fro lopp tho 
        current = 0
        for i in range(k):
            if s[i] in vowels:
                current += 1

        # At first, this is also our best answer
        # as of now ela best ni pettukunaham
        best = current

        # Slide the window forward
        #increment cheyali
        for i in range(k, len(s)):
            # Add the new letter entering the window
            #innpudu end lo letter add chesam 
            if s[i] in vowels:
                current += 1

            # Remove the old letter leaving the window
            # starting dhi tesasam 
            if s[i - k] in vowels:
                current -= 1

            # Save the biggest vowel count found
            #eppudu edhi ite highest vowels vastdho adhi best lo store chayali 
            best = max(best, current)

        return best